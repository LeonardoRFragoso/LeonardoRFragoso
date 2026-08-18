# Post-Rotation Reconciliation — Phase 2A.8 (Updated Phase 2A.10)

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Phase 2A.9 update:** 2026-08-18
**Phase 2A.10 update:** 2026-08-18
**Status:** READ-ONLY AUDIT — No credentials rotated by Devin. No history rewritten. No provider dashboards accessed.

> **CRITICAL:** Leonardo reports that exposed credentials have been manually changed. Devin cannot independently verify provider-side revocation or runtime validation. This document separates owner-reported actions from independently verified evidence. No credential values are listed.

## Evidence Classification (Phase 2A.9 Updated)

| Evidence Level | Meaning | Available to Devin? |
|---|---|---|
| OWNER_REPORTED | Leonardo generally stated credentials were changed | Yes (claimed, not independently verified) |
| OWNER_ATTESTED_COMPLETED | Leonardo explicitly confirms the old credential/session was revoked, invalidated, replaced, or otherwise made unusable | Yes (explicit attestation required — do NOT infer) |
| GITHUB_VERIFIED | Devin verified current tree state, code patterns, or commit history via GitHub API | Yes |
| PROVIDER_VERIFIED | Credential confirmed revoked/rotated at provider dashboard | NO — Devin has no dashboard access |
| RUNTIME_VERIFIED | Application confirmed working with new credential in production | NO — Devin has no production access |
| NOT_APPLICABLE | Item is PII (removal IS remediation) or ICTSI-owned (handoff, not Leonardo's action) | N/A |

> **Phase 2A.9 Evidence Model Correction:** Absence of PROVIDER_VERIFIED must NOT automatically block history rewrite when OWNER_ATTESTED_COMPLETED is present and no contrary evidence exists. For production ROTATE_AND_REDEPLOY items, readiness requires: (1) OWNER_ATTESTED_COMPLETED for replacement + old credential revocation, (2) current tree clean, (3) no known runtime blocker. RUNTIME_VERIFIED is stronger evidence but not mandatory if Leonardo explicitly attests the production system is functioning. Never fabricate provider verification.

> **Current Evidence Status:** Leonardo has stated credentials were changed (OWNER_REPORTED) but has NOT yet provided explicit per-item attestation of revocation (OWNER_ATTESTED_COMPLETED). When Leonardo provides explicit attestation, readiness states will be updated.

## Current-Tree Rescan Results

### Scan Methodology
- **Gitleaks:** `gitleaks detect --source <repo>` on current main branch of each repo
- **Targeted credential scan:** grep for known credential patterns (sk-proj-, GOCSPX-, APP_USR-, SG., private keys, password=, SECRET_KEY=) excluding venv/node_modules/.git
- **PII-sensitive path check:** find for *.pdf, *cpf*, *cnpj*, *contrato*, chrome_profile* directories

### Per-Repository Results

| Repository | Gitleaks | Targeted Scan | PII Paths | Security PR Merged? | Notes |
|---|---|---|---|---|---|
| ProFlow | CLEAN | CLEAN (Phase 2A.9: PR #9 merged, real MP creds + PII removed from docs) | CLEAN | YES (PR #8 + PR #9) | Current tree clean after Phase 2A.9 follow-up |
| base-corporativa | CLEAN | FINDINGS: real creds in RAILWAY_ENV_ATUALIZADO.txt, frontend/.env.production | CLEAN | NO (PR #1 open) | Expected — cleanup PR not merged |
| FinanceControl | CLEAN | CLEAN (false positives: placeholders) | CLEAN | YES (PR #1) | All findings are placeholder values |
| Digital-Signage-Platform | CLEAN | CLEAN | CLEAN (project docs, not PII) | NO (PR #4 open) | No credentials in current tree |
| Bot_IqOption | CLEAN | FINDINGS: real creds in .env, RAILWAY_ENV_COMPLETE.txt | CLEAN | NO (PR #5 open) | Expected — cleanup PR not merged |
| PayFlow-AI | CLEAN | CLEAN (false positives: venv library files) | CLEAN | YES (PR #1) | Twilio token removed |
| FlowTrack | CLEAN | CLEAN (false positive: .env.example placeholder) | CLEAN | NO (PR #1 open) | No credentials in current tree |
| MVP-linkedin-bot | CLEAN | CLEAN (false positives: synthetic test fixtures, format strings) | CLEAN | YES (PR #2) | PII files (CPF, CVs, CSVs, screenshots) confirmed removed |
| Bet-IA-BOT | DELETED | N/A — repository deleted in Phase 2A.10 | N/A | N/A | Repository deleted by owner. Security audit trail preserved (item #34). |
| Portfolio | CLEAN | CLEAN | CLEAN | YES (PR #1) | CNPJ/contrato social PDFs confirmed removed |
| LogiFlow | CLEAN | CLEAN (Phase 2A.9: PR #1 merged, Evolution API key + MP app ID removed from docs) | CLEAN | YES (PR #1) | Current tree clean after Phase 2A.9 cleanup |
| API_Analyze | CLEAN | CLEAN (Phase 2A.9: PR #1 merged, API keys replaced with placeholders, .gitignore added) | CLEAN | YES (PR #1) | Current tree clean after Phase 2A.9 cleanup |

### Phase 2A.9 Cleanup Merges
- **ProFlow PR #9** (merge SHA: `390ea2b6ef2e44c0e548b4f4e4b60bee303b1a08`): Removed real MP credentials and user email PII from `MP_PRODUCTION_VALIDATION.md`
- **LogiFlow PR #1** (merge SHA: `90df4b0b727c37e9840f7002d394080f63086e08`): Removed Evolution API key from 5 docs files + docker-compose.yml; removed MP app ID from 3 docs files + tasks file
- **API_Analyze PR #1** (merge SHA: `e521658aa32c2fa568e6190a08ac26a6013315af`): Replaced real News API + Alpha Vantage keys with placeholders; added .gitignore

### New Exposure Check
No new credentials were committed during manual remediation. All findings were pre-existing and have now been cleaned:
- ProFlow docs credentials: cleaned by PR #9 (Phase 2A.9)
- base-corporativa credentials: pre-existing (PR #1 not merged)
- Bot_IqOption credentials: pre-existing (PR #5 not merged)
- LogiFlow Evolution API key: cleaned by PR #1 (Phase 2A.9)
- API_Analyze API keys: cleaned by PR #1 (Phase 2A.9)

### Current-Tree Exposure Summary (Phase 2A.9 Updated)

| Category | Repos | Status |
|---|---|---|
| Current tree CLEAN (security PR merged) | ProFlow, FinanceControl, Digital-Signage-Platform, PayFlow-AI, MVP-linkedin-bot, Bet-IA-BOT, Portfolio, LogiFlow, API_Analyze | 9 repos clean |
| Current tree has credentials (PR open, not merged) | base-corporativa, Bot_IqOption | 2 repos blocked |

---

## Per-Item Reconciliation (41 items)

### Items 1-7: ProFlow (7 credentials)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Django | SECRET_KEY | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #8 + PR #9 merged) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 2 | OpenAI | API key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #8 + PR #9 merged) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 3 | Google | OAuth secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #8 + PR #9 merged) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 4 | GitHub | OAuth secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #8 + PR #9 merged) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 5 | Mercado Pago | Access token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #9 merged — real MP token removed from MP_PRODUCTION_VALIDATION.md) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 6 | Mercado Pago | Client secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #8 + PR #9 merged) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 7 | Mercado Pago | Webhook secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #8 + PR #9 merged) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |

> **ProFlow Note (Phase 2A.9 Updated):** PR #8 cleaned .gitignore and .env.example. PR #9 (Phase 2A.9) cleaned real MP credentials and user email PII from MP_PRODUCTION_VALIDATION.md. Remaining `SG.xxxxxx` and `APP_USR-xxxxxxxx` patterns in other docs files are placeholder values. Current tree is CLEAN.

### Items 8-17: base-corporativa (10 credentials)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 8 | Cloudflare R2 | Access key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in RAILWAY_ENV_ATUALIZADO.txt — PR #1 not merged) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 9 | Cloudflare R2 | Secret key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 10 | Mercado Pago | Access token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 11 | Mercado Pago | Public key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 12 | Melhor Envio | Client ID | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 13 | Melhor Envio | Client secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 14 | Melhor Envio | API token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 15 | PostgreSQL | Database URL | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 16 | Django | Superuser password | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | OWNER_REPORTED | NO (still in .env.railway) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 17 | SendGrid | API key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |

> **base-corporativa Note:** PR #1 is still open. Current tree still contains all 10 credentials. If Leonardo has already rotated these at the providers and configured replacement env vars in Railway, the PR can be classified as MERGE_READY_AFTER_ROTATION. However, merging PR #1 is still required to remove the old values from the current tree.

### Item 18: FinanceControl (1 credential)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 18 | AWS EC2 | RSA private key | REVOKE_ONLY | OWNER_REPORTED | YES (removed from current tree by PR #1) | NO | N/A (inactive) | CLEAN | WAITING_MANUAL_CONFIRMATION |

### Items 19-20: Digital-Signage-Platform (2 items, ICTSI-owned)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 19 | MySQL (iTracker) | DB credentials | OWNER_HANDOFF | N/A — Leonardo should not rotate | YES (PR #4 open, no creds in current tree) | NO | NO | CLEAN | WAITING_OWNER_HANDOFF |
| 20 | Application | JWT secret | OWNER_HANDOFF | N/A — Leonardo should not rotate | YES (PR #4 open) | NO | NO | CLEAN | WAITING_OWNER_HANDOFF |

### Items 21-27: Bot_IqOption (7 items)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 21 | Mercado Pago | Access token | REVOKE_ONLY | OWNER_REPORTED | NO (still in .env — PR #5 not merged) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 22 | Mercado Pago | Client secret | REVOKE_ONLY | OWNER_REPORTED | NO (still in .env) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 23 | Mercado Pago | Public key | REVOKE_ONLY | OWNER_REPORTED | NO (still in .env) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 24 | Mercado Pago | Client ID | UNKNOWN_REQUIRES_MANUAL_CHECK | OWNER_REPORTED | NO (still in .env) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 25 | Django/App | SECRET_KEY | GENERATE_NEW_LOCAL_SECRET | OWNER_REPORTED | NO (still in RAILWAY_ENV_COMPLETE.txt) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 26 | IQ Option | JWT session tokens (197) | INVALIDATE_SESSION | OWNER_REPORTED | YES (still in log file — PR #5 not merged) | N/A | N/A | Still in log | CURRENT_TREE_BLOCKER + WAITING_SESSION_INVALIDATION |
| 27 | Application | Per-user API key files | UNKNOWN_REQUIRES_MANUAL_CHECK | OWNER_REPORTED | NO (still in current tree) | N/A | N/A | Still exposed | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |

> **Bot_IqOption Note:** PR #5 is still open. Current tree still contains all credentials and session tokens. Railway auto-deploy state unconfirmed (NEEDS_MANUAL_CONFIRMATION).

### Item 28: PayFlow-AI (1 credential)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 28 | Twilio | Auth token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from docs by PR #1) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |

### Items 29-30: FlowTrack (2 items, ICTSI-owned)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 29 | Application | SECRET_KEY | OWNER_HANDOFF | N/A — Leonardo should not rotate | YES (PR #1 open, weak fallback in config.py) | NO | NO | Weak fallback present | WAITING_OWNER_HANDOFF |
| 30 | Application | Session/CSRF tokens (179) | OWNER_HANDOFF | N/A — Leonardo should not rotate | YES (removed from current tree — nohup.out not in tree) | NO | NO | CLEAN | WAITING_OWNER_HANDOFF |

### Items 31-33, 40-41: MVP-linkedin-bot (5 items)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 31 | Google Chrome | Browser session tokens | INVALIDATE_SESSION | OWNER_REPORTED | YES (chrome_profile removed by PR #2) | N/A | N/A | CLEAN | WAITING_SESSION_INVALIDATION |
| 32 | LinkedIn | Session data in logs | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | OWNER_REPORTED | YES (logs removed by PR #2) | N/A | N/A | CLEAN | WAITING_SESSION_INVALIDATION |
| 33 | Personal | CPF (PII) | REMOVE_PII_FROM_HISTORY | N/A — PII removal IS the remediation | YES (cpf.pdf removed by PR #2) | N/A | N/A | CLEAN | READY_FOR_HISTORY_SANITIZATION |
| 40 | Telegram | Bot token | REVOKE_ONLY | OWNER_REPORTED | YES (removed from quick_get_id.py, get_my_id.py by PR #2) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |
| 41 | LinkedIn | Password | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | OWNER_REPORTED | YES (removed from test fixture + tenant JSON by PR #2) | N/A | N/A | CLEAN | WAITING_SESSION_INVALIDATION |

### Item 34: Bet-IA-BOT (1 credential) — REPOSITORY DELETED

> **Phase 2A.10:** Bet-IA-BOT repository was deleted by owner. History sanitization is NOT_APPLICABLE_REPOSITORY_DELETED. Canonical item #34 is preserved in the audit trail. Classification remains REVOKE_ONLY. Evidence state remains OWNER_REPORTED (repository deletion does NOT prove credential revocation).

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 34 | API-Football | API key | REVOKE_ONLY | OWNER_REPORTED | N/A — repository deleted | N/A | N/A (inactive) | DELETED | NOT_APPLICABLE_REPOSITORY_DELETED |

### Items 35-36: Portfolio (2 PII items)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 35 | Personal/Business | CNPJ card PDF | REMOVE_PII_FROM_HISTORY | N/A — PII removal IS the remediation | YES (removed by PR #1) | N/A | N/A | CLEAN | READY_FOR_HISTORY_SANITIZATION |
| 36 | Personal/Business | Articles of association PDF | REMOVE_PII_FROM_HISTORY | N/A — PII removal IS the remediation | YES (removed by PR #1) | N/A | N/A | CLEAN | READY_FOR_HISTORY_SANITIZATION |

### Item 37: LogiFlow (1 credential)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 37 | Evolution API | API key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (PR #1 merged — Evolution API key removed from 5 docs + docker-compose, MP app ID removed from 3 docs) | N/A | N/A | CLEAN | WAITING_OWNER_ATTESTATION |

> **LogiFlow Note (Phase 2A.9 Updated):** PR #1 (merge SHA: `90df4b0b`) removed the Evolution API key from all docs files and docker-compose.yml. Runtime source already used env var loading. Current tree is CLEAN.

### Items 38-39: API_Analyze (2 credentials)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 38 | News API | API key | REVOKE_ONLY | OWNER_REPORTED | YES (PR #1 merged — real key replaced with placeholder, .gitignore added) | N/A | N/A (inactive) | CLEAN | WAITING_OWNER_ATTESTATION |
| 39 | Alpha Vantage | API key | REVOKE_ONLY | OWNER_REPORTED | YES (PR #1 merged — real key replaced with placeholder, .gitignore added) | N/A | N/A (inactive) | CLEAN | WAITING_OWNER_ATTESTATION |

> **API_Analyze Note (Phase 2A.9 Updated):** PR #1 (merge SHA: `e521658a`) replaced real News API and Alpha Vantage keys with placeholders and added .gitignore. Current tree is CLEAN.

---

## Readiness Summary (Phase 2A.9 Corrected)

### Corrected Session Invalidation Count

Phase 2A.8 erroneously reported "5 items waiting session invalidation" but the unique canonical IDs are: **26, 31, 32, 41** = **4 unique items**. Item 26 was double-counted (once in session invalidation, once in current-tree exposure). This is corrected in Phase 2A.9.

### Primary Readiness State (exactly ONE per item, sum = 41)

| Readiness State | Count | Items |
|---|---|---|
| READY_FOR_HISTORY_SANITIZATION | 3 | 33, 35, 36 (PII — removal IS remediation) |
| WAITING_OWNER_ATTESTATION | 14 | 1, 2, 3, 4, 5, 6, 7, 18, 28, 34, 37, 38, 39, 40 |
| CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION | 16 | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 27 |
| CURRENT_TREE_BLOCKER + WAITING_SESSION_INVALIDATION | 1 | 26 |
| WAITING_SESSION_INVALIDATION | 3 | 31, 32, 41 |
| WAITING_OWNER_HANDOFF | 4 | 19, 20, 29, 30 |
| **Total** | **41** | — |

> **Invariant:** SUM(PRIMARY_READINESS_COUNTS) == 41. Each canonical ID 1..41 has exactly ONE primary readiness state. Secondary blockers are documented in the per-repository table but do not distort primary totals.

### By Evidence Level (Phase 2A.9 Updated)

| Evidence Level | Count |
|---|---|
| OWNER_REPORTED | 33 (Leonardo generally stated credentials changed; not yet explicitly attested per-item) |
| OWNER_ATTESTED_COMPLETED | 0 (Leonardo has not yet provided explicit per-item attestation) |
| GITHUB_VERIFIED (current tree clean) | 24 (items in repos with merged PRs + clean rescan after Phase 2A.9) |
| GITHUB_VERIFIED (current tree still exposed) | 17 (items in base-corporativa PR #1 open + Bot_IqOption PR #5 open) |
| PROVIDER_VERIFIED | 0 (Devin has no dashboard access — not a blocker per Phase 2A.9 model) |
| RUNTIME_VERIFIED | 0 (Devin has no production access — not a blocker per Phase 2A.9 model) |
| NOT_APPLICABLE (PII) | 3 (items 33, 35, 36) |
| NOT_APPLICABLE (ICTSI-owned) | 4 (items 19, 20, 29, 30) |

---

## Env-Dependent PR Re-Evaluation

### base-corporativa PR #1

| Field | Value |
|---|---|
| Head SHA | `e1655bb3166fa120ecaffa8e8f35dfaf33b717ca` |
| State | OPEN, MERGEABLE, CLEAN |
| Current tree | Still contains all 10 credentials |
| Leonardo reports rotation done | YES (OWNER_REPORTED) |
| Env vars configured in Railway? | UNKNOWN — Devin cannot verify Railway dashboard |
| **Classification** | **WAITING_OWNER_RUNTIME_ATTESTATION** — Leonardo reports credentials changed (OWNER_REPORTED) but has not provided explicit OWNER_ATTESTED_COMPLETED stating replacement env vars are configured in Railway AND production application works AND old credentials were revoked/inactivated. |
| **Action needed** | Leonardo must provide explicit attestation: (1) replacement env vars set in Railway, (2) production application works, (3) old credentials revoked. Then merge PR #1. |

### Digital-Signage-Platform PR #4

| Field | Value |
|---|---|
| Head SHA | `1f9664713c681af83a92ad4647719ab070608a57` |
| State | OPEN, MERGEABLE, CLEAN |
| Current tree | CLEAN (no credentials in current tree) |
| Owner | ICTSI/iTracker |
| **Classification** | **OWNER_HANDOFF_BEFORE_MERGE** (unchanged) — former employer system; notify ICTSI before merging |
| **Action needed** | Leonardo notifies ICTSI. If ICTSI confirms decommissioned or authorizes merge, PR #4 can be merged. |

### FlowTrack PR #1

| Field | Value |
|---|---|
| Head SHA | `bb1c040cf241607e6aa02b30cd67d9d87fc7725b` |
| State | OPEN, MERGEABLE, CLEAN |
| Current tree | CLEAN (weak fallback in config.py, but no real credentials) |
| Owner | ICTSI/iTracker |
| **Classification** | **OWNER_HANDOFF_BEFORE_MERGE** (unchanged) — former employer system; notify ICTSI before merging |
| **Action needed** | Leonardo notifies ICTSI. If ICTSI confirms decommissioned or authorizes merge, PR #1 can be merged. |

### Bot_IqOption PR #5

| Field | Value |
|---|---|
| Head SHA | `d3a248eee8be3979a6b96b784393f0a3b629bc69` |
| State | OPEN, MERGEABLE, UNSTABLE |
| Current tree | Still contains all credentials and session tokens |
| Railway auto-deploy state | UNCONFIRMED |
| **Classification** | **NEEDS_MANUAL_CONFIRMATION** (unchanged) — Railway deployments stale but auto-deploy state unconfirmed |
| **Action needed** | Leonardo must confirm: (1) Railway project deleted/disabled, OR (2) GitHub auto-deploy disabled, OR (3) production branch is not main. Then merge PR #5. |

---

## Repository-by-Repository History Sanitization Readiness (Phase 2A.9 Model)

### Blocker Categories

| Blocker Type | Meaning |
|---|---|
| CURRENT_TREE_BLOCKER | Current tree still contains real credential values (PR not merged or not created) |
| OWNER_ATTESTATION_BLOCKER | Leonardo has not yet provided explicit OWNER_ATTESTED_COMPLETED for this item |
| SESSION_BLOCKER | Session invalidation not yet confirmed |
| OWNER_HANDOFF_BLOCKER | Former-employer system — ICTSI handoff not completed |
| RUNTIME_BLOCKER | Runtime state unconfirmed (e.g., Railway auto-deploy) |

> **Phase 2A.9 Evidence Model:** "Devin cannot independently verify provider" is NOT a blocker by itself. Absence of PROVIDER_VERIFIED does not block history rewrite when OWNER_ATTESTED_COMPLETED is present and no contrary evidence exists.

### Per-Repository Status

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
| Bet-IA-BOT | DELETED | N/A | N/A | N/A | N/A | **N/A** | NOT_APPLICABLE_REPOSITORY_DELETED |
| Portfolio | CLEAN | N/A (PII) | N/A | N/A | N/A | **YES** | None — PII removal IS the remediation |
| LogiFlow | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| API_Analyze | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |

### Ready Repositories: 1 of 12

Only **Portfolio-LeonardoFragoso-React** is READY for history sanitization (PII-only items, current tree clean, no credential rotation dependency).

### Blocked Repositories: 11 of 12

All other repositories are BLOCKED. The most common blocker is OWNER_ATTESTATION_BLOCKER — Leonardo has stated credentials were changed (OWNER_REPORTED) but has not yet provided explicit per-item attestation of revocation (OWNER_ATTESTED_COMPLETED). When Leonardo provides explicit attestation, the following repos would become READY (assuming no other blockers):
- **ProFlow, FinanceControl, PayFlow-AI, LogiFlow, API_Analyze** — would become READY with OWNER_ATTESTED_COMPLETED (current tree already clean, no other blockers)
- **MVP-linkedin-bot** — would need OWNER_ATTESTED_COMPLETED + SESSION_BLOCKER resolved
- **base-corporativa** — would need OWNER_ATTESTED_COMPLETED + CURRENT_TREE_BLOCKER (PR #1 merge) + RUNTIME_BLOCKER resolved
- **Bot_IqOption** — would need OWNER_ATTESTED_COMPLETED + CURRENT_TREE_BLOCKER (PR #5 merge) + SESSION_BLOCKER + RUNTIME_BLOCKER resolved
- **Digital-Signage-Platform, FlowTrack** — would need OWNER_HANDOFF_BLOCKER resolved (ICTSI confirmation)

---

## Phase 2A.9 Additional Findings

### ProFlow Docs Credential Exposure (RESOLVED)

ProFlow PR #8 cleaned `.gitignore` and `backend/.env.example` but did NOT clean documentation files. Phase 2A.9 PR #9 resolved this by removing real MP credentials and user email PII from `MP_PRODUCTION_VALIDATION.md`. The remaining `SG.xxxxxx` and `APP_USR-xxxxxxxx` patterns in other docs files are placeholder values, not real credentials.

### LogiFlow Cleanup (RESOLVED)

Phase 2A.9 PR #1 (merge SHA: `90df4b0b727c37e9840f7002d394080f63086e08`) removed the Evolution API key from 5 docs files + docker-compose.yml and the MP app ID from 3 docs files + tasks file. Runtime source already used env var loading. Current tree is now clean.

### API_Analyze Cleanup (RESOLVED)

Phase 2A.9 PR #1 (merge SHA: `e521658aa32c2fa568e6190a08ac26a6013315af`) replaced real News API and Alpha Vantage keys with placeholders in `V2/backend/.env.example` and added `.gitignore`. Current tree is now clean.

> **Note:** These findings do not add new items to the 41-item canonical matrix. They describe current-tree exposure status for existing items (5, 37, 38, 39) which have now been resolved.
