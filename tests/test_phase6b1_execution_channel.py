from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_governed_pilot_execution_workflow_is_authorization_only() -> None:
    workflow = (
        REPO_ROOT / ".github/workflows/phase6b-pilot-execution.yml"
    ).read_text(encoding="utf-8")
    assert "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json" in workflow
    assert "ref: ${{ github.sha }}" in workflow
    assert "git diff --name-only HEAD^ HEAD" in workflow
    assert "arg-pilot execute" in workflow
    assert "verify_pilot_archive" in workflow
    assert "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02" in workflow
    assert "confirmatory" not in workflow.lower()

    tests_workflow = (REPO_ROOT / ".github/workflows/tests.yml").read_text(
        encoding="utf-8"
    )
    assert "paths-ignore:" in tests_workflow
    assert "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json" in tests_workflow
