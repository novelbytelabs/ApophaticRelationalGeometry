"""Command-line interface for the fail-closed ARG Phase 6 pilot runner."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pilot import (
    execute_pilot,
    load_frozen_bundle,
    pilot_plan,
    verify_model_baseline,
)


def _canonical_print(value: object) -> None:
    print(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=("validate", "plan", "execute"),
        help="validate/plan are data-free; execute requires the fixed committed authorization record",
    )
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--archive",
        type=Path,
        default=Path("artifacts/phase6_pilot"),
        help="new empty destination used only by the execute command",
    )
    args = parser.parse_args()

    bundle = load_frozen_bundle(args.repo_root)
    source_commit = verify_model_baseline(bundle.repo_root, bundle.protocol)
    if args.command == "validate":
        _canonical_print(
            {
                "protocol_id": bundle.protocol["protocol_id"],
                "protocol_version": bundle.protocol["protocol_version"],
                "source_commit": source_commit,
                "lock": "PASS",
                "model_baseline": "PASS",
                "pilot_executed": False,
                "confirmatory_execution": "BLOCKED",
            }
        )
        return
    if args.command == "plan":
        plan = pilot_plan(bundle)
        plan["source_commit"] = source_commit
        _canonical_print(plan)
        return
    execute_pilot(bundle.repo_root, args.archive)


if __name__ == "__main__":
    main()
