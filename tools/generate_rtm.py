from __future__ import annotations
from datetime import date
from pathlib import Path

CSV = """RequirementID,Requirement,ControlID,ImplementationRef,ValidationEvidence,Acceptance
REQ-001,Authenticate users,IA-5,Repo1/implementations/IA-5-authenticator-management.md,Repo1/evidence/IA-5/mfa-enforcement.md,Planned
REQ-002,Log auth failures,AU-2,Repo1/implementations/AU-2-audit-events.md,Repo1/evidence/AU-2/log-review-checklist.md,Planned
REQ-003,Quarterly access reviews,AC-2,Repo1/implementations/AC-2-account-management.md,Repo1/evidence/AC-2/account-review-log.md,Planned
"""

def main() -> None:
    today = date.today().isoformat()
    out_dir = Path("generated")
    out_dir.mkdir(parents=True, exist_ok=True)

    rtm_path = out_dir / f"rtm-{today}.csv"
    rtm_path.write_text(CSV, encoding="utf-8")

    rows = CSV.strip().splitlines()
    count = len(rows) - 1
    summary = f"""RTM Summary (Generated)

Generated: {today}
Row count: {count}

Controls referenced:
- IA-5
- AU-2
- AC-2
"""
    (out_dir / f"rtm-summary-{today}.md").write_text(summary, encoding="utf-8")
    print("Wrote RTM and summary.")

if __name__ == "__main__":
    main()
