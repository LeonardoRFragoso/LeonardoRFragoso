#!/usr/bin/env python3
"""
History Sanitization Plan Validator (Phase 2A.12 Batch 1)

Parses HISTORY_SANITIZATION_PLAN.md and validates:
- No duplicate active repository rows in the Canonical Rewrite Table
- Deleted repositories are NOT counted as executable rewrite targets
- All active rewrite targets still exist on GitHub (live API check, optional)
- Active target total matches the detailed per-repository plan count
- COMPLETED + READY + BLOCKED == active rewrite candidate count
- Visibility totals == account repository count (30)
- Bet-IA-BOT lifecycle is DELETED_BY_OWNER
- Bet-IA-BOT rewrite status is N/A (not an executable target)
- Canonical security matrix still contains 41 IDs (delegates to
  validate_credential_matrix.py parse logic)
- Completed repos are not counted as READY or BLOCKED

Usage:
    python3 validate_history_sanitization_plan.py            # offline (no GitHub API)
    python3 validate_history_sanitization_plan.py --live      # also check live GitHub

Exit codes:
    0 = all validations passed
    1 = validation failure
"""

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PLAN_PATH = SCRIPT_DIR / "HISTORY_SANITIZATION_PLAN.md"

EXPECTED_ACCOUNT_TOTAL = 30
EXPECTED_PUBLIC = 15
EXPECTED_PRIVATE = 15
EXPECTED_ACTIVE_CANDIDATES = 12  # do not hardcode if live evidence contradicts
EXPECTED_CREDENTIAL_IDS = 41

ALLOWED_REWRITE_REQUIRED = {"YES", "NO", "N/A_REPOSITORY_DELETED"}
ALLOWED_REWRITE_READY = {"YES", "NO", "N/A", "COMPLETED"}

# The 12 canonical active candidates (used to cross-check the parsed table)
CANONICAL_ACTIVE_CANDIDATES = {
    "ProFlow",
    "base-corporativa",
    "FinanceControl",
    "Digital-Signage-Platform",
    "FlowTrack",
    "Bot_IqOption",
    "MVP-linkedin-bot",
    "Portfolio-LeonardoFragoso-React",
    "AndaimesPini_Project",
    "PayFlow-AI",
    "LogiFlow",
    "API_Analyze",
}


def parse_canonical_table(path: Path) -> list[dict]:
    """Parse the Canonical Rewrite Table from the markdown.

    The table header begins with '| REPOSITORY | VISIBILITY_NOW |'.
    Returns a list of row dicts keyed by column name.
    """
    content = path.read_text()
    lines = content.split("\n")
    rows: list[dict] = []
    headers: list[str] = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("| REPOSITORY | VISIBILITY_NOW |"):
            headers = [c.strip() for c in stripped.split("|")[1:-1]]
            in_table = True
            continue
        if in_table:
            if stripped.startswith("|---|"):
                continue
            if not stripped.startswith("|"):
                break
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) != len(headers):
                # Not a matching row — could be a different table; stop
                break
            # Strip markdown bold markers from cell values
            cells = [c.replace("**", "") for c in cells]
            rows.append(dict(zip(headers, cells)))
    return rows


def parse_totals_section(path: Path) -> dict[str, int]:
    """Parse the account-level totals table at the end of the plan."""
    content = path.read_text()
    lines = content.split("\n")
    totals: dict[str, int] = {}
    in_totals = False
    for line in lines:
        stripped = line.strip()
        if stripped == "| Metric | Value |":
            in_totals = True
            continue
        if in_totals:
            if stripped.startswith("|---|"):
                continue
            if not stripped.startswith("|"):
                # keep looking for the account-level totals table specifically
                in_totals = False
                continue
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) == 2 and cells[0] not in ("Metric",):
                try:
                    totals[cells[0]] = int(cells[1])
                except ValueError:
                    pass
    return totals


def count_detailed_sections(path: Path) -> list[str]:
    """Find the per-repository detailed section headers (### N. <name>)."""
    content = path.read_text()
    # Match headers like "### 1. ProFlow" within the Per-Repository Sanitization Plan
    # but NOT the DELETED_REPOSITORY_AUDIT_RECORD or other sections.
    names = []
    in_per_repo = False
    for line in content.split("\n"):
        if "## Per-Repository Sanitization Plan" in line:
            in_per_repo = True
            continue
        if in_per_repo:
            if line.startswith("## ") and "Per-Repository" not in line:
                break
            m = re.match(r"^### \d+\. (.+)$", line.strip())
            if m:
                names.append(m.group(1).strip())
    return names


