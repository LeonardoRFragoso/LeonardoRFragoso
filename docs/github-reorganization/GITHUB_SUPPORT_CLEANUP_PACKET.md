# GitHub Support Cleanup Packet — Phase 2A.12.1

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Phase:** 2A.12.1 — Stale Sensitive PR Ref Cleanup Packet
**Status:** PENDING_OWNER_SUBMISSION — Leonardo will submit manually

> **CRITICAL:** This document contains GitHub Support request drafts for removing stale GitHub-managed pull-request refs that still expose pre-rewrite commits. No PII, credential values, or database contents are included. No support request has been submitted automatically.

---

## Background

Phase 2A.12 Batch 1 executed git-filter-repo history rewrites on two repositories:

1. **LeonardoRFragoso/Portfolio-LeonardoFragoso-React** — removed PII PDFs from all history
2. **LeonardoRFragoso/AndaimesPini_Project** — removed SQLite database and backup files from all history

Both rewrites were force-pushed successfully. Owner-managed branches (main, security/*) no longer reference sensitive data. However, GitHub-managed `refs/pull/1/head` refs still point to pre-rewrite commits, making old sensitive objects reachable through the GitHub API and PR ref fetch.

GitHub Support is requested to dereference/remove these stale PR refs and run server-side garbage collection.

---

## Repository 1: Portfolio-LeonardoFragoso-React

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/Portfolio-LeonardoFragoso-React |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.12 Batch 1) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| FIRST_CHANGED_COMMITS | `4c5231ffb689c0e6eaa5176f3d5546fd74413657` → `6f4edf77295596b5d9069a128089cc6dd8c8fac0` |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `1b9da04ec0909b4274503224c90388bd06ea42c0`) |
| LFS_ORPHANED | NO (no LFS configured) |
| CURRENT_OWNER_BRANCH_SCAN | PASS (no sensitive paths reachable from main or security/remove-sensitive-pdfs) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `4d9fc8880cad0b69b6e35eaf59b54a1be6d869d3` | `2a067f9a058d5941274779b036f811e4202b2c57` | refs/heads/main |
| `1b9da04ec0909b4274503224c90388bd06ea42c0` | `e3bd8e3e0e77db814e632696f422a5126307bebd` | refs/heads/security/remove-sensitive-pdfs |
| `1b9da04ec0909b4274503224c90388bd06ea42c0` | `e3bd8e3e0e77db814e632696f422a5126307bebd` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Changed Refs (from git-filter-repo)

```
refs/heads/main
refs/heads/security/remove-sensitive-pdfs
refs/pull/1/head
```

### Suboptimal Issues

None — "No filtering problems encountered."

### Support Request Draft

```
Subject: Request to remove stale PR refs exposing pre-rewrite history — LeonardoRFragoso/Portfolio-LeonardoFragoso-React

Hello GitHub Support,

I am the owner of the repository LeonardoRFragoso/Portfolio-LeonardoFragoso-React.

I recently used git-filter-repo to remove sensitive personal identification documents (PII PDFs) from the entire git history of this repository. The rewritten history was force-pushed successfully to all owner-managed branches.

Current state:
- Repository: LeonardoRFragoso/Portfolio-LeonardoFragoso-React
- Rewritten main branch SHA: 2a067f9a058d5941274779b036f811e4202b2c57
- Owner-managed branches (main, security/remove-sensitive-pdfs) no longer reference the sensitive data
- Fork count: 0 (no forks exist)
- No Git LFS objects were involved

However, stale GitHub-managed pull-request refs still expose pre-rewrite commits:
- Affected PR count: 1
- Affected PR number: #1 (state: MERGED)
- refs/pull/1/head still points to old pre-rewrite SHA: 1b9da04ec0909b4274503224c90388bd06ea42c0
- First changed commit: 4c5231ffb689c0e6eaa5176f3d5546fd74413657 (old) → 6f4edf77295596b5d9069a128089cc6dd8c8fac0 (new)

The old commits reachable through refs/pull/1/head still contain the sensitive PII documents that were removed during the history rewrite.

I respectfully request that GitHub Support:
1. Remove or dereference the stale refs/pull/1/head ref
2. Clear any cached views associated with PR #1 that expose pre-rewrite commits
3. Run server-side garbage collection to permanently remove the unreachable objects containing sensitive data

Thank you for your assistance.

Best regards,
Leonardo Fragoso
```

---

## Repository 2: AndaimesPini_Project

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/AndaimesPini_Project |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.12 Batch 1) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| FIRST_CHANGED_COMMITS | `a1e5134faee2875dfa2a45482ad48e2e9cfe80a6` → `e760a681bc2d8e313c3d4408863908afb6089178` |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `b66dd80bb61dbe1f7ab462e903c2613008397abd`) |
| LFS_ORPHANED | NO (no LFS configured) |
| CURRENT_OWNER_BRANCH_SCAN | PASS (no sensitive paths reachable from main or security/remove-sensitive-artifacts) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `23c1a53d67378754ae6acb0e39753549f812f6e9` | `be192a64116359a11e4619ae78a94686a0b7be41` | refs/heads/main |
| `b66dd80bb61dbe1f7ab462e903c2613008397abd` | `d5368e196c358c6796be50cf7445a35f8c3596d0` | refs/heads/security/remove-sensitive-artifacts |
| `b66dd80bb61dbe1f7ab462e903c2613008397abd` | `d5368e196c358c6796be50cf7445a35f8c3596d0` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Changed Refs (from git-filter-repo)

```
refs/heads/main
refs/heads/security/remove-sensitive-artifacts
refs/pull/1/head
```

### Suboptimal Issues

None — "No filtering problems encountered."

### Support Request Draft

```
Subject: Request to remove stale PR refs exposing pre-rewrite history — LeonardoRFragoso/AndaimesPini_Project

Hello GitHub Support,

I am the owner of the repository LeonardoRFragoso/AndaimesPini_Project.

I recently used git-filter-repo to remove sensitive client/business data (SQLite database files and database backup files) from the entire git history of this repository. The rewritten history was force-pushed successfully to all owner-managed branches.

Current state:
- Repository: LeonardoRFragoso/AndaimesPini_Project
- Rewritten main branch SHA: be192a64116359a11e4619ae78a94686a0b7be41
- Owner-managed branches (main, security/remove-sensitive-artifacts) no longer reference the sensitive data
- Fork count: 0 (no forks exist)
- No Git LFS objects were involved

However, stale GitHub-managed pull-request refs still expose pre-rewrite commits:
- Affected PR count: 1
- Affected PR number: #1 (state: MERGED)
- refs/pull/1/head still points to old pre-rewrite SHA: b66dd80bb61dbe1f7ab462e903c2613008397abd
- First changed commit: a1e5134faee2875dfa2a45482ad48e2e9cfe80a6 (old) → e760a681bc2d8e313c3d4408863908afb6089178 (new)

The old commits reachable through refs/pull/1/head still contain the sensitive client/business database files that were removed during the history rewrite.

I respectfully request that GitHub Support:
1. Remove or dereference the stale refs/pull/1/head ref
2. Clear any cached views associated with PR #1 that expose pre-rewrite commits
3. Run server-side garbage collection to permanently remove the unreachable objects containing sensitive data

Thank you for your assistance.

Best regards,
Leonardo Fragoso
```

---

## Summary

| Repository | Upstream Sanitized | Forks | Affected PRs | LFS | Owner Branch Scan | Global Erasure | Support Required |
|---|---|---|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |
| AndaimesPini_Project | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |

### Post-Submission Tracking

| Repository | Support Request Status | Date Submitted | Ticket Number | Resolution Date |
|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | PENDING_OWNER_SUBMISSION | — | — | — |
| AndaimesPini_Project | PENDING_OWNER_SUBMISSION | — | — | — |

> **Note:** After GitHub Support confirms cleanup, update this table and change `GITHUB_SUPPORT_REQUEST` from `PENDING_OWNER_SUBMISSION` to `COMPLETED` in the central documentation. At that point, `GLOBAL_ERASURE` may be upgraded to `PROVEN` if GitHub confirms all stale objects have been garbage-collected.
