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

## Repository 3: FinanceControl

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/FinanceControl |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.13 Batch 2) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `88647876cd2a9bdfa9f097950a11ec767735c020`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (sensitive paths not reachable from main or security/remove-sensitive-artifacts) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `feb1ffdc97ef3971193248ee9b61dc1d8dbcd031` | `3a1c40d5881acd046e3ba1551dd66d9084ada37a` | refs/heads/main |
| `88647876cd2a9bdfa9f097950a11ec767735c020` | `be47e830c6a92297727e4239e701180c0187afce` | refs/heads/security/remove-sensitive-artifacts |
| `88647876cd2a9bdfa9f097950a11ec767735c020` | `be47e830c6a92297727e4239e701180c0187afce` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR ref

The old commits reachable through `refs/pull/1/head` still contain the removed sensitive files: EC2 RSA private key (`chave-EC2/Finance2.pem`, `backend/chave-EC2/Finance2.pem`), SQLite databases (`backend/db.sqlite3`, `backend/backend/db.sqlite3`), and a payment receipt PDF. No credential values are listed here.

---

## Repository 4: PayFlow-AI

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/PayFlow-AI |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.13 Batch 2) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `3f16cbe9d291348c9a7e3c7401bbf2af24d10052`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (Twilio auth token values not reachable from main or security/remove-exposed-token) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `afdcb7b58b187c146e15848659192205c08a882b` | `003291b613b85ad90fb005810d5290aa79ed69ac` | refs/heads/main |
| `3f16cbe9d291348c9a7e3c7401bbf2af24d10052` | `f115494bac71d6e1e48e167f593636b1ad38e4b2` | refs/heads/security/remove-exposed-token |
| `3f16cbe9d291348c9a7e3c7401bbf2af24d10052` | `f115494bac71d6e1e48e167f593636b1ad38e4b2` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR ref

The old commits reachable through `refs/pull/1/head` still contain two real Twilio auth token values (32-hex) that were redacted from `Docs/CORRIGIR_TOKEN.txt` history. No token values are listed here.

---

## Repository 5: LogiFlow

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/LogiFlow |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.13 Batch 2) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `44933eb53b0d66ec89d5d96bec70e0547473d165`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (real Evolution API key not reachable from main or security/remove-evolution-api-key-from-docs) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `90df4b0b727c37e9840f7002d394080f63086e08` | `b82451f612d7043367e3789489a36073dff4531c` | refs/heads/main |
| `44933eb53b0d66ec89d5d96bec70e0547473d165` | `015acbff9e2552b4b25c4607abaa88cd8ee99c4e` | refs/heads/security/remove-evolution-api-key-from-docs |
| `44933eb53b0d66ec89d5d96bec70e0547473d165` | `015acbff9e2552b4b25c4607abaa88cd8ee99c4e` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR ref

The old commits reachable through `refs/pull/1/head` still contain the real Evolution API key value that was redacted from 7 historical documentation/configuration files. No credential values are listed here.

---

## Repository 6: base-corporativa

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/base-corporativa |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.13 Batch 2) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `e1655bb3166fa120ecaffa8e8f35dfaf33b717ca`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (R2 keys, SendGrid key, and env files not reachable from main, feature/pagae-payment-method, or security/remove-versioned-secrets) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `e40c90fe5e98609509ad6cf0d00406a3f92bbe60` | `33f7d1999cfd56fc2a09f362ea859ec074b064e7` | refs/heads/main |
| `9497561eb702b7f131215809e225dda34afc71c2` | `9edf2ea2f8b9dedc9d0e7048fd6f27e7eb2340f0` | refs/heads/feature/pagae-payment-method |
| `e1655bb3166fa120ecaffa8e8f35dfaf33b717ca` | `eb0b26c6b2bbdb670226bb45d8bfe599c4d574eb` | refs/heads/security/remove-versioned-secrets |
| `e1655bb3166fa120ecaffa8e8f35dfaf33b717ca` | `eb0b26c6b2bbdb670226bb45d8bfe599c4d574eb` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR ref

The old commits reachable through `refs/pull/1/head` still contain the removed environment files (`RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway`, `backend/.env`) and the hardcoded R2 access key, R2 secret key, and SendGrid API key values that were redacted from history. No credential values are listed here.

---

## Summary

| Repository | Upstream Sanitized | Forks | Affected PRs | LFS | Owner Branch Scan | Global Erasure | Support Required |
|---|---|---|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |
| AndaimesPini_Project | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |
| FinanceControl | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |
| PayFlow-AI | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |
| LogiFlow | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |
| base-corporativa | YES | 0 | 1 (#1) | NO | PASS | NOT_YET_PROVEN | YES |

### Post-Submission Tracking

| Repository | Support Request Status | Date Submitted | Ticket Number | Resolution Date |
|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | PENDING_OWNER_SUBMISSION | — | — | — |
| AndaimesPini_Project | PENDING_OWNER_SUBMISSION | — | — | — |
| FinanceControl | PENDING_OWNER_SUBMISSION | — | — | — |
| PayFlow-AI | PENDING_OWNER_SUBMISSION | — | — | — |
| LogiFlow | PENDING_OWNER_SUBMISSION | — | — | — |
| base-corporativa | PENDING_OWNER_SUBMISSION | — | — | — |

> **Note:** After GitHub Support confirms cleanup, update this table and change `GITHUB_SUPPORT_REQUEST` from `PENDING_OWNER_SUBMISSION` to `COMPLETED` in the central documentation. At that point, `GLOBAL_ERASURE` may be upgraded to `PROVEN` if GitHub confirms all stale objects have been garbage-collected.