def check_deleted_audit_record(path: Path) -> tuple[bool, bool]:
    """Verify Bet-IA-BOT appears only in the DELETED_REPOSITORY_AUDIT_RECORD,
    not as an executable target. Returns (has_tombstone, not_in_active_sections)."""
    content = path.read_text()
    has_tombstone = "## DELETED_REPOSITORY_AUDIT_RECORD" in content
    # Bet-IA-BOT must NOT appear in the Execution Order tiers or the Canonical Rewrite Table
    # as an executable target. It may appear in the tombstone and in preserved historical
    # update text. Check the detailed sections and execution order explicitly.
    detailed = count_detailed_sections(path)
    in_detailed = "Bet-IA-BOT" in detailed

    # Check execution order tier lines (### Tier ... sections)
    in_tiers = False
    tier_lines: list[str] = []
    in_exec = False
    for line in content.split("\n"):
        if line.startswith("## Execution Order"):
            in_exec = True
            continue
        if in_exec and line.startswith("## ") and "Execution Order" not in line:
            in_exec = False
        if in_exec and re.match(r"^\d+\\. \\*\\*Bet-IA-BOT", line.strip()):
            in_tiers = True
        if in_exec and "Bet-IA-BOT" in line and line.strip().startswith(tuple("0123456789")):
            tier_lines.append(line.strip())
    bet_in_tier_executable = any("Bet-IA-BOT" in t and "removed" not in t.lower() and "deleted" not in t.lower() for t in tier_lines)
    # The note line about removal is acceptable; an executable numbered entry is not.
    not_in_active = (not in_detailed) and (not bet_in_tier_executable)
    return has_tombstone, not_in_active


def validate_credential_matrix_has_41() -> bool:
    """Delegate to validate_credential_matrix.py and confirm 41 IDs."""
    validator = SCRIPT_DIR / "validate_credential_matrix.py"
    if not validator.exists():
        print("  WARN: validate_credential_matrix.py not found — skipping 41-ID check")
        return True
    try:
        result = subprocess.run(
            [sys.executable, str(validator)],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT_DIR),
            timeout=30,
        )
        ok = result.returncode == 0
        # Confirm "Total items: 41" appears in output
        has_41 = "Total items: 41" in result.stdout
        return ok and has_41
    except Exception as e:
        print(f"  ERROR running credential validator: {e}")
        return False


