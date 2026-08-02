#!/usr/bin/env python3
"""ARG audit tripwire. Usage: python arg_tripwire.py /path/to/bundle-root"""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

DANGEROUS = {
    "eval": re.compile(r"\beval\s*\("),
    "exec": re.compile(r"\bexec\s*\("),
    "importlib": re.compile(r"\bimportlib\b"),
    "ctypes": re.compile(r"\bctypes\b"),
    "os.system": re.compile(r"\bos\.system\s*\("),
}
REQUIRED_ROWS = {
    "source_commit","protocol_id","protocol_version","contract_version",
    "config_id","inferential_unit","split","model_id","integrator",
    "dt_or_tolerance_profile","step","time",
}

RUNTIME_PATHS = [
    str(Path(p).resolve()) for p in sys.path
    if p and Path(p).is_dir()
]

SITE_GUARD = r"""
import os, socket, sys
from pathlib import Path
roots = [Path(p).resolve() for p in os.environ.get("AUDIT_ALLOWED_ROOTS","").split(os.pathsep) if p]
for p in (sys.prefix, sys.base_prefix, "/usr/lib", "/lib", "/usr/share", "/dev/null"):
    try: roots.append(Path(p).resolve())
    except Exception: pass
def inside(path):
    try:
        p = Path(path).resolve()
        return any(p == r or r in p.parents for r in roots)
    except Exception:
        return False
def audit(event, args):
    if event.startswith("socket.") or event in {"subprocess.Popen","os.system","os.posix_spawn","os.fork","os.forkpty"}:
        raise PermissionError("network/IPC/process creation blocked by audit harness")
    if event == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
        if not inside(args[0]):
            raise PermissionError(f"filesystem access outside sandbox blocked: {args[0]}")
sys.addaudithook(audit)
def denied(*a, **k): raise PermissionError("network/IPC blocked by audit harness")
socket.socket = denied
socket.create_connection = denied
for name in ("system","popen","fork","forkpty","mkfifo"):
    if hasattr(os, name): setattr(os, name, denied)
"""

