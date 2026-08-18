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

## Repository 7: API_Analyze

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/API_Analyze |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.14 Batch 3) |
| FORK_COUNT | 1 (kabann-1978/API_Analyze-B3 — NOT modified, may retain old secrets) |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #1 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (points to old SHA `c58e8c906e3d315c54b2bb7227f60279de681467`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (API key values not reachable from main or security/remove-api-keys-from-env-example) |
| GLOBAL_ERASURE | NOT_YET_PROVEN (fork risk + stale PR ref) |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `e521658aa32c2fa568e6190a08ac26a6013315af` | `6b3beb4e2624ad9e2bc66c1836d1a4d9aa5a44e0` | refs/heads/main |
| `c58e8c906e3d315c54b2bb7227f60279de681467` | `8e18ba6d5b921d6a8b1d130bdc4167524d1be3d0` | refs/heads/security/remove-api-keys-from-env-example |
| `c58e8c906e3d315c54b2bb7227f60279de681467` | `8e18ba6d5b921d6a8b1d130bdc4167524d1be3d0` | refs/pull/1/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR ref

The old commits reachable through `refs/pull/1/head` still contain the real News API key and Alpha Vantage API key values that were redacted from `V2/backend/.env.example` history. No credential values are listed here. Additionally, fork `kabann-1978/API_Analyze-B3` may retain the old secret values in its history.

---

## Repository 8: Bot_IqOption

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/Bot_IqOption |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.14 Batch 3) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 1 |
| AFFECTED_PR_NUMBERS | #5 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/5/head` (points to old SHA `d3a248eee8be3979a6b96b784393f0a3b629bc69`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (MP secret, JWT tokens, RSA key, and sensitive paths not reachable from main or any of 5 owner-managed branches) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `f26b29496dbb7e9c302d65252b1fdc0f956291a7` | `4b24fd33923ade683a8e6ba5dda59b356c42489d` | refs/heads/main |
| `d3a248eee8be3979a6b96b784393f0a3b629bc69` | `6d982ab47632d591bb7424810d25c94ad40c7eff` | refs/heads/security/remove-versioned-secrets |
| `d3a248eee8be3979a6b96b784393f0a3b629bc69` | `6d982ab47632d591bb7424810d25c94ad40c7eff` | refs/pull/5/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR ref

The old commits reachable through `refs/pull/5/head` still contain the removed sensitive files (`.env`, `RAILWAY_ENV_COMPLETE.txt`, `bot_iqoption.log` with 197 JWT session tokens, `keys/` directory, `db.sqlite3`, `venv/`, `bot-iq.pem` EC2 RSA private key) and the MERCADOPAGO_CLIENT_SECRET value that was redacted from history. No credential values are listed here.

---

## Repository 9: MVP-linkedin-bot

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/MVP-linkedin-bot |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.14 Batch 3) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 2 |
| AFFECTED_PR_NUMBERS | #1 (closed), #2 (merged) |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/1/head` (old SHA `8acdcc36980d27a4684d62d7b5ff81582588c333`) + `refs/pull/2/head` (old SHA `3e7bc0c573b5b663c6401433468a3bb28fb17596`) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (Chrome session tokens, LinkedIn session data, PII files, and sensitive directories not reachable from main, devin/fix branch, or security/remove-sensitive-artifacts) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `c2afbcd5e35867bd585ed89ac1641d8a6430bf02` | `749ef218395628e28139a49aeaa61dee270802f6` | refs/heads/main |
| `8acdcc36980d27a4684d62d7b5ff81582588c333` | `401fa5198797f33f9c0744b54b3acd6500b469e7` | refs/heads/devin/1781123382-fix-numeric-question-no-preposition |
| `3e7bc0c573b5b663c6401433468a3bb28fb17596` | `344fa37d5410f972f98ef1444c94038a79d3a92b` | refs/heads/security/remove-sensitive-artifacts |
| `8acdcc36980d27a4684d62d7b5ff81582588c333` | `401fa5198797f33f9c0744b54b3acd6500b469e7` | refs/pull/1/head (rewritten locally, NOT pushed) |
| `3e7bc0c573b5b663c6401433468a3bb28fb17596` | `344fa37d5410f972f98ef1444c94038a79d3a92b` | refs/pull/2/head (rewritten locally, NOT pushed) |

### Sensitive material still reachable via stale PR refs

The old commits reachable through `refs/pull/1/head` and `refs/pull/2/head` still contain the removed Chrome profile directories (with browser session tokens), LinkedIn session data in logs, PII files (cpf.pdf, CV PDFs, application history CSVs), and venv directories. No credential values, PII contents, or session data are listed here.

---

## Repository 10: ProFlow

### Support Eligibility Packet