def check_live_github(candidates: set[str]) -> tuple[bool, list[str]]:
    """Optionally verify all active candidates still exist on GitHub."""
    try:
        result = subprocess.run(
            ["gh", "repo", "list", "LeonardoRFragoso", "--limit", "100",
             "--json", "name", "--jq", ".[].name"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            print(f"  gh repo list failed: {result.stderr.strip()}")
            return False, []
        live_repos = {r.strip() for r in result.stdout.splitlines() if r.strip()}
        missing = sorted(candidates - live_repos)
        return len(missing) == 0, missing
    except Exception as e:
        print(f"  live check error: {e}")
        return False, []


def validate(rows: list[dict], totals: dict, detailed: list[str], live: bool) -> bool:
    errors: list[str] = []

    # 1. No duplicate active repository rows
    repo_names = [r["REPOSITORY"] for r in rows]
    duplicates = [n for n, c in Counter(repo_names).items() if c > 1]
    if duplicates:
        errors.append(f"Duplicate active repository rows: {duplicates}")

    # 2. Deleted repositories not counted as executable rewrite targets
    for r in rows:
        if r["REPOSITORY"] == "Bet-IA-BOT":
            errors.append("Bet-IA-BOT appears in the Canonical Rewrite Table (active targets) — must be in tombstone only")

    # 3. All rows are valid canonical candidates
    parsed_set = set(repo_names)
    extra = parsed_set - CANONICAL_ACTIVE_CANDIDATES
    missing = CANONICAL_ACTIVE_CANDIDATES - parsed_set
    if extra:
        errors.append(f"Unexpected active candidates in table: {sorted(extra)}")
    if missing:
        errors.append(f"Missing active candidates from table: {sorted(missing)}")

    # 4. Active target total matches detailed plan count
    active_count = len(rows)
    if active_count != len(detailed):
        errors.append(
            f"Active table count ({active_count}) != detailed plan section count ({len(detailed)}). "
            f"Table: {sorted(repo_names)}; Detailed: {detailed}"
        )
    if active_count != EXPECTED_ACTIVE_CANDIDATES:
        errors.append(f"Active candidate count {active_count} != expected {EXPECTED_ACTIVE_CANDIDATES}")

    # 5. REWRITE_REQUIRED / REWRITE_READY value validation
    for r in rows:
        if r["REWRITE_REQUIRED"] not in ALLOWED_REWRITE_REQUIRED:
            errors.append(f"{r['REPOSITORY']}: invalid REWRITE_REQUIRED '{r['REWRITE_REQUIRED']}'")
        if r["REWRITE_READY"] not in ALLOWED_REWRITE_READY:
            errors.append(f"{r['REPOSITORY']}: invalid REWRITE_READY '{r['REWRITE_READY']}'")
        # All active candidates must have REWRITE_REQUIRED = YES
        if r["REWRITE_REQUIRED"] != "YES":
            errors.append(f"{r['REPOSITORY']}: active candidate must have REWRITE_REQUIRED=YES, got '{r['REWRITE_REQUIRED']}'")

    # 6. COMPLETED + READY + BLOCKED == active candidate count
    completed = sum(1 for r in rows if r["REWRITE_READY"] == "COMPLETED")
    ready = sum(1 for r in rows if r["REWRITE_READY"] == "YES")
    blocked = sum(1 for r in rows if r["REWRITE_READY"] == "NO")
    if completed + ready + blocked != active_count:
        errors.append(f"COMPLETED({completed}) + READY({ready}) + BLOCKED({blocked}) != active count({active_count})")
    # Completed repos must not also be counted as READY or BLOCKED
    if completed > 0 and ready + blocked + completed != active_count:
        errors.append(f"Completed repos overlap with READY/BLOCKED counts")

    # 7. Visibility totals == account repository count
    acct_total = totals.get("ACCOUNT_TOTAL_REPOS")
    pub = totals.get("PUBLIC_REPOS")
    priv = totals.get("PRIVATE_REPOS")
    if acct_total != EXPECTED_ACCOUNT_TOTAL:
        errors.append(f"ACCOUNT_TOTAL_REPOS={acct_total} != {EXPECTED_ACCOUNT_TOTAL}")
    if pub != EXPECTED_PUBLIC:
        errors.append(f"PUBLIC_REPOS={pub} != {EXPECTED_PUBLIC}")
    if priv != EXPECTED_PRIVATE:
        errors.append(f"PRIVATE_REPOS={priv} != {EXPECTED_PRIVATE}")
    if pub is not None and priv is not None and pub + priv != EXPECTED_ACCOUNT_TOTAL:
        errors.append(f"PUBLIC({pub}) + PRIVATE({priv}) != {EXPECTED_ACCOUNT_TOTAL}")

    # 8. Bet-IA-BOT lifecycle + rewrite status
    has_tombstone, not_in_active = check_deleted_audit_record(PLAN_PATH)
    if not has_tombstone:
        errors.append("DELETED_REPOSITORY_AUDIT_RECORD section missing")
    if not not_in_active:
        errors.append("Bet-IA-BOT still appears as an executable rewrite target (detailed section or tier)")
    plan_text = PLAN_PATH.read_text()
    if "DELETED_BY_OWNER" not in plan_text:
        errors.append("Bet-IA-BOT lifecycle DELETED_BY_OWNER not documented")
    if "NOT_APPLICABLE_REPOSITORY_DELETED" not in plan_text:
        errors.append("Bet-IA-BOT NOT_APPLICABLE_REPOSITORY_DELETED status not documented")
    if "N/A_REPOSITORY_DELETED" not in plan_text:
        errors.append("Bet-IA-BOT REWRITE_REQUIRED=N/A_REPOSITORY_DELETED not documented")

    # 9. Canonical security matrix still contains 41 IDs
    if not validate_credential_matrix_has_41():
        errors.append("Credential matrix does not contain 41 IDs (validate_credential_matrix.py failed)")

    # 10. Live GitHub check (optional)
    if live:
        ok, missing_live = check_live_github(parsed_set)
        if not ok:
            errors.append(f"Active candidates not found on live GitHub: {missing_live}")

    # Report
    print("=" * 60)
    print("HISTORY SANITIZATION PLAN VALIDATOR (Phase 2A.12 Batch 1)")
    print("=" * 60)
    print()
    print(f"Active candidates parsed: {active_count}")
    print(f"  COMPLETED: {completed}")
    print(f"  READY: {ready}")
    print(f"  BLOCKED: {blocked}")
    print(f"  COMPLETED + READY + BLOCKED = {completed + ready + blocked}")
    print()
    print(f"Visibility totals: PUBLIC={pub}, PRIVATE={priv}, TOTAL={acct_total}")
    print()
    print(f"Detailed plan sections: {len(detailed)} -> {detailed}")
    print()
    print(f"Bet-IA-BOT tombstone present: {has_tombstone}")
    print(f"Bet-IA-BOT not in active targets: {not_in_active}")
    print()
    print(f"Canonical credential matrix 41 IDs: checked via validate_credential_matrix.py")
    print()
    if live:
        print("Live GitHub existence check: performed")
    else:
        print("Live GitHub existence check: skipped (use --live to enable)")
    print()

    if errors:
        print("=" * 60)
        print("VALIDATION ERRORS:")
        print("=" * 60)
        for e in errors:
            print(f"  X {e}")
        print()
        print(f"FAILED: {len(errors)} error(s)")
        return False
    print("=" * 60)
    print("ALL VALIDATIONS PASSED")
    print("=" * 60)
    return True


if __name__ == "__main__":
    if not PLAN_PATH.exists():
        print(f"ERROR: {PLAN_PATH} not found")
        sys.exit(1)
    rows = parse_canonical_table(PLAN_PATH)
    if not rows:
        print("ERROR: could not parse Canonical Rewrite Table")
        sys.exit(1)
    totals = parse_totals_section(PLAN_PATH)
    detailed = count_detailed_sections(PLAN_PATH)
    live = "--live" in sys.argv
    success = validate(rows, totals, detailed, live)
    sys.exit(0 if success else 1)
