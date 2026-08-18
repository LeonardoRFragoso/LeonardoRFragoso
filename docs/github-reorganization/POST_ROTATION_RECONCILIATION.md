# Post-Rotation Reconciliation — Phase 2A.8

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Status:** READ-ONLY AUDIT — No credentials rotated by Devin. No history rewritten. No provider dashboards accessed.

> **CRITICAL:** Leonardo reports that exposed credentials have been manually changed. Devin cannot independently verify provider-side revocation or runtime validation. This document separates owner-reported actions from independently verified evidence. No credential values are listed.

## Evidence Classification

| Evidence Level | Meaning | Available to Devin? |
|---|---|---|
| OWNER_REPORTED | Leonardo states he performed the action | Yes (claimed, not independently verified) |
| GITHUB_VERIFIED | Devin verified current tree state, code patterns, or commit history via GitHub API | Yes |
| PROVIDER_VERIFIED | Credential confirmed revoked/rotated at provider dashboard | NO — Devin has no dashboard access |
| RUNTIME_VERIFIED | Application confirmed working with new credential in production | NO — Devin has no production access |

> **Important:** OWNER_REPORTED is NOT the same as PROVIDER_VERIFIED or RUNTIME_VERIFIED. History sanitization readiness for third-party credentials normally requires provider-side revocation confirmation. Since Devin cannot verify this, items are classified as OWNER_REPORTED with a WAITING_MANUAL_CONFIRMATION readiness state unless the item is PII or NOT_APPLICABLE.

## Current-Tree Rescan Results

### Scan Methodology
- **Gitleaks:** `gitleaks detect --source <repo>` on current main branch of each repo
- **Targeted credential scan:** grep for known credential patterns (sk-proj-, GOCSPX-, APP_USR-, SG., private keys, password=, SECRET_KEY=) excluding venv/node_modules/.git
- **PII-sensitive path check:** find for *.pdf, *cpf*, *cnpj*, *contrato*, chrome_profile* directories

### Per-Repository Results

