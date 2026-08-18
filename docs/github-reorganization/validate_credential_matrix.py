#!/usr/bin/env python3
"""
Credential Rotation Matrix Validator

Parses the Updated Summary Table in CREDENTIAL_ROTATION_MATRIX.md and
validates that:
- Exactly 41 unique items exist (IDs 1..41)
- No duplicate IDs
- Each item has exactly one TYPE from: CREDENTIAL, SESSION, LOCAL_APP_SECRET, PII
- Each item has exactly one REMEDIATION_CLASS from the allowed set
- Each item has a valid OWNER
- Each item has a valid PROJECT_RUNTIME_STATUS
- All totals sum to 41

Usage:
    python3 validate_credential_matrix.py

Exit codes:
    0 = all validations passed
    1 = validation failure
"""

import re
import sys
from collections import Counter
from pathlib import Path

VALID_TYPES = {"CREDENTIAL", "SESSION", "LOCAL_APP_SECRET", "PII"}
VALID_REMEDIATION_CLASSES = {
    "ROTATE_AND_REDEPLOY",
    "REVOKE_ONLY",
    "INVALIDATE_SESSION",
    "CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS",
    "OWNER_HANDOFF",
    "GENERATE_NEW_LOCAL_SECRET",
    "REMOVE_PII_FROM_HISTORY",
    "NOT_APPLICABLE",
    "ALREADY_INVALIDATED_WITH_EVIDENCE",
    "UNKNOWN_REQUIRES_MANUAL_CHECK",
}
VALID_OWNERS = {"Leonardo", "ICTSI/iTracker", "ICTSI", "UNKNOWN"}
VALID_RUNTIME_STATUSES = {
    "ACTIVE_PRODUCTION",
    "ACTIVE_DEVELOPMENT",
    "INACTIVE",
    "ARCHIVED_IN_PRACTICE",
}
EXPECTED_ITEM_COUNT = 41


def parse_matrix(filepath: str) -> list[dict]:
    """Parse the markdown table and return list of item dicts."""
    content = Path(filepath).read_text()
    lines = content.split("\n")
    items = []
    in_table = False
    for line in lines:
        # Detect the start of the Updated Summary Table
        if "| # | Repo" in line:
            in_table = True
            continue
        if in_table:
            # Skip header separator
            if line.startswith("|---|"):
                continue
            # End of table
            if not line.startswith("|"):
                break
            # Parse row
            cells = [c.strip() for c in line.split("|")]
            # Remove empty first/last from leading/trailing |
            cells = [c for c in cells if c != ""]
            if len(cells) < 9:
                continue
            try:
                item_id = int(cells[0])
            except ValueError:
                continue
            items.append({
                "id": item_id,
                "repo": cells[1],
                "provider": cells[2],
                "type_desc": cells[3],
                "type": cells[4],
                "runtime_status": cells[5],
                "remediation_class": cells[6],
                "owner": cells[7],
                "active_deployment": cells[8],
                "next_action": cells[9] if len(cells) > 9 else "",
            })
    return items


