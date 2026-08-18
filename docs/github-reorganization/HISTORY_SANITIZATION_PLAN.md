# Git History Sanitization Plan — Phase 2A (Canonicalized Phase 2A.10.1, updated Phase 2A.11)

**Account:** LeonardoRFragoso
**Phase 2A date:** 2026-08-17
**Phase 2A.7 update:** 2026-08-18
**Phase 2A.8 update:** 2026-08-18
**Phase 2A.9 update:** 2026-08-18
**Phase 2A.10 update:** 2026-08-18
**Phase 2A.10.1 update:** 2026-08-18 (history-sanitization plan canonicalization & pre-rewrite gate)
**Phase 2A.11 update:** 2026-08-18 (runtime gate closure, cleanup PR integration, pre-history-rewrite readiness)
**Status:** PLAN ONLY — **DO NOT EXECUTE without Leonardo's explicit per-repo authorization**

> **CRITICAL:** History rewriting is DESTRUCTIVE and irreversible. It rewrites all commit SHAs, breaks forks, breaks open PRs, and requires force-push. This document is a PLAN only. No history rewrite has been performed or will be performed without explicit authorization.

> **Phase 2A.10.1 scope:** This phase is DOCUMENTATION ONLY. It reconciles the history-sanitization plan after the Phase 2A.10 deletion batch. It does NOT delete repositories, rotate credentials, invalidate sessions, rewrite history, force-push, merge any PR, or start Phase 2B.

## Phase 2A.10.1 Update — History-Sanitization Plan Canonicalization

### Why this update exists

After Phase 2A.10, the history-sanitization plan contained stale contradictions: Bet-IA-BOT (deleted in Phase 2A.10) still appeared as an executable rewrite target in the detailed plan, the tier ordering, the summary table, and the rewrite total, even though its lifecycle header correctly stated `DELETED_BY_OWNER` / `NOT_APPLICABLE_REPOSITORY_DELETED`. In addition, three repositories with real credential material in history (PayFlow-AI, LogiFlow, API_Analyze) had current-tree cleanup merged in Phase 2A.9 but were never given detailed history-sanitization sections, and AndaimesPini_Project was present in the detailed plan but missing from the readiness table.

Phase 2A.10.1 corrects all of these by establishing ONE canonical history-rewrite repository set and ONE canonical rewrite table. The historical phase-update audit trail (2A.7 / 2A.8 / 2A.9 / 2A.10) is preserved verbatim below for traceability.

### Canonical history-rewrite repository set (12 active candidates)

Reconstructed from all security findings across Phases 1 through 2A.10 — NOT derived from the old numbered sections. Every candidate was verified against live GitHub metadata and audit evidence on 2026-08-18.

| # | Repository | Evidence source |
|---|---|---|
| 1 | ProFlow | Items #1-#7 (Django/OpenAI/Google OAuth/GitHub OAuth/Mercado Pago) — was PUBLIC |
| 2 | base-corporativa | Items #8-#17 (R2/Mercado Pago/Melhor Envio/PostgreSQL/Django superuser/SendGrid) — was PUBLIC |
| 3 | FinanceControl | Item #18 (AWS EC2 RSA private key) + PII (paycheck PDF, sqlite3) — was PUBLIC |
| 4 | Digital-Signage-Platform | Items #19-#20 (MySQL DB credentials, JWT secret) — was PUBLIC, ICTSI-owned |
| 5 | FlowTrack | Items #29-#30 (weak SECRET_KEY, 179 session/CSRF tokens) — was PUBLIC, ICTSI-owned |
| 6 | Bot_IqOption | Items #21-#27 (Mercado Pago/SECRET_KEY/user keys) + #26 (197 JWT session tokens) — was PRIVATE |
| 7 | MVP-linkedin-bot | Items #31-#33, #40-#41 (Chrome/LinkedIn sessions, Telegram token, LinkedIn password, CPF PII) — was PRIVATE |
| 8 | Portfolio-LeonardoFragoso-React | Items #35-#36 (CNPJ card PDF, articles of association PDF) — PII, is PUBLIC |
| 9 | AndaimesPini_Project | Client/business data in SQLite DB (not in credential matrix — data artifact) — was PUBLIC |
| 10 | PayFlow-AI | Item #28 (Twilio auth token) — real Twilio credential existed in history — was PUBLIC |
| 11 | LogiFlow | Item #37 (Evolution API key) — real Evolution API credential material committed before current-tree cleanup — was PUBLIC |
| 12 | API_Analyze | Items #38-#39 (News API key, Alpha Vantage key) — real keys previously committed — was PUBLIC |

**ACTIVE_REWRITE_CANDIDATES = 12.** Bet-IA-BOT is NOT in this set (see DELETED_REPOSITORY_AUDIT_RECORD below).

### Canonical Rewrite Table (Phase 2A.10.1)

One canonical table. Every non-deleted candidate occurs exactly once. Bet-IA-BOT occurs only in the deleted-repository audit record, not in the executable target count.

Allowed values:
- `REWRITE_REQUIRED`: YES | NO | N/A_REPOSITORY_DELETED
- `REWRITE_READY`: YES | NO | N/A