| Repository | Gitleaks | Targeted Scan | PII Paths | Security PR Merged? | Notes |
|---|---|---|---|---|---|
| ProFlow | CLEAN | FINDINGS: real creds in 3 docs files | CLEAN | YES (PR #8) | Docs files with SendGrid/MP credentials not cleaned by PR #8 |
| base-corporativa | CLEAN | FINDINGS: real creds in RAILWAY_ENV_ATUALIZADO.txt, frontend/.env.production | CLEAN | NO (PR #1 open) | Expected — cleanup PR not merged |
| FinanceControl | CLEAN | CLEAN (false positives: placeholders) | CLEAN | YES (PR #1) | All findings are placeholder values |
| Digital-Signage-Platform | CLEAN | CLEAN | CLEAN (project docs, not PII) | NO (PR #4 open) | No credentials in current tree |
| Bot_IqOption | CLEAN | FINDINGS: real creds in .env, RAILWAY_ENV_COMPLETE.txt | CLEAN | NO (PR #5 open) | Expected — cleanup PR not merged |
| PayFlow-AI | CLEAN | CLEAN (false positives: venv library files) | CLEAN | YES (PR #1) | Twilio token removed |
| FlowTrack | CLEAN | CLEAN (false positive: .env.example placeholder) | CLEAN | NO (PR #1 open) | No credentials in current tree |
| MVP-linkedin-bot | CLEAN | CLEAN (false positives: synthetic test fixtures, format strings) | CLEAN | YES (PR #2) | PII files (CPF, CVs, CSVs, screenshots) confirmed removed |
| Bet-IA-BOT | CLEAN | CLEAN | CLEAN | YES (PR #1) | API-Football key removed |
| Portfolio | CLEAN | CLEAN | CLEAN | YES (PR #1) | CNPJ/contrato social PDFs confirmed removed |
| LogiFlow | CLEAN | FINDINGS: Evolution API key in 5 docs files (item 37) | CLEAN | NO PR CREATED | Item 37 still in current tree; no cleanup PR exists |
| API_Analyze | CLEAN | FINDINGS: real API keys in .env.example (items 38-39) | CLEAN | NO PR CREATED | News API + Alpha Vantage keys still in .env.example |

### New Exposure Check
No new credentials were committed during manual remediation. All findings are pre-existing:
- ProFlow docs credentials: committed in `e712f1a` and `9a1f812` (pre-existing)
- base-corporativa credentials: pre-existing (PR #1 not merged)
- Bot_IqOption credentials: pre-existing (PR #5 not merged)
- LogiFlow Evolution API key: pre-existing (no cleanup PR)
- API_Analyze API keys: pre-existing (no cleanup PR)

### Current-Tree Exposure Summary

| Category | Repos | Status |
|---|---|---|
| Current tree CLEAN (security PR merged) | FinanceControl, Digital-Signage-Platform, PayFlow-AI, MVP-linkedin-bot, Bet-IA-BOT, Portfolio | 6 repos clean |
| Current tree has credentials (PR open, not merged) | base-corporativa, Bot_IqOption | 2 repos blocked |
| Current tree has credentials (no PR created) | LogiFlow, API_Analyze | 2 repos need PR |
| Current tree has credentials in docs (PR merged but incomplete) | ProFlow | 1 repo needs follow-up |

---

## Per-Item Reconciliation (41 items)

### Items 1-7: ProFlow (7 credentials)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Django | SECRET_KEY | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from RAILWAY_ENV_FINAL.txt) | NO | NO | Docs files still contain SECRET_KEY pattern | WAITING_MANUAL_CONFIRMATION |
| 2 | OpenAI | API key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from RAILWAY_ENV_FINAL.txt) | NO | NO | Docs files may contain key | WAITING_MANUAL_CONFIRMATION |
| 3 | Google | OAuth secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from RAILWAY_ENV_FINAL.txt) | NO | NO | Not found in docs | WAITING_MANUAL_CONFIRMATION |
| 4 | GitHub | OAuth secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from RAILWAY_ENV_FINAL.txt) | NO | NO | Not found in docs | WAITING_MANUAL_CONFIRMATION |
| 5 | Mercado Pago | Access token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | PARTIAL (removed from RAILWAY_ENV_FINAL.txt but still in MERCADOPAGO_INTEGRACAO_COMPLETA.txt, RAILWAY_ENV_CONFIG.md) | NO | NO | Still in docs | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 6 | Mercado Pago | Client secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from RAILWAY_ENV_FINAL.txt) | NO | NO | Not found in docs | WAITING_MANUAL_CONFIRMATION |
| 7 | Mercado Pago | Webhook secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from RAILWAY_ENV_FINAL.txt) | NO | NO | Not found in docs | WAITING_MANUAL_CONFIRMATION |

> **ProFlow Note:** PR #8 cleaned .gitignore and .env.example but did NOT clean docs files (RAILWAY_ENV_CONFIG.md, RAILWAY_EMAIL_SETUP.md, MERCADOPAGO_INTEGRACAO_COMPLETA.txt) which still contain SendGrid and Mercado Pago credential values. A follow-up cleanup PR is needed for ProFlow docs.

### Items 8-17: base-corporativa (10 credentials)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 8 | Cloudflare R2 | Access key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in RAILWAY_ENV_ATUALIZADO.txt — PR #1 not merged) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 9 | Cloudflare R2 | Secret key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 10 | Mercado Pago | Access token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 11 | Mercado Pago | Public key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 12 | Melhor Envio | Client ID | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 13 | Melhor Envio | Client secret | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 14 | Melhor Envio | API token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 15 | PostgreSQL | Database URL | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 16 | Django | Superuser password | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | OWNER_REPORTED | NO (still in .env.railway) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 17 | SendGrid | API key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in current tree) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |

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
| 21 | Mercado Pago | Access token | REVOKE_ONLY | OWNER_REPORTED | NO (still in .env — PR #5 not merged) | NO | N/A (inactive) | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 22 | Mercado Pago | Client secret | REVOKE_ONLY | OWNER_REPORTED | NO (still in .env) | NO | N/A | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 23 | Mercado Pago | Public key | REVOKE_ONLY | OWNER_REPORTED | NO (still in .env) | NO | N/A | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 24 | Mercado Pago | Client ID | UNKNOWN_REQUIRES_MANUAL_CHECK | OWNER_REPORTED | NO (still in .env) | NO | N/A | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 25 | Django/App | SECRET_KEY | GENERATE_NEW_LOCAL_SECRET | OWNER_REPORTED | NO (still in RAILWAY_ENV_COMPLETE.txt) | N/A | N/A | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 26 | IQ Option | JWT session tokens (197) | INVALIDATE_SESSION | OWNER_REPORTED | YES (still in log file — PR #5 not merged) | NO | N/A | Still in log | WAITING_SESSION_INVALIDATION + CURRENT_TREE_EXPOSURE |
| 27 | Application | Per-user API key files | UNKNOWN_REQUIRES_MANUAL_CHECK | OWNER_REPORTED | NO (still in current tree) | NO | N/A | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |

> **Bot_IqOption Note:** PR #5 is still open. Current tree still contains all credentials and session tokens. Railway auto-deploy state unconfirmed (NEEDS_MANUAL_CONFIRMATION).

### Item 28: PayFlow-AI (1 credential)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 28 | Twilio | Auth token | ROTATE_AND_REDEPLOY | OWNER_REPORTED | YES (removed from docs by PR #1) | NO | NO | CLEAN | WAITING_MANUAL_CONFIRMATION |

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
| 40 | Telegram | Bot token | REVOKE_ONLY | OWNER_REPORTED | YES (removed from quick_get_id.py, get_my_id.py by PR #2) | NO | N/A | CLEAN | WAITING_MANUAL_CONFIRMATION |
| 41 | LinkedIn | Password | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | OWNER_REPORTED | YES (removed from test fixture + tenant JSON by PR #2) | N/A | N/A | CLEAN | WAITING_SESSION_INVALIDATION |

### Item 34: Bet-IA-BOT (1 credential)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 34 | API-Football | API key | REVOKE_ONLY | OWNER_REPORTED | YES (removed from test_new_api.py by PR #1) | NO | N/A (inactive) | CLEAN | WAITING_MANUAL_CONFIRMATION |

### Items 35-36: Portfolio (2 PII items)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 35 | Personal/Business | CNPJ card PDF | REMOVE_PII_FROM_HISTORY | N/A — PII removal IS the remediation | YES (removed by PR #1) | N/A | N/A | CLEAN | READY_FOR_HISTORY_SANITIZATION |
| 36 | Personal/Business | Articles of association PDF | REMOVE_PII_FROM_HISTORY | N/A — PII removal IS the remediation | YES (removed by PR #1) | N/A | N/A | CLEAN | READY_FOR_HISTORY_SANITIZATION |

### Item 37: LogiFlow (1 credential)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 37 | Evolution API | API key | ROTATE_AND_REDEPLOY | OWNER_REPORTED | NO (still in 5 docs files — no cleanup PR created) | NO | NO | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |

> **LogiFlow Note:** No security PR was created for LogiFlow. The Evolution API key (logiflow-evolution-key-2025) is still in 5 documentation files in the current tree. A cleanup PR is needed.

### Items 38-39: API_Analyze (2 credentials)

| # | Provider | Type | Remediation Class | Owner Report | GitHub Verified | Provider Verified | Runtime Verified | Current Tree | Readiness |
|---|---|---|---|---|---|---|---|---|---|
| 38 | News API | API key | REVOKE_ONLY | OWNER_REPORTED | NO (still in V2/backend/.env.example — no cleanup PR) | NO | N/A (inactive) | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |
| 39 | Alpha Vantage | API key | REVOKE_ONLY | OWNER_REPORTED | NO (still in V2/backend/.env.example — no cleanup PR) | NO | N/A (inactive) | Still exposed | WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE |

> **API_Analyze Note:** No security PR was created for API_Analyze. The News API and Alpha Vantage keys are still in .env.example in the current tree. A cleanup PR is needed.

---

## Readiness Summary

### By Readiness State

| Readiness State | Count | Items |
|---|---|---|
| READY_FOR_HISTORY_SANITIZATION | 3 | 33, 35, 36 (PII items — removal IS the remediation) |
| WAITING_MANUAL_CONFIRMATION | 14 | 1, 2, 3, 4, 6, 7, 18, 28, 34, 37, 38, 39, 40 + 27 (unknown check) |
| WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE | 13 | 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 26 |
| WAITING_SESSION_INVALIDATION | 4 | 26, 31, 32, 41 |
| WAITING_OWNER_HANDOFF | 4 | 19, 20, 29, 30 |
| NOT_APPLICABLE_TO_HISTORY_GATE | 0 | — |

> **Note:** Some items appear in multiple categories because they have multiple blockers (e.g., current-tree exposure + manual confirmation). The primary readiness state is the most restrictive one.

### Primary Readiness State (most restrictive, per item)

| Readiness State | Count |
|---|---|
| READY_FOR_HISTORY_SANITIZATION | 3 |
| WAITING_MANUAL_CONFIRMATION | 12 |
| WAITING_MANUAL_CONFIRMATION + CURRENT_TREE_EXPOSURE | 17 |
| WAITING_SESSION_INVALIDATION | 4 |
| WAITING_OWNER_HANDOFF | 4 |
| UNKNOWN_REQUIRES_MANUAL_CHECK | 1 |
| **Total** | **41** |

### By Evidence Level

| Evidence Level | Count |
|---|---|
| OWNER_REPORTED | 33 (all non-PII, non-handoff items) |
| GITHUB_VERIFIED (current tree clean) | 14 (items in repos with merged PRs + clean rescan) |
| GITHUB_VERIFIED (current tree still exposed) | 17 (items in repos with open/missing PRs) |
| PROVIDER_VERIFIED | 0 (Devin cannot verify) |
| RUNTIME_VERIFIED | 0 (Devin cannot verify) |
| NOT_APPLICABLE (PII/handoff) | 7 (items 19, 20, 29, 30, 33, 35, 36) |

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
| **Classification** | **MERGE_READY_AFTER_ROTATION** (conditional) — if Leonardo confirms replacement env vars are set in Railway, PR #1 can be merged to remove old values from current tree. If env vars NOT set, classification remains STILL_BLOCKED. |
| **Action needed** | Leonardo must confirm: (1) replacement env vars set in Railway, (2) application working with new values. Then merge PR #1. |

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

## Repository-by-Repository History Sanitization Readiness

| Repository | Current Tree | Rotation Status | Session Status | Owner Handoff | Rewrite Paths Known | Backup Plan | History Sanitization | Blocker |
|---|---|---|---|---|---|---|---|---|
| ProFlow | EXPOSURE in docs | OWNER_REPORTED | N/A | N/A | YES | YES (mirror clone) | **BLOCKED** | Docs files still contain SendGrid/MP credentials; follow-up cleanup PR needed |
| base-corporativa | EXPOSURE (PR #1 open) | OWNER_REPORTED | N/A | N/A | YES | YES | **BLOCKED** | PR #1 not merged; old credentials still in current tree |
| FinanceControl | CLEAN | OWNER_REPORTED | N/A | N/A | YES | YES | **BLOCKED** | Provider-side revocation of EC2 key not verified |
| Digital-Signage-Platform | CLEAN | N/A | N/A | WAITING | YES | YES | **BLOCKED** | Owner handoff to ICTSI not completed |
| Bot_IqOption | EXPOSURE (PR #5 open) | OWNER_REPORTED | OWNER_REPORTED | N/A | YES | YES | **BLOCKED** | PR #5 not merged; Railway auto-deploy unconfirmed; old credentials still in current tree |
| PayFlow-AI | CLEAN | OWNER_REPORTED | N/A | N/A | YES | YES | **BLOCKED** | Provider-side revocation of Twilio token not verified |
| FlowTrack | CLEAN | N/A | N/A | WAITING | YES | YES | **BLOCKED** | Owner handoff to ICTSI not completed |
| MVP-linkedin-bot | CLEAN | OWNER_REPORTED | OWNER_REPORTED | N/A | YES | YES | **BLOCKED** | Session invalidation not independently verified; provider revocation not verified |
| Bet-IA-BOT | CLEAN | OWNER_REPORTED | N/A | N/A | YES | YES | **BLOCKED** | Provider-side revocation of API-Football key not verified |
| Portfolio | CLEAN | N/A (PII only) | N/A | N/A | YES | YES | **READY** | PII removal IS the remediation; current tree clean; history rewrite can proceed for PII only |
| LogiFlow | EXPOSURE (no PR) | OWNER_REPORTED | N/A | N/A | YES | YES | **BLOCKED** | No cleanup PR created; Evolution API key still in 5 docs files |
| API_Analyze | EXPOSURE (no PR) | OWNER_REPORTED | N/A | N/A | YES | YES | **BLOCKED** | No cleanup PR created; API keys still in .env.example |

### Ready Repositories: 1 of 12

Only **Portfolio-LeonardoFragoso-React** is READY for history sanitization (PII-only items, current tree clean, no credential rotation dependency).

### Blocked Repositories: 11 of 12

All other repositories are BLOCKED for one or more of:
1. Current-tree exposure not cleaned (PR not merged or not created)
2. Provider-side revocation not independently verified
3. Session invalidation not independently verified
4. Owner handoff not completed
5. Railway auto-deploy state unconfirmed

---

## Additional Findings (Not New Credential Items)

### ProFlow Docs Credential Exposure

ProFlow PR #8 cleaned `.gitignore` and `backend/.env.example` but did NOT clean documentation files that contain real SendGrid and Mercado Pago credential values:
- `Docs/deployment/RAILWAY_ENV_CONFIG.md` — SendGrid API key, MP public key, MP access token
- `Docs/deployment/RAILWAY_EMAIL_SETUP.md` — SendGrid API key
- `Docs/MERCADOPAGO_INTEGRACAO_COMPLETA.txt` — MP access token, MP public key

These are pre-existing (not from manual remediation). A follow-up cleanup PR is needed for ProFlow.

### LogiFlow Missing Cleanup PR

No security PR was created for LogiFlow. The Evolution API key (`logiflow-evolution-key-2025`) is still in 5 documentation files. A cleanup PR is needed.

### API_Analyze Missing Cleanup PR

No security PR was created for API_Analyze. The News API and Alpha Vantage keys are still in `V2/backend/.env.example`. A cleanup PR is needed.

> **Note:** These findings do not add new items to the 41-item canonical matrix. They describe current-tree exposure status for existing items (5, 37, 38, 39) and identify cleanup gaps.