def validate(items: list[dict]) -> bool:
    """Run all validations. Returns True if all pass."""
    errors = []
    warnings = []

    # Check count
    if len(items) != EXPECTED_ITEM_COUNT:
        errors.append(f"Expected {EXPECTED_ITEM_COUNT} items, found {len(items)}")

    # Check IDs are 1..41, no duplicates
    ids = [item["id"] for item in items]
    duplicates = [id for id, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate IDs: {duplicates}")

    expected_ids = set(range(1, EXPECTED_ITEM_COUNT + 1))
    actual_ids = set(ids)
    missing = expected_ids - actual_ids
    extra = actual_ids - expected_ids
    if missing:
        errors.append(f"Missing IDs: {sorted(missing)}")
    if extra:
        errors.append(f"Unexpected IDs: {sorted(extra)}")

    # Check each item has valid TYPE, REMEDIATION_CLASS, OWNER, RUNTIME_STATUS
    for item in items:
        if item["type"] not in VALID_TYPES:
            errors.append(
                f"Item {item['id']}: invalid TYPE '{item['type']}'. "
                f"Must be one of {VALID_TYPES}"
            )
        if item["remediation_class"] not in VALID_REMEDIATION_CLASSES:
            errors.append(
                f"Item {item['id']}: invalid REMEDIATION_CLASS '{item['remediation_class']}'. "
                f"Must be one of {VALID_REMEDIATION_CLASSES}"
            )
        if item["owner"] not in VALID_OWNERS:
            errors.append(
                f"Item {item['id']}: invalid OWNER '{item['owner']}'. "
                f"Must be one of {VALID_OWNERS}"
            )
        if item["runtime_status"] not in VALID_RUNTIME_STATUSES:
            errors.append(
                f"Item {item['id']}: invalid PROJECT_RUNTIME_STATUS '{item['runtime_status']}'. "
                f"Must be one of {VALID_RUNTIME_STATUSES}"
            )

    # Compute totals
    type_counts = Counter(item["type"] for item in items)
    remediation_counts = Counter(item["remediation_class"] for item in items)
    owner_counts = Counter(item["owner"] for item in items)
    runtime_counts = Counter(item["runtime_status"] for item in items)

    # Check invariants
    type_sum = sum(type_counts.values())
    remediation_sum = sum(remediation_counts.values())
    owner_sum = sum(owner_counts.values())
    runtime_sum = sum(runtime_counts.values())

    if type_sum != EXPECTED_ITEM_COUNT:
        errors.append(f"TYPE totals sum to {type_sum}, expected {EXPECTED_ITEM_COUNT}")
    if remediation_sum != EXPECTED_ITEM_COUNT:
        errors.append(f"REMEDIATION_CLASS totals sum to {remediation_sum}, expected {EXPECTED_ITEM_COUNT}")
    if owner_sum != EXPECTED_ITEM_COUNT:
        errors.append(f"OWNER totals sum to {owner_sum}, expected {EXPECTED_ITEM_COUNT}")
    if runtime_sum != EXPECTED_ITEM_COUNT:
        errors.append(f"RUNTIME_STATUS totals sum to {runtime_sum}, expected {EXPECTED_ITEM_COUNT}")

    # Check OWNER_HANDOFF consistency: items with OWNER=ICTSI should have OWNER_HANDOFF
    for item in items:
        if "ICTSI" in item["owner"] and item["remediation_class"] != "OWNER_HANDOFF":
            errors.append(
                f"Item {item['id']}: OWNER is '{item['owner']}' but REMEDIATION_CLASS is "
                f"'{item['remediation_class']}'. Former-employer items must be OWNER_HANDOFF."
            )

    # Print results
    print("=" * 60)
    print("CREDENTIAL ROTATION MATRIX VALIDATOR")
    print("=" * 60)
    print()

    print(f"Total items: {len(items)}")
    print()

    print("--- TYPE Totals ---")
    for t in sorted(VALID_TYPES):
        print(f"  {t}: {type_counts.get(t, 0)}")
    print(f"  SUM: {type_sum}")
    print()

    print("--- REMEDIATION_CLASS Totals ---")
    for r in sorted(VALID_REMEDIATION_CLASSES):
        print(f"  {r}: {remediation_counts.get(r, 0)}")
    print(f"  SUM: {remediation_sum}")
    print()

    print("--- OWNER Totals ---")
    for o in sorted(VALID_OWNERS):
        print(f"  {o}: {owner_counts.get(o, 0)}")
    print(f"  SUM: {owner_sum}")
    print()

    print("--- RUNTIME_STATUS Totals ---")
    for s in sorted(VALID_RUNTIME_STATUSES):
        print(f"  {s}: {runtime_counts.get(s, 0)}")
    print(f"  SUM: {runtime_sum}")
    print()

    # ACTIVE_PRODUCTION by subtype
    active_items = [item for item in items if item["runtime_status"] == "ACTIVE_PRODUCTION"]
    active_type_counts = Counter(item["type"] for item in active_items)
    print("--- ACTIVE_PRODUCTION by TYPE ---")
    for t in sorted(VALID_TYPES):
        print(f"  {t}: {active_type_counts.get(t, 0)}")
    print(f"  ACTIVE_PRODUCTION_TOTAL: {len(active_items)}")
    print()

    # INACTIVE by subtype
    inactive_items = [item for item in items if item["runtime_status"] == "INACTIVE"]
    print(f"  INACTIVE_TOTAL: {len(inactive_items)}")

    # ARCHIVED_IN_PRACTICE by subtype
    archived_items = [item for item in items if item["runtime_status"] == "ARCHIVED_IN_PRACTICE"]
    print(f"  ARCHIVED_IN_PRACTICE_TOTAL: {len(archived_items)}")
    print()

    # Cross-check: ACTIVE + INACTIVE + ARCHIVED = 41
    cross_sum = len(active_items) + len(inactive_items) + len(archived_items)
    print(f"  Cross-check: {len(active_items)} + {len(inactive_items)} + {len(archived_items)} = {cross_sum}")
    if cross_sum != EXPECTED_ITEM_COUNT:
        errors.append(f"Runtime cross-check failed: {cross_sum} != {EXPECTED_ITEM_COUNT}")
    print()

    if errors:
        print("=" * 60)
        print("VALIDATION ERRORS:")
        print("=" * 60)
        for e in errors:
            print(f"  ❌ {e}")
        print()
        print(f"FAILED: {len(errors)} error(s)")
        return False
    else:
        print("=" * 60)
        print("ALL VALIDATIONS PASSED ✓")
        print("=" * 60)
        return True


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    matrix_path = script_dir / "CREDENTIAL_ROTATION_MATRIX.md"
    if not matrix_path.exists():
        print(f"ERROR: {matrix_path} not found")
        sys.exit(1)
    items = parse_matrix(str(matrix_path))
    success = validate(items)
    sys.exit(0 if success else 1)
