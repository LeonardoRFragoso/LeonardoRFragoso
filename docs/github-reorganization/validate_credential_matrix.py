#!/usr/bin/env python3
"""
Credential Rotation Matrix Validator

Parses the Updated Summary Table in CREDENTIAL_ROTATION_MATRIX.md and
validates that:
- Exactly 41 unique items exist (IDs 1..41)
- No duplicate IDs
- Each item has exactly one TYPE from: CREDENTIAL, SESSION, LOCAL_APP_SECRET, PII
- Each item has exactly one REMEDIATION_CLASS from the allowed set
- Each item has a valid OWNER (normalized)
- Each item has a valid PROJECT_RUNTIME_STATUS
- All totals sum to 41
- Typed "Updated Totals" tables in the markdown agree with computed row totals
- OWNER_HANDOFF consistency: ICTSI-owned items must have OWNER_HANDOFF

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

VALID_TYPES = ["CREDENTIAL", "SESSION", "LOCAL_APP_SECRET", "PII"]
VALID_REMEDIATION_CLASSES = [
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
]
VALID_RUNTIME_STATUSES = [
    "ACTIVE_PRODUCTION",
    "ACTIVE_DEVELOPMENT",
    "INACTIVE",
    "ARCHIVED_IN_PRACTICE",
]

# Owner alias normalization — all shorthand forms map to canonical values
OWNER_ALIASES = {
    "ICTSI": "ICTSI/iTracker",
    "iTracker": "ICTSI/iTracker",
    "ICTSI/iTracker": "ICTSI/iTracker",
    "Leonardo": "Leonardo",
    "UNKNOWN": "UNKNOWN",
}
CANONICAL_OWNERS = ["Leonardo", "ICTSI/iTracker", "UNKNOWN"]

EXPECTED_ITEM_COUNT = 41
EXPECTED_COLUMN_COUNT = 10  # #, Repo, Provider, Type_desc, TYPE, RUNTIME, REMEDIATION, OWNER, ACTIVE_DEPLOY, NEXT_ACTION


def normalize_owner(raw: str) -> str:
    """Normalize owner string to canonical form."""
    return OWNER_ALIASES.get(raw, raw)


def parse_matrix(filepath: str) -> list[dict]:
    """Parse the markdown table and return list of item dicts.

    Uses robust parsing that preserves empty cells between separators.
    Fails on malformed rows rather than silently skipping them.
    """
    content = Path(filepath).read_text()
    lines = content.split("\n")
    items = []
    in_table = False
    line_num = 0

    for i, line in enumerate(lines):
        line_num = i + 1
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

            # Robust parsing: split on | and take inner cells (drop leading/trailing empty)
            raw_cells = line.split("|")
            # raw_cells[0] is empty (before first |), raw_cells[-1] is empty (after last |)
            cells = [c.strip() for c in raw_cells[1:-1]]

            # Validate exact column count
            if len(cells) != EXPECTED_COLUMN_COUNT:
                raise ValueError(
                    f"Line {line_num}: expected {EXPECTED_COLUMN_COUNT} columns, "
                    f"got {len(cells)}. Row content: {line[:80]}..."
                )

            # Parse ID — must be an integer
            try:
                item_id = int(cells[0])
            except ValueError:
                raise ValueError(
                    f"Line {line_num}: first column is not an integer: '{cells[0]}'"
                )

            items.append({
                "id": item_id,
                "repo": cells[1],
                "provider": cells[2],
                "type_desc": cells[3],
                "type": cells[4],
                "runtime_status": cells[5],
                "remediation_class": cells[6],
                "owner_raw": cells[7],
                "owner": normalize_owner(cells[7]),
                "active_deployment": cells[8],
                "next_action": cells[9],
            })

    return items


def parse_typed_totals(filepath: str) -> dict[str, dict[str, int]]:
    """Parse the 'Updated Totals' tables from the markdown to get hand-typed totals.

    Returns dict with keys 'type', 'remediation', 'runtime', 'owner',
    each mapping to a dict of {label: count}.
    """
    content = Path(filepath).read_text()
    lines = content.split("\n")
    typed = {"type": {}, "remediation": {}, "runtime": {}, "owner": {}}
    current_section = None

    for line in lines:
        # Detect section headers (check all, not elif, since headers can follow each other)
        if "#### By Type (sum" in line:
            current_section = "type"
            continue
        elif "#### By Remediation Class (sum" in line:
            current_section = "remediation"
            continue
        elif "#### By Project Runtime Status (sum" in line:
            current_section = "runtime"
            continue
        elif "#### By Owner (sum" in line:
            current_section = "owner"
            continue

        if current_section:
            # Stop parsing current section if we hit a new header
            if line.startswith("#"):
                current_section = None
                continue
            if line.startswith("|---|"):
                continue
            if not line.startswith("|"):
                # End of this table — keep current_section so next header can reset it
                continue
            raw_cells = line.split("|")
            cells = [c.strip() for c in raw_cells[1:-1]]
            # Only parse tables with exactly 2 columns (label + count) to avoid
            # picking up reconciliation tables with different structures
            if len(cells) == 2 and cells[0] not in ("Type", "Remediation Class", "Runtime Status", "Owner", "**Total**"):
                try:
                    count = int(cells[1])
                    typed[current_section][cells[0]] = count
                except ValueError:
                    pass

    return typed


def validate(items: list[dict], typed_totals: dict) -> bool:
    """Run all validations. Returns True if all pass."""
    errors = []

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
        if item["owner"] not in CANONICAL_OWNERS:
            errors.append(
                f"Item {item['id']}: invalid OWNER '{item['owner_raw']}' (normalized: '{item['owner']}'). "
                f"Must be one of {CANONICAL_OWNERS}"
            )
        if item["runtime_status"] not in VALID_RUNTIME_STATUSES:
            errors.append(
                f"Item {item['id']}: invalid PROJECT_RUNTIME_STATUS '{item['runtime_status']}'. "
                f"Must be one of {VALID_RUNTIME_STATUSES}"
            )

    # Check OWNER_HANDOFF consistency: items with OWNER=ICTSI/iTracker must have OWNER_HANDOFF
    for item in items:
        if item["owner"] == "ICTSI/iTracker" and item["remediation_class"] != "OWNER_HANDOFF":
            errors.append(
                f"Item {item['id']}: OWNER is '{item['owner']}' but REMEDIATION_CLASS is "
                f"'{item['remediation_class']}'. Former-employer items must be OWNER_HANDOFF."
            )

    # Compute totals from row data
    type_counts = Counter(item["type"] for item in items)
    remediation_counts = Counter(item["remediation_class"] for item in items)
    owner_counts = Counter(item["owner"] for item in items)
    runtime_counts = Counter(item["runtime_status"] for item in items)

    # Check invariants — all sums must equal EXPECTED_ITEM_COUNT
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

    # Cross-check: sum of all runtime status categories = 41 (dynamic, not hardcoded)
    if runtime_sum != EXPECTED_ITEM_COUNT:
        errors.append(
            f"Runtime cross-check failed: dynamic sum {runtime_sum} != {EXPECTED_ITEM_COUNT}"
        )

    # Validate typed totals match computed totals
    for section, computed in [("type", type_counts), ("remediation", remediation_counts),
                               ("runtime", runtime_counts), ("owner", owner_counts)]:
        typed = typed_totals.get(section, {})
        for label, typed_count in typed.items():
            # Normalize owner labels in typed totals too
            normalized_label = normalize_owner(label) if section == "owner" else label
            computed_count = computed.get(normalized_label, computed.get(label, 0))
            if typed_count != computed_count:
                errors.append(
                    f"Typed total mismatch in '{section}' section: "
                    f"'{label}' typed as {typed_count} but computed from rows as {computed_count}"
                )

    # Print results
    print("=" * 60)
    print("CREDENTIAL ROTATION MATRIX VALIDATOR")
    print("=" * 60)
    print()

    print(f"Total items: {len(items)}")
    print()

    print("--- TYPE Totals ---")
    for t in VALID_TYPES:
        print(f"  {t}: {type_counts.get(t, 0)}")
    print(f"  SUM: {type_sum}")
    print()

    print("--- REMEDIATION_CLASS Totals ---")
    for r in VALID_REMEDIATION_CLASSES:
        print(f"  {r}: {remediation_counts.get(r, 0)}")
    print(f"  SUM: {remediation_sum}")
    print()

    print("--- OWNER Totals (normalized) ---")
    for o in CANONICAL_OWNERS:
        print(f"  {o}: {owner_counts.get(o, 0)}")
    print(f"  SUM: {owner_sum}")
    print()

    print("--- RUNTIME_STATUS Totals ---")
    for s in VALID_RUNTIME_STATUSES:
        print(f"  {s}: {runtime_counts.get(s, 0)}")
    print(f"  SUM: {runtime_sum}")
    print()

    # ACTIVE_PRODUCTION by subtype
    active_items = [item for item in items if item["runtime_status"] == "ACTIVE_PRODUCTION"]
    active_type_counts = Counter(item["type"] for item in active_items)
    print("--- ACTIVE_PRODUCTION by TYPE ---")
    for t in VALID_TYPES:
        print(f"  {t}: {active_type_counts.get(t, 0)}")
    print(f"  ACTIVE_PRODUCTION_TOTAL: {len(active_items)}")
    print()

    # All runtime status totals
    for status in VALID_RUNTIME_STATUSES:
        status_items = [item for item in items if item["runtime_status"] == status]
        print(f"  {status}_TOTAL: {len(status_items)}")
    print()

    # Dynamic cross-check
    print(f"  Dynamic cross-check: sum of all runtime categories = {runtime_sum}")
    if runtime_sum == EXPECTED_ITEM_COUNT:
        print(f"  ✓ Matches expected {EXPECTED_ITEM_COUNT}")
    else:
        print(f"  ✗ MISMATCH: {runtime_sum} != {EXPECTED_ITEM_COUNT}")
    print()

    # Typed totals consistency check
    print("--- Typed Totals Consistency Check ---")
    typed_ok = True
    for section, computed in [("type", type_counts), ("remediation", remediation_counts),
                               ("runtime", runtime_counts), ("owner", owner_counts)]:
        typed = typed_totals.get(section, {})
        for label, typed_count in typed.items():
            normalized_label = normalize_owner(label) if section == "owner" else label
            computed_count = computed.get(normalized_label, computed.get(label, 0))
            status = "✓" if typed_count == computed_count else "✗"
            if typed_count != computed_count:
                typed_ok = False
            print(f"  {status} {section}.{label}: typed={typed_count}, computed={computed_count}")
    print()

    # Phase 2A.9: PRIMARY_READINESS_COUNTS invariant — sum must equal 41
    readiness_sum = 0
    in_readiness_table = False
    matrix_content = Path(__file__).parent.joinpath("CREDENTIAL_ROTATION_MATRIX.md").read_text()
    for line in matrix_content.split("\n"):
        stripped = line.strip()
        # Look for the totals table header (2-column: "Primary Readiness State" | "Count")
        if stripped == "| Primary Readiness State | Count |":
            in_readiness_table = True
            continue
        if in_readiness_table:
            if stripped.startswith("|---|"):
                continue
            if not stripped.startswith("|"):
                break
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) == 2 and cells[0] not in ("Primary Readiness State", "**Total**"):
                try:
                    count = int(cells[1])
                    readiness_sum += count
                except ValueError:
                    pass
    print("--- Primary Readiness Counts Invariant ---")
    if readiness_sum == EXPECTED_ITEM_COUNT:
        print(f"  ✓ SUM(PRIMARY_READINESS_COUNTS) = {readiness_sum} == {EXPECTED_ITEM_COUNT}")
    else:
        print(f"  ✗ SUM(PRIMARY_READINESS_COUNTS) = {readiness_sum} != {EXPECTED_ITEM_COUNT}")
        errors.append(
            f"PRIMARY_READINESS_COUNTS invariant failed: sum is {readiness_sum}, "
            f"expected {EXPECTED_ITEM_COUNT}"
        )
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
    try:
        items = parse_matrix(str(matrix_path))
    except ValueError as e:
        print(f"PARSE ERROR: {e}")
        sys.exit(1)
    typed_totals = parse_typed_totals(str(matrix_path))
    success = validate(items, typed_totals)
    sys.exit(0 if success else 1)