PROBE = r"""
import csv, json, os, sys, tempfile
from pathlib import Path
import numpy as np
from apophatic_geometry.model import Parameters, State, intrinsic_edge_lengths
from apophatic_geometry.models import (
    ModelId, ProjectionTarget, derivatives_for_model, rk4_step
)
from apophatic_geometry.simulate import run
from tests.reference_equations import reference_derivative, reference_rk4_step

report = {}
rng = np.random.Generator(np.random.PCG64(20260801))
params = Parameters()
state = State(
    x=np.array([0.8,-0.25,0.45]),
    s=np.array([0.2,-0.1,0.1]),
    q=np.array([0.0,0.05,-0.05]),
)
# Constant-output tripwire.
mut = State(x=state.x + np.array([0.01,0,0]), s=state.s.copy(), q=state.q.copy())
a = derivatives_for_model(state, params, ModelId.MF).pack()
b = derivatives_for_model(mut, params, ModelId.MF).pack()
report["nonconstant_output"] = bool(not np.array_equal(a,b))

# Differential checks at FP64 gates.
max_deriv = 0.0
max_step = 0.0
differential_ok = True
for _ in range(32):
    x = rng.normal(size=3)
    x = x / np.linalg.norm(x) * rng.uniform(np.sqrt(3e-6), np.sqrt(3.0))
    st = State(x=x, s=rng.uniform(-2,2,3), q=rng.uniform(-1,1,3))
    target = ProjectionTarget.from_state(st)
    for mid in ModelId:
        kw = {"target":target} if mid in (ModelId.MP,ModelId.MFP) else {}
        got = derivatives_for_model(st, params, mid, **kw).pack()
        ref = reference_derivative(st, params, mid.value, c0=target.c0 if kw else None).pack()
        max_deriv = max(max_deriv, float(np.max(np.abs(got-ref))))
        differential_ok &= bool(np.allclose(got,ref,rtol=1e-12,atol=1e-13))
        got2 = rk4_step(st,params,0.001,mid,**kw).pack()
        ref2 = reference_rk4_step(st,params,0.001,mid.value,c0=target.c0 if kw else None).pack()
        max_step = max(max_step, float(np.max(np.abs(got2-ref2))))
        differential_ok &= bool(np.allclose(got2,ref2,rtol=1e-12,atol=1e-13))
report["differential_fp64"] = differential_ok
report["differential_max_derivative_abs"] = max_deriv
report["differential_max_step_abs"] = max_step

# Metamorphic global sign check.
neg = State(x=-state.x, s=state.s.copy(), q=state.q.copy())
sign_ok = True
for mid in ModelId:
    t1 = ProjectionTarget.from_state(state) if mid in (ModelId.MP,ModelId.MFP) else None
    t2 = ProjectionTarget.from_state(neg) if mid in (ModelId.MP,ModelId.MFP) else None
    p = rk4_step(state,params,0.005,mid,target=t1)
    n = rk4_step(neg,params,0.005,mid,target=t2)
    sign_ok &= bool(np.allclose(p.x,-n.x,rtol=1e-12,atol=1e-13))
    sign_ok &= bool(np.allclose(p.s,n.s,rtol=1e-12,atol=1e-13))
    sign_ok &= bool(np.allclose(p.q,n.q,rtol=1e-12,atol=1e-13))
report["global_sign_metamorphic"] = sign_ok

# Fail-closed exception tripwires.
def raises(fn):
    try: fn()
    except Exception: return True
    return False
report["rejects_invalid_dt"] = raises(lambda: rk4_step(state,params,0.0,ModelId.MF))
report["rejects_nonfinite_state"] = raises(
    lambda: State(x=np.array([np.nan,0,0]),s=np.zeros(3),q=np.zeros(3))
)
report["rejects_wrong_projection_target"] = raises(
    lambda: rk4_step(state,params,0.005,ModelId.MP,target=ProjectionTarget(c0=1.0))
)

# Extreme finite geometry must remain finite/positive or fail closed.
extreme_ok = True
for qv in (-1000.0, 1000.0):
    st = State(x=np.array([1.0,0.0,-1.0]),s=np.zeros(3),q=np.full(3,qv))
    try:
        lengths = intrinsic_edge_lengths(st,params)
        extreme_ok &= bool(np.all(np.isfinite(lengths)) and np.all(lengths > 0))
    except (FloatingPointError, ValueError, OverflowError):
        pass
report["extreme_geometry_fails_closed"] = extreme_ok

# Frozen-container aliasing tripwire.
raw = np.array([1.0,2.0,3.0])
frozen = State(x=raw,s=np.zeros(3),q=np.zeros(3))
raw[0] = 9.0
report["state_is_immutable_copy"] = bool(frozen.x[0] == 1.0 and not frozen.x.flags.writeable)

# Output schema, determinism, hidden environment flags, and partial-write behavior.
work = Path(os.environ["AUDIT_WORK"])
p1, p2 = work/"a.csv", work/"b.csv"
run(steps=3,dt=0.005,output=p1,model=ModelId.MF)
run(steps=3,dt=0.005,output=p2,model=ModelId.MF)
report["deterministic_bytes"] = bool(p1.read_bytes() == p2.read_bytes())
with p1.open(newline="",encoding="utf-8") as h:
    rows = list(csv.DictReader(h))
    fields = set(rows[0])
report["required_protocol_row_fields"] = bool(set(json.loads(os.environ["AUDIT_REQUIRED_ROWS"])) <= fields)
report["source_commit_label"] = rows[0]["source_commit"]
report["configuration_hash"] = rows[0]["configuration_hash"]
partial = work/"partial.csv"
failed = raises(lambda: run(steps=5,dt=1e100,output=partial,model=ModelId.MF))
report["exception_propagates"] = failed
report["failed_run_leaves_no_output"] = bool(not partial.exists())
print(json.dumps(report,sort_keys=True,allow_nan=False))
"""

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def limits():
    import resource
    resource.setrlimit(resource.RLIMIT_CPU, (20,20))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3,1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (64*1024**2,64*1024**2))