| REPOSITORY | VISIBILITY_NOW | PUBLIC_WHEN_EXPOSED | CURRENT_TREE | SENSITIVE_HISTORY_TYPE | OWNER | OWNER_ATTESTATION | SESSION_STATUS | OWNER_HANDOFF | RUNTIME_GATE | OPEN_PR_GATE | FORK_RISK | REWRITE_REQUIRED | REWRITE_READY | BLOCKER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ProFlow | PRIVATE | YES | CLEAN | CREDENTIALS (items 1-7) | Leonardo | PENDING | N/A | N/A | N/A | OPEN (PR #1, #2) | LOW (0 forks; was public) | YES | NO | OWNER_ATTESTATION_BLOCKER, OPEN_PR_GATE |
| base-corporativa | PRIVATE | YES | CLEAN (PR #1 merged Phase 2A.11) | CREDENTIALS (items 8-17) | Leonardo | PENDING | N/A | N/A | CLEARED (NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED) | NONE (PR #1 merged) | LOW (0 forks; was public) | YES | NO | OWNER_ATTESTATION_BLOCKER |
| FinanceControl | PRIVATE | YES | CLEAN | CREDENTIALS (item 18) + PII | Leonardo | PENDING | N/A | N/A | N/A | NONE | LOW (0 forks; was public) | YES | NO | OWNER_ATTESTATION_BLOCKER |
| Digital-Signage-Platform | PRIVATE | YES | CLEAN | CREDENTIALS (items 19-20) | ICTSI/iTracker | N/A | N/A | PENDING | N/A | OPEN (PR #4, head 1f96647) | LOW (0 forks; was public) | YES | NO | OWNER_HANDOFF_BLOCKER, OPEN_PR_GATE |
| FlowTrack | PRIVATE | YES | CLEAN | SESSIONS (item 30) + LOCAL_APP_SECRET (item 29) | ICTSI/iTracker | N/A | PENDING | PENDING | N/A | OPEN (PR #1, head bb1c040) | LOW (0 forks; was public) | YES | NO | OWNER_HANDOFF_BLOCKER, SESSION_BLOCKER, OPEN_PR_GATE |
| Bot_IqOption | PRIVATE | NO (always private) | CLEAN (PR #5 merged Phase 2A.11) | CREDENTIALS (items 21-25, 27) + SESSIONS (item 26) | Leonardo | PENDING | PENDING | N/A | CLEARED (NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED) | NONE (PR #5 merged) | NONE (private, 0 forks) | YES | NO | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER |
| MVP-linkedin-bot | PRIVATE | NO (always private) | CLEAN | SESSIONS (items 31, 32, 41) + CREDENTIAL (item 40) + PII (item 33) | Leonardo | PENDING | PENDING | N/A | N/A | OPEN (PR #1, head 8acdcc3) | NONE (private, 0 forks) | YES | NO | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER, OPEN_PR_GATE |
| Portfolio-LeonardoFragoso-React | PUBLIC | YES (is public) | CLEAN | PII (items 35-36) | Leonardo | N/A (PII) | N/A | N/A | N/A | NONE | LOW (0 forks; is public) | YES | YES | NONE — PII removal IS the remediation |
| AndaimesPini_Project | PRIVATE | YES | CLEAN | CLIENT_BUSINESS_DATA (SQLite DB; not in credential matrix) | Leonardo | N/A (data, not credentials) | N/A | N/A | N/A | NONE | LOW (0 forks; was public) | YES | YES | NONE — data artifact removal IS the remediation; PR #1 merged, current tree clean |
| PayFlow-AI | PUBLIC | YES (is public) | CLEAN | CREDENTIAL (item 28, Twilio auth token) | Leonardo | PENDING | N/A | N/A | N/A | NONE | LOW (0 forks; is public) | YES | NO | OWNER_ATTESTATION_BLOCKER |
| LogiFlow | PUBLIC | YES (is public) | CLEAN | CREDENTIAL (item 37, Evolution API key) | Leonardo | PENDING | N/A | N/A | N/A | NONE | LOW (0 forks; is public) | YES | NO | OWNER_ATTESTATION_BLOCKER |
| API_Analyze | PUBLIC | YES (is public) | CLEAN | CREDENTIALS (items 38-39, News API + Alpha Vantage keys) | Leonardo | PENDING | N/A | N/A | N/A | NONE | HIGH (1 fork: kabann-1978/API_Analyze-B3) | YES | NO | OWNER_ATTESTATION_BLOCKER, FORK_RISK |

### Readiness counts (computed from the canonical table — Phase 2A.11 updated)

| Metric | Value |
|---|---|
| ACTIVE_REWRITE_CANDIDATES | 12 |
| REWRITE_READY | 2 (Portfolio-LeonardoFragoso-React, AndaimesPini_Project) |
| REWRITE_BLOCKED | 10 |
| READY + BLOCKED | 12 (= ACTIVE_REWRITE_CANDIDATES) |
| DELETED_REWRITE_NA | 1 (Bet-IA-BOT — see audit record) |

### Blocker counts (repositories; a repo may carry multiple blockers — Phase 2A.11 updated)

| Blocker | Repositories | Count |
|---|---|---|
| OWNER_ATTESTATION_BLOCKER | ProFlow, base-corporativa, FinanceControl, Bot_IqOption, MVP-linkedin-bot, PayFlow-AI, LogiFlow, API_Analyze | 8 |
| SESSION_BLOCKER | Bot_IqOption, MVP-linkedin-bot, FlowTrack | 3 |
| OWNER_HANDOFF_BLOCKER | Digital-Signage-Platform, FlowTrack | 2 |
| CURRENT_TREE_BLOCKER | NONE (base-corporativa and Bot_IqOption cleared by PR merges Phase 2A.11) | 0 |
| RUNTIME_BLOCKER | NONE (base-corporativa and Bot_IqOption cleared by OWNER_ATTESTED_RUNTIME_STATE Phase 2A.11) | 0 |
| OPEN_PR_GATE | ProFlow, Digital-Signage-Platform, FlowTrack, MVP-linkedin-bot | 4 (base-corporativa and Bot_IqOption PRs merged) |
| FORK_RISK | API_Analyze | 1 |

> **OWNER_ATTESTATION remains PENDING for all credential-bearing repos.** Leonardo previously reported credentials were changed (OWNER_REPORTED). This has NOT been upgraded to OWNER_ATTESTED_COMPLETED. No provider dashboard access is required for OWNER_ATTESTED_COMPLETED, but explicit Leonardo attestation per item is mandatory (see Part G / POST_ROTATION_RECONCILIATION.md).

### Live PR gate reconciliation (Phase 2A.11 updated — base-corporativa #1 and Bot_IqOption #5 MERGED)

Force-pushing rewritten history can invalidate open PRs. Live PR state for every candidate:

| Repository | Open PRs | Head SHA | Mergeable | Gate impact |
|---|---|---|---|---|
| ProFlow | PR #1, PR #2 (copilot feature branches) | 4d7a463 / aa54292 | UNKNOWN | Close or merge before rewrite |
| base-corporativa | NONE (PR #1 MERGED Phase 2A.11, merge SHA e40c90f) | — | — | None — current tree CLEAN |
| FinanceControl | none | — | — | None |
| Digital-Signage-Platform | PR #4 (security/remove-versioned-secrets) | 1f9664713c681af83a92ad4647719ab070608a57 | MERGEABLE | OWNER_HANDOFF_BEFORE_MERGE — DO NOT merge |
| FlowTrack | PR #1 (security/remove-sensitive-artifacts) | bb1c040cf241607e6aa02b30cd67d9d87fc7725b | MERGEABLE | OWNER_HANDOFF_BEFORE_MERGE — DO NOT merge |
| Bot_IqOption | NONE (PR #5 MERGED Phase 2A.11, merge SHA f26b294) | — | — | None — current tree CLEAN |
| MVP-linkedin-bot | PR #1 (devin bot fix, NOT the merged security PR #2) | 8acdcc36980d27a4684d62d7b5ff81582588c333 | UNKNOWN | Close or merge before rewrite |
| Portfolio-LeonardoFragoso-React | none | — | — | None |
| AndaimesPini_Project | none (security PR #1 already merged) | — | — | None |
| PayFlow-AI | none (security PR #1 already merged) | — | — | None |
| LogiFlow | none (security PR #1 already merged) | — | — | None |
| API_Analyze | none (security PR #1 already merged) | — | — | None |

> **Phase 2A.11:** base-corporativa PR #1 and Bot_IqOption PR #5 were merged after Leonardo confirmed neither is deployed on Railway (OWNER_ATTESTED_RUNTIME_STATE). Both current trees are now CLEAN.

## DELETED_REPOSITORY_AUDIT_RECORD (Tombstone)

This section preserves the historical audit trail for repositories that participated in the canonical security audit but were deleted by owner. These repositories are NOT executable rewrite targets. They appear here only for traceability.

### Bet-IA-BOT — DELETED_BY_OWNER

| Field | Value |
|---|---|
| Canonical item | #34 (API-Football API key) |
| Remediation class | REVOKE_ONLY |
| OWNER_REPORTED | Yes — Leonardo reported the credential was changed |
| REPOSITORY_LIFECYCLE | DELETED_BY_OWNER (deleted in Phase 2A.10) |
| History sanitization | NOT_APPLICABLE_REPOSITORY_DELETED (GitHub repository no longer exists) |
| REWRITE_REQUIRED | N/A_REPOSITORY_DELETED |
| REWRITE_READY | N/A |
| Evidence state | OWNER_REPORTED (unchanged) |
| Key principle | **Repository deletion does NOT prove credential revocation.** The API-Football key (item #34) still requires explicit owner attestation of revocation. |

> Bet-IA-BOT must NOT appear as an executable rewrite target anywhere in this plan. It is excluded from ACTIVE_REWRITE_CANDIDATES, from the detailed per-repository sanitization sections, from the execution-order tiers, and from the rewrite total. The git-filter-repo instructions that previously appeared here have been removed because the repository no longer exists.

---

## Phase 2A.10 Update — Repository Deletion Batch (preserved)

13 repositories were deleted by owner (see `REPOSITORY_DISPOSITION.md`). One of these (Bet-IA-BOT) participated in the canonical security audit:

- **Bet-IA-BOT:** DELETED_BY_OWNER. History sanitization status changed to NOT_APPLICABLE_REPOSITORY_DELETED (GitHub repository no longer exists). Canonical item #34 (API-Football API key, REVOKE_ONLY) is preserved in the audit trail. Repository deletion does NOT prove credential revocation — the evidence state remains OWNER_REPORTED.

The remaining 11 repositories in the history sanitization plan are unchanged.

## Phase 2A.9 Update — Current-Tree Final Closure & Evidence Model Correction (preserved)

### Phase 2A.9 Cleanup Merges
- **ProFlow PR #9** (merge SHA: `390ea2b6`): Removed real MP credentials and user email PII from `MP_PRODUCTION_VALIDATION.md`
- **LogiFlow PR #1** (merge SHA: `90df4b0b`): Removed Evolution API key from 5 docs + docker-compose.yml; removed MP app ID from 3 docs + tasks file
- **API_Analyze PR #1** (merge SHA: `e521658a`): Replaced real News API + Alpha Vantage keys with placeholders; added .gitignore

### Evidence Model Correction
Phase 2A.9 corrects the evidence model. Absence of PROVIDER_VERIFIED is NOT a blocker by itself. When Leonardo provides explicit OWNER_ATTESTED_COMPLETED (confirming old credential revoked/replaced) and current tree is clean and no contrary evidence exists, history sanitization can proceed. See `POST_ROTATION_RECONCILIATION.md` for full evidence model.

### Corrected Readiness Counts (Phase 2A.9 model — superseded by the Phase 2A.10.1 canonical table above)
- **3 of 41 items READY** (PII items: 33, 35, 36)
- **38 of 41 items BLOCKED** — primary blocker is WAITING_OWNER_ATTESTATION (Leonardo has not yet provided explicit per-item attestation)
- **Session invalidation count corrected:** 4 unique items (26, 31, 32, 41) — not 5 as Phase 2A.8 erroneously reported

### Per-Repository History Sanitization Readiness (Phase 2A.9 model — preserved for traceability; the authoritative table is the Phase 2A.10.1 Canonical Rewrite Table above)

| Repository | CURRENT_TREE | OWNER_ATTESTATION | SESSION | OWNER_HANDOFF | RUNTIME | HISTORY_READY | Blockers |
|---|---|---|---|---|---|---|---|
| ProFlow | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| base-corporativa | EXPOSED (PR #1 open) | PENDING | N/A | N/A | PENDING | **NO** | CURRENT_TREE_BLOCKER, OWNER_ATTESTATION_BLOCKER, RUNTIME_BLOCKER |
| FinanceControl | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| Digital-Signage-Platform | CLEAN | N/A | N/A | PENDING | N/A | **NO** | OWNER_HANDOFF_BLOCKER |
| Bot_IqOption | EXPOSED (PR #5 open) | PENDING | PENDING | N/A | PENDING | **NO** | CURRENT_TREE_BLOCKER, OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER, RUNTIME_BLOCKER |
| PayFlow-AI | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| FlowTrack | CLEAN | N/A | N/A | PENDING | N/A | **NO** | OWNER_HANDOFF_BLOCKER |
| MVP-linkedin-bot | CLEAN | PENDING | PENDING | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER |
| Portfolio-LeonardoFragoso-React | CLEAN | N/A (PII) | N/A | N/A | N/A | **YES** | None — PII removal IS the remediation |
| AndaimesPini_Project | CLEAN | N/A (data) | N/A | N/A | N/A | **YES** | None — data artifact removal IS the remediation (added in Phase 2A.10.1) |
| LogiFlow | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| API_Analyze | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |

> **Phase 2A.10.1 correction:** The Phase 2A.9 table originally omitted AndaimesPini_Project and included Bet-IA-BOT as a DELETED/N/A row. Bet-IA-BOT has been moved to the DELETED_REPOSITORY_AUDIT_RECORD. AndaimesPini_Project has been added (data artifact, current tree clean after PR #1 merge, no credential rotation dependency → READY). This raises READY repositories from 1 to 2.

### Ready Repositories: 2 of 12 (Phase 2A.10.1 corrected)

**Portfolio-LeonardoFragoso-React** and **AndaimesPini_Project** are READY for history sanitization (PII/data-only, current tree clean, no credential rotation dependency).

### Repositories that would become READY with OWNER_ATTESTED_COMPLETED:
- ProFlow, FinanceControl, PayFlow-AI, LogiFlow, API_Analyze (current tree clean, no other blockers — assuming open PR gates are resolved first where applicable)

### Phase 2A.8 Update — Post-Rotation Reconciliation (preserved)

Leonardo reports exposed credentials have been manually changed. Post-rotation reconciliation (see `POST_ROTATION_RECONCILIATION.md`) determined:

1. **3 of 41 items READY for history sanitization** (PII items: 33, 35, 36 — removal IS the remediation)
2. **38 of 41 items still BLOCKED** — primary blocker is OWNER_ATTESTATION_BLOCKER
3. **Only Portfolio-LeonardoFragoso-React is READY** for history sanitization (PII-only, current tree clean) — Phase 2A.10.1 adds AndaimesPini_Project as a second READY repo
4. **11 of 12 repositories are BLOCKED** — see per-repository table above

### Phase 2A.7 Update — Factual Dependency Changes (preserved)

1. **MVP-linkedin-bot PR #2 has been MERGED** (merge SHA: `c2afbcd5`). Current tree is clean. History sanitization is still needed for the original credential/PII commits.
2. **Two additional compromised credentials discovered** in Phase 2A.6.1: Telegram bot token (item 40) and LinkedIn password (item 41). These must be added to the history sanitization scope for MVP-linkedin-bot.
3. **Four env-dependent PRs reclassified** based on runtime evidence (see `CREDENTIAL_RUNTIME_REALITY_AUDIT.md`):
   - base-corporativa: WAITING_OWNER_RUNTIME_ATTESTATION — merge after Leonardo provides explicit attestation
   - Digital-Signage-Platform: OWNER_HANDOFF_BEFORE_MERGE — notify ICTSI first
   - FlowTrack: OWNER_HANDOFF_BEFORE_MERGE — notify ICTSI first
   - Bot_IqOption: NEEDS_MANUAL_CONFIRMATION — Railway auto-deploy state unconfirmed
4. **Former-employer systems (ICTSI/iTracker)**: History sanitization for Digital-Signage-Platform and FlowTrack should only proceed after OWNER_HANDOFF is completed and ICTSI has confirmed credential rotation.
5. **Credential rotation status**: Leonardo reports credentials changed (OWNER_REPORTED). Not yet explicitly attested per-item (OWNER_ATTESTED_COMPLETED).

## Important Principles

1. **History rewrite does NOT make credentials safe.** Credential rotation at the provider is the primary remediation. History rewrite is secondary cleanup to prevent future discovery of leaked values.
2. **Rotation must happen FIRST.** Rewriting history before rotating credentials is pointless — the credentials are already compromised and may have been scraped by automated tools.
3. **Force-push breaks things.** Anyone with a local clone will need to re-clone. Open PRs may break. Forks (if any) will diverge.
4. **Backups are mandatory.** Always create a full backup clone before any history rewrite.

## Recommended Tool: git-filter-repo

`git-filter-repo` is the modern recommended tool (replaces BFG and `git filter-branch`).

### Standard Command Pattern

```bash
# 1. Backup
git clone --mirror https://github.com/LeonardoRFragoso/<repo>.git <repo>-backup.git

# 2. Work on the backup
cd <repo>-backup.git

# 3. Remove specific files from all history
git filter-repo --invert-paths --path <file/path> --path <another/path>

# 4. Remove specific patterns (use with caution)
git filter-repo --replace-text <(echo 'literal-secret-value==>REDACTED')

# 5. Verify
git log --all --oneline | head -20
# Run gitleaks to verify
gitleaks detect --source . --no-banner -v

# 6. Push (DESTRUCTIVE — requires explicit authorization)
git push --force --mirror
```

### Alternative: BFG Repo-Cleaner

For simpler cases (deleting files by name/size):

```bash
# 1. Backup
git clone --mirror https://github.com/LeonardoRFragoso/<repo>.git <repo>-backup.git

# 2. Delete files
java -jar bfg.jar --delete-files <pattern> <repo>-backup.git

# 3. Clean up
cd <repo>-backup.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 4. Push (DESTRUCTIVE)
git push --force --mirror
```

---

## Per-Repository Sanitization Plan (12 active candidates)

> For `--replace-text` planning, secret values are NEVER printed in this document. Where literal replacement is required, the plan states `SECRET_VALUE_REFERENCE_REQUIRED` — the operator must obtain the historical secret value from the secure audit evidence (not from this document) at execution time.

### 1. ProFlow

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC when secrets were committed |
| **Forks possible** | Yes — was public. Live check: 0 forks. Document fork history but low risk. |
| **Paths to purge** | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` |
| **Literal replacement also necessary?** | No — secrets are in the two files above; file removal suffices. |
| **Branches affected** | All branches containing these files in history |
| **Tags affected** | Check `git tag` — likely none |
| **Open PRs** | PR #1 (head 4d7a463, mergeable UNKNOWN), PR #2 (head aa54292, mergeable UNKNOWN) — both copilot feature branches. Close or merge before rewrite. |
| **Force-push required** | Yes — `git push --force --mirror` |
| **Collaborator impact** | Any local clones will need re-clone |
| **Deployment integration** | Railway — no direct integration with git history (deploys from branch HEAD) |
| **Worthwhile?** | **YES** — was public, contains payment/OAuth/OpenAI credentials. High risk of automated scraping. |
| **Prerequisite** | All 7 credentials (items #1-#7 in rotation matrix) must be ROTATED first |
| **Recommended command** | `git filter-repo --invert-paths --path RAILWAY_ENV_FINAL.txt --path DEPLOY_CHECKLIST.md` |
| **Backup strategy** | `git clone --mirror` to local backup before rewrite |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER, OPEN_PR_GATE (PR #1, #2) |

### 2. base-corporativa

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. Secrets were in CURRENT TREE (now cleaned by PR #1 merge Phase 2A.11). |
| **Forks possible** | Yes — was public. Live check: 0 forks. |
| **Paths to purge** | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` (both removed from current tree by PR #1; still in history) |
| **Literal replacement also necessary?** | Yes — R2 keys were hardcoded in `backend/fix_product_images_r2.py`, `backend/list_r2_images.py`, `backend/upload_pdfs_to_r2.py`, `backend/upload_product_images_to_r2.py`. PR #1 replaced them with `os.getenv()`. Historical values still need `--replace-text` with `SECRET_VALUE_REFERENCE_REQUIRED` (R2 access key + R2 secret key values from secure audit evidence). |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | NONE (PR #1 MERGED Phase 2A.11, merge SHA e40c90f) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None — NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED (Leonardo confirms not deployed on Railway) |
| **Worthwhile?** | **YES** — was public, contains R2/payment/email/DB credentials in history. |
| **Prerequisite** | All 10 credentials (items #8-#17 in rotation matrix) must be ROTATED first |
| **Recommended command** | `git filter-repo --invert-paths --path RAILWAY_ENV_ATUALIZADO.txt --path backend/.env.railway` then `git filter-repo --replace-text` with the R2 key values (SECRET_VALUE_REFERENCE_REQUIRED) |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER |
| **Classification** | RUNTIME_GATE CLEARED (NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED). CURRENT_TREE CLEAN (PR #1 merged). Remaining blocker: OWNER_ATTESTATION_BLOCKER (credential revocation not yet explicitly attested). |

### 3. FinanceControl

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. RSA key in current tree AND history. |
| **Forks possible** | Yes — was public. Live check: 0 forks. |
| **Paths to purge** | `chave-EC2/Finance2.pem`, `backend/chave-EC2/Finance2.pem` (historical path), `backend/db.sqlite3`, `ReciboDePagamento_3_01122025173256_408_b479a41d.pdf` |
| **Literal replacement also necessary?** | No — file removal suffices. |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None identified |
| **Worthwhile?** | **YES** — was public, contains RSA private key for EC2. EC2 keypair must be rotated first. |
| **Prerequisite** | EC2 keypair (item #18 in rotation matrix) must be ROTATED/REVOKED first |
| **Recommended command** | `git filter-repo --invert-paths --path chave-EC2/Finance2.pem --path backend/chave-EC2/Finance2.pem --path backend/db.sqlite3 --path "ReciboDePagamento_3_01122025173256_408_b479a41d.pdf"` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER |

### 4. Digital-Signage-Platform

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. DB credentials in history. |
| **Forks possible** | Yes — was public. Live check: 0 forks. |
| **Paths to purge** | `secrets/db_credentials.txt`, `.env.tv`, `.env.production` |
| **Literal replacement also necessary?** | Yes — historical DB credentials in `backend/app.py`, `backend/tools/migrate_sqlite_to_mysql.py`, `backend/.env.production.example`. Use `--replace-text` with `SECRET_VALUE_REFERENCE_REQUIRED` (tvs_itracker DB URL + password values from secure audit evidence). |
| **Branches affected** | All branches (2 branches) |
| **Tags affected** | Check `git tag` |
| **Open PRs** | PR #4 (head 1f9664713c681af83a92ad4647719ab070608a57, MERGEABLE) — security cleanup. DO NOT merge (OWNER_HANDOFF_BEFORE_MERGE). |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Former employer (iTracker) — confirm no active CI/CD integration |
| **Worthwhile?** | **YES** — was public, contains former employer DB credentials. Legal review recommended. |
| **Prerequisite** | DB credentials (item #19) and JWT secret (item #20) must be ROTATED first. **Confirm with iTracker IT if DB is under their control.** |
| **Recommended command** | `git filter-repo --invert-paths --path secrets/db_credentials.txt --path .env.tv --path .env.production` then `git filter-repo --replace-text` with DB URL/password values (SECRET_VALUE_REFERENCE_REQUIRED) |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve. **Legal review recommended due to former employer IP.** |
| **Current blockers** | OWNER_HANDOFF_BLOCKER, OPEN_PR_GATE (PR #4) |
| **Constraint** | Former-employer repo. DO NOT modify infrastructure, rotate secrets, or force-push until owner handoff/authorization is documented. REWRITE_READY = NO. |

### 5. FlowTrack

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. Session tokens in history. |
| **Forks possible** | Yes — was public. Live check: 0 forks. |
| **Paths to purge** | `nohup.out` |
| **Literal replacement also necessary?** | No — file removal suffices. |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | PR #1 (head bb1c040cf241607e6aa02b30cd67d9d87fc7725b, MERGEABLE) — security cleanup. DO NOT merge (OWNER_HANDOFF_BEFORE_MERGE). |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Client (ICTSI) — confirm no active CI/CD |
| **Worthwhile?** | **YES** — was public, contains 179 session/CSRF tokens from production operations system. |
| **Prerequisite** | Session tokens (item #30) should be invalidated first. SECRET_KEY (item #29) should be rotated. |
| **Recommended command** | `git filter-repo --invert-paths --path nohup.out` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve. **Legal review recommended due to client IP.** |
| **Current blockers** | OWNER_HANDOFF_BLOCKER, SESSION_BLOCKER, OPEN_PR_GATE (PR #1) |
| **Constraint** | Former-employer repo. DO NOT modify infrastructure, rotate secrets, or force-push until owner handoff/authorization is documented. REWRITE_READY = NO. |

### 6. Bot_IqOption

| Field | Value |
|---|---|
| **Visibility** | PRIVATE (was already private) |
| **Public when leaked** | No — was always private. Lower risk of external scraping. |
| **Forks possible** | Unlikely (private repo). Live check: 0 forks. |
| **Paths to purge** | `bot_iqoption_v2/backend/.env`, `bot_iqoption_v2/backend/RAILWAY_ENV_COMPLETE.txt`, `bot_iqoption_v2/backend/bot_iqoption.log`, `bot_iqoption_v2/backend/keys/` (entire directory), `bot_iqoption_v2/backend/db.sqlite3`, `bot_iqoption_v2/backend/venv/` (entire directory) — all removed from current tree by PR #5 merge Phase 2A.11; still in history |
| **Literal replacement also necessary?** | Yes — real MERCADOPAGO_CLIENT_SECRET values in historical versions of `.env.example` and `RAILWAY_ENV_TEMPLATE.md`. PR #5 replaced them with placeholders. Historical values still need `--replace-text` with `SECRET_VALUE_REFERENCE_REQUIRED`. |
| **Branches affected** | All branches (5 branches) |
| **Tags affected** | Check `git tag` |
| **Open PRs** | NONE (PR #5 MERGED Phase 2A.11, merge SHA f26b294) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None — NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED (Leonardo confirms not deployed on Railway) |
| **Worthwhile?** | **MODERATE** — was always private, but contains production MercadoPago credentials and 197 JWT tokens in history. Worthwhile for hygiene but lower urgency than public repos. |
| **Prerequisite** | All MercadoPago credentials (items #21-#24), SECRET_KEY (#25), session tokens (#26), user keys (#27) must be ROTATED first |
| **Recommended command** | `git filter-repo --invert-paths --path bot_iqoption_v2/backend/.env --path bot_iqoption_v2/backend/RAILWAY_ENV_COMPLETE.txt --path bot_iqoption_v2/backend/bot_iqoption.log --path bot_iqoption_v2/backend/keys --path bot_iqoption_v2/backend/db.sqlite3 --path bot_iqoption_v2/backend/venv` then `git filter-repo --replace-text` with MERCADOPAGO_CLIENT_SECRET values (SECRET_VALUE_REFERENCE_REQUIRED) |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER |
| **Classification** | RAILWAY_RUNTIME_GATE CLEARED (NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED). CURRENT_TREE CLEAN (PR #5 merged). Remaining blockers: OWNER_ATTESTATION_BLOCKER (credential revocation not yet explicitly attested) + SESSION_BLOCKER (IQ Option session invalidation not yet confirmed). |

### 7. MVP-linkedin-bot

| Field | Value |
|---|---|
| **Visibility** | PRIVATE (was already private) |
| **Public when leaked** | No — was always private |
| **Forks possible** | Unlikely (private repo). Live check: 0 forks. |
| **Paths to purge** | `Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot/` (entire directory), `Auto_job_applier_linkedIn/V2-Completa/chrome_profile_linkedin_bot/` (entire directory), `Auto_job_applier_linkedIn/V1/logs/` (entire directory), `cpf.pdf`, `perguntas.csv`, any `venv/` directories |
| **Literal replacement also necessary?** | No — file/directory removal suffices. |
| **Branches affected** | All branches (2 branches) |
| **Tags affected** | Check `git tag` |
| **Open PRs** | PR #1 (head 8acdcc36980d27a4684d62d7b5ff81582588c333, mergeable UNKNOWN) — devin bot fix (NOT the merged security PR #2). Close or merge before rewrite. |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None identified |
| **Worthwhile?** | **MODERATE** — was always private, but contains Chrome session tokens and personal ID. Large repo (~867MB) — history rewrite will be slow. |
| **Prerequisite** | Chrome/Google session (#31) and LinkedIn session (#32) must be invalidated first |
| **Recommended command** | `git filter-repo --invert-paths --path Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot --path Auto_job_applier_linkedIn/V2-Completa/chrome_profile_linkedin_bot --path Auto_job_applier_linkedIn/V1/logs --path cpf.pdf --path perguntas.csv` |
| **Backup strategy** | `git clone --mirror` to local backup (will be large) |
| **Authorization required** | Leonardo must explicitly approve. **Note:** PR #1 should be reviewed/merged or closed before rewrite. |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER, OPEN_PR_GATE (PR #1) |

### 8. Portfolio-LeonardoFragoso-React

| Field | Value |
|---|---|
| **Visibility** | PUBLIC (stays public) |
| **Public when leaked** | Yes — is PUBLIC |
| **Forks possible** | Yes — is public. Live check: 0 forks. |
| **Paths to purge** | `public/Docs/cartao cnpj.pdf`, `public/Docs/contrato-social-cnpj.pdf` |
| **Literal replacement also necessary?** | No — file removal suffices. |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones will need re-clone |
| **Deployment integration** | Vercel/Netlify — deploys from branch HEAD |
| **Worthwhile?** | **YES** — is public, contains personal/business registration documents. PII exposure. |
| **Prerequisite** | None — these are PII documents, not credentials. No rotation needed. |
| **Recommended command** | `git filter-repo --invert-paths --path "public/Docs/cartao cnpj.pdf" --path "public/Docs/contrato-social-cnpj.pdf"` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | NONE — READY (PII removal IS the remediation) |

### 9. AndaimesPini_Project

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. SQLite DB with client data was in current tree. |
| **Forks possible** | Yes — was public. Live check: 0 forks. |
| **Paths to purge** | `database/db.sqlite3`, all `*.sqlite_backup` files |
| **Literal replacement also necessary?** | No — file removal suffices. |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | None (security PR #1 already merged) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Railway + Vercel — deploys from branch HEAD |
| **Worthwhile?** | **YES** — was public, contains client business data in SQLite DB. |
| **Prerequisite** | None — these are data artifacts, not credentials. No rotation needed. |
| **Recommended command** | `git filter-repo --invert-paths --path database/db.sqlite3 --use-base-name --path '*.sqlite_backup'` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | NONE — READY (data artifact removal IS the remediation; current tree clean after PR #1 merge) |
| **Note** | Not represented in the canonical 41-item credential matrix because its issue is client/business data, not credentials. It remains in the history-cleanup plan. |

### 10. PayFlow-AI

| Field | Value |
|---|---|
| **Visibility** | PUBLIC (stays public) |
| **Public when leaked** | Yes — is PUBLIC. Real Twilio credential existed in history. |
| **Forks possible** | Yes — is public. Live check: 0 forks. |
| **Paths to purge** | `Docs/CORRIGIR_TOKEN.txt` (contained the Twilio auth token), `README.md` (historical generic-api-key finding at L122) |
| **Literal replacement also necessary?** | Yes — the Twilio auth token value (32-hex) was committed in `Docs/CORRIGIR_TOKEN.txt`. Current tree was cleaned by PR #1 (Twilio token removed), but the value persists in history. Use `--replace-text` with `SECRET_VALUE_REFERENCE_REQUIRED` (Twilio auth token value from secure audit evidence). |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | None (security PR #1 already merged) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Railway — deploys from branch HEAD |
| **Worthwhile?** | **YES** — is public, real Twilio auth token was committed to history. |
| **Prerequisite** | Twilio auth token (item #28 in rotation matrix) must be ROTATED/REVOKED first |
| **Recommended command** | `git filter-repo --invert-paths --path Docs/CORRIGIR_TOKEN.txt` then `git filter-repo --replace-text` with the Twilio auth token value (SECRET_VALUE_REFERENCE_REQUIRED) to redact it from `README.md` and any other historical occurrences |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER |
| **Audit evidence** | Item #28 (Twilio, ROTATE_AND_REDEPLOY). PR #1 (merged) removed the token from current tree. History rewrite required because the real credential value was committed. |

### 11. LogiFlow

| Field | Value |
|---|---|
| **Visibility** | PUBLIC (stays public) |
| **Public when leaked** | Yes — is PUBLIC. Real Evolution API credential material was committed before current-tree cleanup. |
| **Forks possible** | Yes — is public. Live check: 0 forks. |
| **Paths to purge** | Evolution API key occurrences across docs + `docker-compose.yml`; MP app ID occurrences across docs + tasks file. Affected paths (under `LogiFlow CRM/`): `docs/MODULO_WHATSAPP.md`, `docs/WHATSAPP_SETUP.md`, `docs/COMPLETE_SETUP_GUIDE.md`, `docs/GPS_INTEGRATION_GUIDE.md`, `docs/guides/SETUP_EVOLUTION_API.md`, `docs/guides/CONFIGURAR_OAUTH2_SUITECRM.md`, `docs/guides/PROXIMOS_PASSOS_SUITECRM.md`, `docs/guides/SETUP_FOCUSNFE.md`, `evolution-api/README.md`, `docker-compose.yml`, plus MP app ID docs (`docs/MERCADOPAGO_SETUP.md`, `docs/guides/MERCADOPAGO_CREDENCIAIS.md`, `docs/guides/SETUP_MERCADOPAGO.md`, tasks file). |
| **Literal replacement also necessary?** | Yes — the Evolution API key value was committed in multiple docs and `docker-compose.yml`. Current tree was cleaned by PR #1 (merge SHA `90df4b0b`), but the value persists in history. Use `--replace-text` with `SECRET_VALUE_REFERENCE_REQUIRED` (Evolution API key value + MP app ID value from secure audit evidence). File removal is NOT appropriate here (docs files are legitimate and still useful) — only the secret values must be redacted from history. |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | None (security PR #1 already merged) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Render/Railway — deploys from branch HEAD |
| **Worthwhile?** | **YES** — is public, real Evolution API credential material was committed. |
| **Prerequisite** | Evolution API key (item #37 in rotation matrix) must be ROTATED/REVOKED first |
| **Recommended command** | `git filter-repo --replace-text` with the Evolution API key value and MP app ID value (SECRET_VALUE_REFERENCE_REQUIRED). Do NOT use `--invert-paths` on the docs files (they are legitimate documentation). |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER |
| **Audit evidence** | Item #37 (Evolution API, ROTATE_AND_REDEPLOY). PR #1 (merge SHA `90df4b0b`) removed the key from current tree. History rewrite required because real Evolution API credential material was committed. |

### 12. API_Analyze

| Field | Value |
|---|---|
| **Visibility** | PUBLIC (stays public) |
| **Public when leaked** | Yes — is PUBLIC. Real News API / Alpha Vantage keys were previously committed. |
| **Forks possible** | Yes — is public. **Live check: 1 fork (`kabann-1978/API_Analyze-B3`).** Fork risk is HIGH — the fork may retain the historical secret values even after the upstream history is rewritten. The fork owner would need to delete the fork or rewrite its history; in practice this cannot be forced. |
| **Paths to purge** | `V2/backend/.env.example` (contained real News API key at L10 and Alpha Vantage key at L11) |
| **Literal replacement also necessary?** | Yes — the News API key and Alpha Vantage key values were committed in `V2/backend/.env.example`. Current tree was cleaned by PR #1 (merge SHA `e521658a`, keys replaced with placeholders, `.gitignore` added), but the real values persist in history. Use `--replace-text` with `SECRET_VALUE_REFERENCE_REQUIRED` (News API key value + Alpha Vantage key value from secure audit evidence). |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PRs** | None (security PR #1 already merged) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone; the existing fork (`kabann-1978/API_Analyze-B3`) will diverge and may retain secrets. |
| **Deployment integration** | None identified (inactive project) |
| **Worthwhile?** | **YES** — is public, real API keys were committed. Fork risk elevates urgency. |
| **Prerequisite** | News API key (#38) and Alpha Vantage key (#39) must be REVOKED first |
| **Recommended command** | `git filter-repo --replace-text` with the News API key value and Alpha Vantage key value (SECRET_VALUE_REFERENCE_REQUIRED). |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |
| **Current blockers** | OWNER_ATTESTATION_BLOCKER, FORK_RISK (1 fork: kabann-1978/API_Analyze-B3) |
| **Audit evidence** | Items #38 (News API, REVOKE_ONLY) and #39 (Alpha Vantage, REVOKE_ONLY). PR #1 (merge SHA `e521658a`) replaced real keys with placeholders. History rewrite required because real keys were previously committed. |

---

## Execution Order (When Authorized)

### Tier 1 — Was PUBLIC + Contains Credentials/PII (Highest Risk)

1. **ProFlow** — payment/OAuth/OpenAI credentials, was public
2. **base-corporativa** — R2/payment/email/DB credentials, was public, in current tree
3. **FinanceControl** — RSA EC2 key, was public, in current tree
4. **Digital-Signage-Platform** — DB credentials + JWT secret, was public (former employer — handoff required)
5. **Portfolio-LeonardoFragoso-React** — PII documents, is public
6. **AndaimesPini_Project** — client business data, was public
7. **FlowTrack** — session tokens, was public (former employer — handoff required)
8. **PayFlow-AI** — Twilio auth token, is public
9. **LogiFlow** — Evolution API key, is public
10. **API_Analyze** — News API + Alpha Vantage keys, is public (fork risk)

### Tier 2 — Was PRIVATE + Contains Credentials/Sessions (Moderate Risk)

11. **Bot_IqOption** — MercadoPago + JWT + user keys, was private
12. **MVP-linkedin-bot** — Chrome/LinkedIn sessions + PII, was private

> Bet-IA-BOT was previously listed in a "Tier 3 — Low Priority" section. It has been removed from the execution order because the repository was deleted in Phase 2A.10 (see DELETED_REPOSITORY_AUDIT_RECORD).

---

## Pre-Execution Checklist (For Each Repo)

Before executing history rewrite on any repository:

- [ ] All credentials in that repo have been ROTATED at their provider
- [ ] Old credentials have been REVOKED
- [ ] Deployment environment updated with new credentials
- [ ] Application health-checked with new credentials
- [ ] Full mirror backup created: `git clone --mirror`
- [ ] Forks checked: `gh api repos/LeonardoRFragoso/<repo>/forks`
- [ ] Open PRs reviewed (close or merge before rewrite if possible)
- [ ] Collaborators notified (if any)
- [ ] Leonardo has given EXPLICIT per-repo authorization
- [ ] `git-filter-repo` installed: `pip install git-filter-repo`
- [ ] Test run on backup clone first
- [ ] Gitleaks verification planned post-rewrite

## Post-Execution Checklist

- [ ] `git push --force --mirror` completed
- [ ] Gitleaks run on rewritten repo: `gitleaks detect --source . --no-banner -v`
- [ ] Zero findings confirmed
- [ ] All branches verified present
- [ ] Tags verified (if any)
- [ ] Collaborators instructed to re-clone
- [ ] CI/CD verified still triggers correctly
- [ ] Deployment verified still works

---

## Fork Risk Assessment

For repos that were PUBLIC when secrets were committed, forks may contain the leaked secrets even after history rewrite. Check forks:

```bash
gh api repos/LeonardoRFragoso/<repo>/forks --jq '.[].full_name'
```

If forks exist, the fork owners would need to delete their forks or have their history rewritten too. In practice, most forks of personal projects are abandoned. Document fork count but don't attempt to force-rewrite forks.

**Live fork status (2026-08-18):** Only **API_Analyze** has a fork (`kabann-1978/API_Analyze-B3`). All other 11 active candidates have 0 forks. The API_Analyze fork elevates its risk and is recorded as a blocker/FORK_RISK in the canonical table.

---

## Summary

| Tier | Repos | Risk | Action |
|---|---|---|---|
| Tier 1 (was public + credentials/PII) | ProFlow, base-corporativa, FinanceControl, Digital-Signage-Platform, Portfolio-LeonardoFragoso-React, AndaimesPini_Project, FlowTrack, PayFlow-AI, LogiFlow, API_Analyze | HIGH | Rewrite after credential rotation / handoff |
| Tier 2 (was private + credentials/sessions) | Bot_IqOption, MVP-linkedin-bot | MODERATE | Rewrite after credential rotation / session invalidation |
| Deleted (not executable) | Bet-IA-BOT | N/A | NOT_APPLICABLE_REPOSITORY_DELETED — see DELETED_REPOSITORY_AUDIT_RECORD |

**Total active repos requiring history rewrite: 12**
**Ready for history rewrite: 2** (Portfolio-LeonardoFragoso-React, AndaimesPini_Project)
**Blocked: 10**
**History rewrites performed in Phase 2A: 0** (PLAN ONLY — awaiting authorization)

### Account-level totals (live, Phase 2A.11 updated)

| Metric | Value |
|---|---|
| ACCOUNT_TOTAL_REPOS | 30 |
| PUBLIC_REPOS | 15 |
| PRIVATE_REPOS | 15 |
| ACTIVE_REWRITE_CANDIDATES | 12 |
| DELETED_REWRITE_NA | 1 (Bet-IA-BOT) |
| REWRITE_READY | 2 |
| REWRITE_BLOCKED | 10 |
| OWNER_ATTESTATION_BLOCKED (repos) | 8 |
| SESSION_BLOCKED (repos) | 3 |
| OWNER_HANDOFF_BLOCKED (repos) | 2 |
| CURRENT_TREE_BLOCKED (repos) | 0 (cleared Phase 2A.11 — base-corporativa PR #1 + Bot_IqOption PR #5 merged) |
| RUNTIME_BLOCKED (repos) | 0 (cleared Phase 2A.11 — OWNER_ATTESTED_RUNTIME_STATE: only ProFlow on Railway) |
| RAILWAY_ACTIVE_REPOSITORIES | 1 (ProFlow only — OWNER_ATTESTED_RUNTIME_STATE) |