| Field | Value |
|---|---|
| REPOSITORY | LeonardoRFragoso/ProFlow |
| UPSTREAM_REWRITE_STATUS | COMPLETED (Phase 2A.15) |
| FORK_COUNT | 0 |
| AFFECTED_PR_COUNT | 8 (PR #2-#9; PR #1 ref updated by branch force-push) |
| AFFECTED_PR_NUMBERS | #2, #3, #4, #5, #6, #7, #8, #9 |
| STALE_GITHUB_MANAGED_REFS | `refs/pull/2/head` (old SHA `aa54292f621c380bef28a33a4ddea8ee4a59740f`) + `refs/pull/3/head` (old SHA `5120cf583eae64ab889d0b5a55784d0e4b15c751`) + `refs/pull/4/head` (old SHA `418b0c447d231e0f67020acc486e0d45b8eb7fb6`) + `refs/pull/5/head` (old SHA `ad492fa21561ee2b3d3d3bfffeca2743512e494e`) + `refs/pull/6/head` (old SHA `40725110c1930e7277974276c8191c72def3cbee`) + `refs/pull/7/head` (old SHA `3609f70214bdbba0cac23b9ada575678882da11d`) + `refs/pull/8/head` (old SHA `6639fc3a9c52152923e1a0829440d6589b9e7a28`) + `refs/pull/9/head` (old SHA `acf483cf2f9c413a9b0d96137a03428865f92f27`) |
| PR_1_REF_STATUS | UPDATED — `refs/pull/1/head` now points to rewritten SHA `93a5fdd74a27c49af46cf68996d405eb332c73a7` (matches rewritten `copilot/eldest-turtle` branch) |
| LFS_ORPHANED | NO |
| CURRENT_OWNER_BRANCH_SCAN | PASS (all 4 gitleaks secrets + MP access token not reachable from main or any of 9 owner-managed branches) |
| GLOBAL_ERASURE | NOT_YET_PROVEN |
| SUPPORT_REQUEST_REQUIRED | YES |

### Ref Map (from git-filter-repo)

| Old SHA | New SHA | Ref |
|---|---|---|
| `390ea2b6ef2e44c0e548b4f4e4b60bee303b1a08` | `514aed8a38a3744d29860631400b707e1d0bb672` | refs/heads/main |
| `4d7a463af94e36464cba10520479f3f0916ff325` | `93a5fdd74a27c49af46cf68996d405eb332c73a7` | refs/heads/copilot/eldest-turtle |
| `aa54292f621c380bef28a33a4ddea8ee4a59740f` | `4ebfc9d35670fb3da4de3cb530ac2719af25fb1c` | refs/heads/copilot/add-mercado-pago-subscription |
| `5120cf583eae64ab889d0b5a55784d0e4b15c751` | `e80b4de6f22f1d5645f2d5da2e21edb64c042396` | refs/heads/codex/refactor-onboarding-flow-and-landing-page |
| `418b0c447d231e0f67020acc486e0d45b8eb7fb6` | `4c9a144dd24a04cfb2409d550bf2feb79effc61e` | refs/heads/codex/refactor-onboarding-flow-and-landing-page-r6pdkn |
| `ad492fa21561ee2b3d3d3bfffeca2743512e494e` | `0a9993e2a89c82b3a4d0367c57816ebd5c014861` | refs/heads/codex/refactor-onboarding-flow-and-landing-page-y61xd0 |
| `540e9c4459fb600da69dcce34cf2277f9c0874ae` | `631edd3cb4ce014fb940ba1465e8b2f2624cb69c` | refs/heads/cursor/fix-ai-enhance-validation |
| `acf483cf2f9c413a9b0d96137a03428865f92f27` | `977904b6ba645f7d3d7ea1e057042d1ade95a42e` | refs/heads/security/remove-residual-creds-from-docs |
| `6639fc3a9c52152923e1a0829440d6589b9e7a28` | `88db9fbf29c5527da7164ff27d7de4aa9ef772fe` | refs/heads/security/remove-versioned-secrets |

### Sensitive material still reachable via stale PR refs

The old commits reachable through `refs/pull/2-9/head` still contain the removed credential-bearing files (`RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md`, `MP_PRODUCTION_VALIDATION.md`) with the 4 real gitleaks secrets (Google OAuth secret, OpenAI API key, Django SECRET_KEY, MP webhook secret) and the MP access token (`APP_USR-<REDACTED_MP_TOKEN>-...`). PR #1's ref was updated by the branch force-push and is clean. No credential values are listed here.

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
| API_Analyze | YES | 1 (kabann-1978/API_Analyze-B3) | 1 (#1) | NO | PASS | NOT_YET_PROVEN (fork risk) | YES |
| Bot_IqOption | YES | 0 | 1 (#5) | NO | PASS | NOT_YET_PROVEN | YES |
| MVP-linkedin-bot | YES | 0 | 2 (#1 closed, #2 merged) | NO | PASS | NOT_YET_PROVEN | YES |
| ProFlow | YES | 0 | 8 (#2-#9; PR #1 ref updated) | NO | PASS | NOT_YET_PROVEN | YES |

### Post-Submission Tracking

| Repository | Support Request Status | Date Submitted | Ticket Number | Resolution Date |
|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | PENDING_OWNER_SUBMISSION | — | — | — |
| AndaimesPini_Project | PENDING_OWNER_SUBMISSION | — | — | — |
| FinanceControl | PENDING_OWNER_SUBMISSION | — | — | — |
| PayFlow-AI | PENDING_OWNER_SUBMISSION | — | — | — |
| LogiFlow | PENDING_OWNER_SUBMISSION | — | — | — |
| base-corporativa | PENDING_OWNER_SUBMISSION | — | — | — |
| API_Analyze | PENDING_OWNER_SUBMISSION | — | — | — |
| Bot_IqOption | PENDING_OWNER_SUBMISSION | — | — | — |
| MVP-linkedin-bot | PENDING_OWNER_SUBMISSION | — | — | — |
| ProFlow | PENDING_OWNER_SUBMISSION | — | — | — |

> **Note:** After GitHub Support confirms cleanup, update this table and change `GITHUB_SUPPORT_REQUEST` from `PENDING_OWNER_SUBMISSION` to `COMPLETED` in the central documentation. At that point, `GLOBAL_ERASURE` may be upgraded to `PROVEN` if GitHub confirms all stale objects have been garbage-collected.