def run_child(work: Path, guard: Path, extra_env: dict[str,str] | None = None):
    env = {
        "PATH": os.environ.get("PATH",""),
        "PYTHONPATH": os.pathsep.join([str(guard),str(work/"src"),str(work),*RUNTIME_PATHS]),
        "PYTHONHASHSEED":"0","PYTHONNOUSERSITE":"1",
        "OMP_NUM_THREADS":"1","OPENBLAS_NUM_THREADS":"1","MKL_NUM_THREADS":"1",
        "AUDIT_ALLOWED_ROOTS":os.pathsep.join([str(work),str(guard),*RUNTIME_PATHS]),
        "AUDIT_WORK":str(work/"probe-output"),
        "AUDIT_REQUIRED_ROWS":json.dumps(sorted(REQUIRED_ROWS)),
        "PYTEST_DISABLE_PLUGIN_AUTOLOAD":"1",
    }
    (work/"probe-output").mkdir(exist_ok=True)
    if extra_env: env.update(extra_env)
    p = subprocess.run(
        [sys.executable,"-S","-c","import sitecustomize\n"+PROBE],cwd=work,env=env,
        text=True,capture_output=True,timeout=30,
        preexec_fn=limits if os.name == "posix" else None,
    )
    if p.returncode != 0:
        return None, f"probe rc={p.returncode}: {p.stderr[-1000:]}"
    try: return json.loads(p.stdout.strip().splitlines()[-1]), None
    except Exception as e: return None, f"invalid probe JSON: {e}; stdout={p.stdout[-1000:]}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root",type=Path)
    args = ap.parse_args()
    srcroot = args.root.resolve()
    results: list[tuple[str,bool,str]] = []
    def add(name, ok, detail=""): results.append((name,bool(ok),detail))

    with tempfile.TemporaryDirectory(prefix="arg-tripwire-") as td:
        work = Path(td)/"bundle"
        shutil.copytree(srcroot,work,ignore=shutil.ignore_patterns(
            "__pycache__",".pytest_cache",".coverage","build","*.egg-info"
        ))
        guard = Path(td)/"guard"; guard.mkdir()
        (guard/"sitecustomize.py").write_text(SITE_GUARD,encoding="utf-8")

        # Static dangerous API scan.
        hits=[]
        for p in sorted((work/"src").rglob("*.py")):
            text=p.read_text(encoding="utf-8")
            for name,pat in DANGEROUS.items():
                if pat.search(text): hits.append(f"{p.relative_to(work)}:{name}")
        add("dangerous_api_scan",not hits,", ".join(hits))

        # Audit manifest and frozen lock.
        manifest=json.loads((work/"AUDIT_MANIFEST.json").read_text())
        bad=[]
        for rel,exp in manifest.get("sha256",{}).items():
            p=work/rel
            if not p.is_file() or sha256(p)!=exp: bad.append(rel)
        add("audit_manifest_hashes",not bad,", ".join(bad))
        lock=json.loads((work/"protocol/phase5_v1/LOCK.json").read_text())
        lock_bad=[]
        for rel,exp in lock["files"].items():
            p=work/rel
            if not p.is_file():
                lock_bad.append(f"{rel}:missing"); continue
            if p.suffix.lower()==".json":
                obj=json.loads(p.read_text())
                got=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
            else: got=sha256(p)
            if got!=exp: lock_bad.append(f"{rel}:hash")
        add("phase5_lock_complete",not lock_bad,", ".join(lock_bad))

        # Full advertised test command in a fresh subprocess.
        env=os.environ.copy()
        env.update({
            "PYTHONPATH":os.pathsep.join([str(guard),str(work/"src"),str(work),*RUNTIME_PATHS]),
            "PYTHONHASHSEED":"0","PYTHONNOUSERSITE":"1",
            "OMP_NUM_THREADS":"1","OPENBLAS_NUM_THREADS":"1","MKL_NUM_THREADS":"1",
            "PYTEST_DISABLE_PLUGIN_AUTOLOAD":"1",
            "AUDIT_ALLOWED_ROOTS":os.pathsep.join([str(work),str(guard),*RUNTIME_PATHS]),
        })
        try:
            pytest_code="import sitecustomize, pytest; raise SystemExit(pytest.main(['-q']))"
            p=subprocess.run([sys.executable,"-S","-c",pytest_code],cwd=work,env=env,
                text=True,capture_output=True,timeout=40,
                preexec_fn=limits if os.name=="posix" else None)
            add("advertised_pytest",p.returncode==0,(p.stdout+p.stderr)[-1200:])
        except Exception as e:
            add("advertised_pytest",False,str(e))

        # Determinism and adversarial probes.
        base1,e1=run_child(work,guard,{"ARG_SOURCE_COMMIT":"baseline"})
        shutil.rmtree(work/"probe-output",ignore_errors=True)
        base2,e2=run_child(work,guard,{"ARG_SOURCE_COMMIT":"baseline"})
        shutil.rmtree(work/"probe-output",ignore_errors=True)
        toggled,e3=run_child(work,guard,{
            "ARG_SOURCE_COMMIT":"forged","TEST_MODE":"1","DEBUG":"1",
            "STUB_MODE":"1","ATTESTATION_MODE":"0",
        })
        if e1 or e2 or e3:
            add("probe_execution",False,"; ".join(x for x in (e1,e2,e3) if x))
        else:
            add("fresh_subprocess_determinism",base1==base2)
            for key in (
                "nonconstant_output","differential_fp64","global_sign_metamorphic",
                "rejects_invalid_dt","rejects_nonfinite_state",
                "rejects_wrong_projection_target","extreme_geometry_fails_closed",
                "state_is_immutable_copy","deterministic_bytes",
                "required_protocol_row_fields","exception_propagates",
                "failed_run_leaves_no_output",
            ):
                add(key,base1.get(key,False),json.dumps(base1.get(key)))
            behavior_keys=set(base1)-{"source_commit_label"}
            hidden_ok=all(base1[k]==toggled[k] for k in behavior_keys)
            add("hidden_env_does_not_change_behavior",hidden_ok)
            add("source_commit_is_attested_not_env_supplied",
                base1["source_commit_label"]==toggled["source_commit_label"],
                f'{base1["source_commit_label"]!r} vs {toggled["source_commit_label"]!r}')

    failed=[r for r in results if not r[1]]
    print("ARG TRIPWIRE REPORT")
    for name,ok,detail in results:
        print(f'{"PASS" if ok else "FAIL"} {name}' + (f" :: {detail}" if detail and not ok else ""))
    print(f"SUMMARY: {len(results)-len(failed)} PASS / {len(failed)} FAIL")
    sys.exit(1 if failed else 0)

if __name__=="__main__":
    main()
