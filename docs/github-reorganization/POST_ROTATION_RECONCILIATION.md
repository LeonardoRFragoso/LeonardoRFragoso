# Post-Rotation Reconciliation — Phase 2A.8 (Updated Phase 2A.12 Batch 1, Phase 2A.12.1, Phase 2A.13 Batch 2, Phase 2A.14 Batch 3, Phase 2A.15)

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Phase 2A.9 update:** 2026-08-18
**Phase 2A.10 update:** 2026-08-18
**Phase 2A.10.1 update:** 2026-08-18 (history-sanitization plan canonicalization & pre-rewrite gate)
**Phase 2A.11 update:** 2026-08-18 (runtime gate closure, cleanup PR integration, pre-history-rewrite readiness)
**Phase 2A.12 Batch 1 update:** 2026-08-18 (first history rewrite executed — Portfolio + AndaimesPini)
**Phase 2A.12.1 update:** 2026-08-18 (GitHub Support cleanup packet prepared for stale PR refs)
**Phase 2A.13 Batch 2 update:** 2026-08-18 (owner attestation gate passed; history rewrite executed for FinanceControl, PayFlow-AI, LogiFlow, base-corporativa)
**Phase 2A.14 Batch 3 update:** 2026-08-18 (owner attestation + session closure gate passed; history rewrite executed for API_Analyze, Bot_IqOption, MVP-linkedin-bot)
**Phase 2A.15 update:** 2026-08-18 (owner attestation + production redeploy authorization gate passed; ProFlow history rewrite executed with Railway + Vercel redeploy triggered and healthy)
**Status:** PARTIALLY EXECUTED — Batch 1 + Batch 2 + Batch 3 + ProFlow history rewrite complete (10 repos). GitHub Support cleanup PENDING_OWNER_SUBMISSION. No credentials rotated by Devin. No provider dashboards accessed.

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

## Phase 2A.13 Batch 2 — Owner Attestation Record

**Attestation date:** 2026-08-18
**Attestation method:** Explicit YES/CONFIRMED response in Devin session (no secret values requested or provided).

Leonardo explicitly confirmed the following statement:

> "I confirm that the old exposed credentials under my ownership for base-corporativa, FinanceControl, PayFlow-AI and LogiFlow were revoked, invalidated, replaced, or otherwise made unusable. Any replacement credentials required by active services are already configured. These repositories do not depend on an active Railway production deployment."

### Evidence classification applied

| Repository | Credential Items | Prior Classification | New Classification | PROVIDER_VERIFIED? |
|---|---|---|---|---|
| base-corporativa | #8-#17 (R2 access key, R2 secret key, MP access token, MP public key, Melhor Envio client ID/secret/token, DB URL, Django superuser password, SendGrid API key) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** | NO |
| FinanceControl | #18 (AWS EC2 RSA private key) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** | NO |
| PayFlow-AI | #28 (Twilio auth token) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** | NO |
| LogiFlow | #37 (Evolution API key) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** | NO |

> **Evidence model preserved:** OWNER_ATTESTED_COMPLETED means Leonardo explicitly states the old exposed credentials are no longer usable. It does NOT mean Devin independently verified provider dashboards. PROVIDER_VERIFIED was NOT used. No provider dashboards were accessed. No credentials were rotated by Devin. No sessions were invalidated by Devin.

### Deployment-risk decisions (owner-authorized)

| Repository | Deployment Integration | Risk Decision |
|---|---|---|
| base-corporativa | Railway deployment records present (30 records, historical; owner-attested not active production) | PROCEED — Railway risk owner-attested cleared |
| FinanceControl | None identified | PROCEED — no deployment risk |
| PayFlow-AI | Active Vercel production deployment (deployed 2026-08-18) | PROCEED — owner explicitly authorized force-push accepting Vercel redeploy side effect (attestation covered Railway; Vercel authorization was a separate explicit owner decision) |
| LogiFlow | Active Vercel production deployments (4 projects, deployed 2026-08-18) | PROCEED — owner explicitly authorized force-push accepting Vercel redeploy side effect (same as PayFlow-AI) |

### History rewrite results

| Repository | Method | Secrets Purged | Source Integrity | Fresh-Clone Verify | Post-Scan | Stale PR Refs | Global Erasure |
|---|---|---|---|---|---|---|---|
| FinanceControl | --invert-paths (5 paths) | 5 paths (RSA key, 2 SQLite DBs, PDF) | PASS (341 files, identical blob SHAs) | PASS | PASS (1 benign historical README placeholder) | YES (refs/pull/1/head) | NO |
| PayFlow-AI | --replace-text (2 Twilio token values) | 2 Twilio auth tokens (32-hex) | PASS (375 files, identical blob SHAs) | PASS | PASS (1 benign README placeholder SECRET_KEY) | YES (refs/pull/1/head) | NO |
| LogiFlow | --replace-text (1 Evolution API key) | 1 Evolution API key (27 chars) | PASS (715 files, identical blob SHAs) | PASS | PASS (305 false positives: SuiteCRM DB IDs, SHAs, UUIDs, expired FB test token, current-tree placeholders) | YES (refs/pull/1/head) | NO |
| base-corporativa | --invert-paths (3 env files) + --replace-text (6 secrets) | 3 paths + 6 secrets (R2 access key, R2 secret key, 3 env-file secrets, SendGrid API key) | PASS (584 files, identical blob SHAs) | PASS | PASS (3 current-tree placeholders in example docs) | YES (refs/pull/1/head) | NO |

> All four repositories: UPSTREAM_HISTORY_SANITIZED=YES, GITHUB_MANAGED_STALE_REFS=YES, GITHUB_SUPPORT_CLEANUP_REQUIRED=YES, GLOBAL_ERASURE_PROVEN=NO. Stale `refs/pull/1/head` refs on GitHub still expose pre-rewrite commits; GitHub Support cleanup is required to dereference them and run server-side GC. See GITHUB_SUPPORT_CLEANUP_PACKET.md.

### Scope discoveries beyond the canonical plan

- **FinanceControl:** discovered an additional nested duplicate `backend/backend/db.sqlite3` (same sensitive SQLite class) not in the canonical plan; removed it alongside the planned `backend/db.sqlite3`.
- **PayFlow-AI:** the canonical plan listed `README.md` for path purge, but audit revealed the README finding was a placeholder SECRET_KEY example (false positive) and the real Twilio token appeared in TWO distinct 32-hex values (an "incorrect" and a "correct" token) in `Docs/CORRIGIR_TOKEN.txt`; both were redacted via --replace-text (file preserved in current tree with placeholder).
- **LogiFlow:** the canonical plan anticipated only Evolution API key + MP app ID; full-history gitleaks revealed 28 distinct values, but analysis showed 27 were current-tree documentation placeholders (SEU_TOKEN, sua-chave, abc123, JWT headers, etc.) and SuiteCRM DB record IDs/SHAs/UUIDs/an expired third-party Facebook SDK test token — all false positives. Only 1 real secret (Evolution API key) was absent from the current tree and was redacted. Redacting the 27 current-tree placeholders was forbidden by the source-integrity constraint (Part L).
- **base-corporativa:** discovered a real SendGrid API key (`SG.` prefix) in a historical `backend/.env` file not listed in the canonical plan's path-removal set; added `backend/.env` to path removal and the SendGrid token to --replace-text.

## Phase 2A.14 Batch 3 — Owner Attestation + Session Closure Record

**Attestation date:** 2026-08-18
**Attestation method:** Explicit CONFIRMO response in Devin session (no secret values requested or provided).

Leonardo explicitly confirmed the following statement:

> "I confirm that the old exposed credentials under my ownership for Bot_IqOption, MVP-linkedin-bot and API_Analyze were revoked, invalidated, replaced, or otherwise made unusable. I also confirm that the compromised IQ Option/browser/LinkedIn sessions identified by the audit were invalidated or expired, and that passwords were changed where required. None of these three repositories currently has an active Railway production deployment."

### Evidence classification applied

| Repository | Credential/Session Items | Prior Classification | New Classification | PROVIDER_VERIFIED? |
|---|---|---|---|---|
| Bot_IqOption | #21-#25 (MP credentials, SECRET_KEY), #26 (IQ Option JWT sessions), #27 (per-user keys) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** (#21-#25, #27) + **OWNER_ATTESTED_SESSION_INVALIDATED** (#26) | NO |
| MVP-linkedin-bot | #31 (Chrome sessions), #32 (LinkedIn sessions), #33 (CPF PII), #40 (Telegram token), #41 (LinkedIn password) | OWNER_REPORTED | **OWNER_ATTESTED_SESSION_INVALIDATED** (#31, #32, #41) + **OWNER_ATTESTED_COMPLETED** (#40) | NO |
| API_Analyze | #38 (News API key), #39 (Alpha Vantage key) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** | NO |

> **Evidence model preserved:** OWNER_ATTESTED_COMPLETED and OWNER_ATTESTED_SESSION_INVALIDATED mean Leonardo explicitly states the old exposed credentials/sessions are no longer usable. They do NOT mean Devin independently verified provider dashboards or session state. PROVIDER_VERIFIED was NOT used. No provider dashboards were accessed. No credentials were rotated by Devin. No sessions were invalidated by Devin.

### Open PR gate resolution

| Repository | PR | Action | Authorization |
|---|---|---|---|
| MVP-linkedin-bot | PR #1 (fix numeric question in PT-BR, 1 unique commit 8acdcc36) | Closed by owner authorization | Leonardo explicitly chose to close PR #1; the fix commit is preserved in branch `devin/1781123382-fix-numeric-question-no-preposition` and can be re-applied after the rewrite |

### History rewrite results

| Repository | Method | Secrets/Paths Purged | Source Integrity | Fresh-Clone Verify | Post-Scan | Stale PR Refs | Fork Risk | Global Erasure |
|---|---|---|---|---|---|---|---|---|
| API_Analyze | --replace-text (2 API key values) | 2 API keys (News API 16-char, Alpha Vantage 32-hex) from V2/backend/.env.example history | PASS (210 files, identical blob SHAs) | PASS | PASS (0 gitleaks findings) | YES (refs/pull/1/head) | YES (1 fork: kabann-1978/API_Analyze-B3) | NO |
| Bot_IqOption | --invert-paths (7 paths) + --replace-text (1 MP secret) | 7 paths (.env, RAILWAY_ENV_COMPLETE.txt, bot_iqoption.log, keys/, db.sqlite3, venv/, bot-iq.pem [scope discovery]) + 1 MP_CLIENT_SECRET + 197 JWT session tokens (in log) | PASS (295 files, identical blob SHAs) | PASS | PASS (0 gitleaks findings) | YES (refs/pull/5/head) | NO (0 forks) | NO |
| MVP-linkedin-bot | --invert-paths (6 directories + 15 PII files) | 6 directories (3 chrome_profile, V1/logs, 2 venv) + 15 PII files (cpf.pdf, perguntas.csv, Profile.pdf, 7 CV PDFs, 2 application CSVs, resume.pdf) + 7 Chrome/LinkedIn session tokens | PASS (206 files; 1 empty .gitkeep placeholder removed as part of logs/ directory cleanup — canonical plan explicitly calls for logs/ removal) | PASS | PASS (0 gitleaks findings) | YES (refs/pull/1/head + refs/pull/2/head) | NO (0 forks) | NO |

> All three repositories: UPSTREAM_HISTORY_SANITIZED=YES, GITHUB_MANAGED_STALE_REFS=YES, GITHUB_SUPPORT_CLEANUP_REQUIRED=YES, GLOBAL_ERASURE_PROVEN=NO. API_Analyze additionally has FORK_RISK=YES (1 fork not modified, may retain old secrets). Stale PR refs on GitHub still expose pre-rewrite commits; GitHub Support cleanup is required. See GITHUB_SUPPORT_CLEANUP_PACKET.md.

### Scope discoveries beyond the canonical plan

- **Bot_IqOption:** discovered a real EC2 RSA private key in `bot_iqoption_v2/chaveEC2/bot-iq.pem` (historical only, 2 commits) not in the canonical plan's path-removal set; added it to path removal in a second filter pass. This is the same sensitive class as FinanceControl's EC2 key (item #18).
- **MVP-linkedin-bot:** the canonical plan listed `cpf.pdf` and `perguntas.csv` but the full historical-only path scan revealed additional PII files: 7 CV PDFs (containing Leonardo's full name), Profile.pdf, resume.pdf, and 2 application history CSVs (all historical-only, absent from current tree). These were added to the path-removal set. One empty `.gitkeep` placeholder in `V1/logs/` was also removed as part of the logs directory cleanup (canonical plan explicitly calls for logs/ removal).

## Phase 2A.15 — ProFlow Production-Safe History Sanitization Record

**Attestation date:** 2026-08-18
**Attestation method:** Explicit CONFIRMO response in Devin session (no secret values requested or provided).

Leonardo explicitly confirmed the following statements:

> "I confirm that the old exposed credentials under my ownership identified for ProFlow were revoked, invalidated, replaced or otherwise made unusable. The replacement credentials required by the current ProFlow production deployment are already configured in Railway and the production application is operating with the replacement credentials."

> "Rewriting ProFlow main may trigger a Railway production redeployment even though the current source tree is intended to remain semantically identical. Do you authorize proceeding with the force-push and possible production redeploy?" → CONFIRMO / AUTORIZO

### Evidence classification applied

| Repository | Credential Items | Prior Classification | New Classification | PROVIDER_VERIFIED? |
|---|---|---|---|---|
| ProFlow | #1-#7 (Django SECRET_KEY, OpenAI, Google OAuth, GitHub OAuth, MP access token, MP client secret, MP webhook secret) | OWNER_REPORTED | **OWNER_ATTESTED_COMPLETED** | NO |

> **Evidence model preserved:** OWNER_ATTESTED_COMPLETED means Leonardo explicitly states the old exposed credentials are no longer usable and replacement credentials are configured in Railway. It does NOT mean Devin independently verified provider dashboards or Railway variable values. PROVIDER_VERIFIED was NOT used. No provider dashboards were accessed. No credentials were rotated by Devin. No Railway variables were modified.

### Open PR gate resolution

| PR | Classification | Action | Authorization |
|---|---|---|---|
| PR #2 (copilot/add-mercado-pago-subscription, 1 commit) | STALE_EQUIVALENT_TO_MAIN — only 7 genuinely new files (task JSONs, test file, logos), no useful unique application work | Closed | Proven equivalence (0 effective diff against main for useful work) |
| PR #1 (copilot/eldest-turtle, 1 commit, 92 new source files) | UNIQUE_WORK_PRESERVED — substantial unique application work (MP subscription, badges, payments, AI engine, auth) | Remained open; branch force-pushed with unique work preserved | No closure needed — branch rewrite preserved all 92 new source files |

### Production safety record

| Metric | Before | After |
|---|---|---|
| Frontend (www.proflow.pro) | HTTP 200 (HEALTHY) | HTTP 200 (HEALTHY) |
| API (api.proflow.pro) | HTTP 404 (normal — no root view) | HTTP 404 (normal — no root view) |
| Deployed commit | 390ea2b6ef (= main HEAD) | 514aed8a38 (= rewritten main HEAD) |
| Railway deploy triggered | — | YES (railway-app[bot], 514aed8a38, 21:43:28Z) |
| Vercel deploy triggered | — | YES (vercel[bot] Production, 514aed8a38, 21:44:04Z) |
| CI workflow | failure (pre-existing) | failure (pre-existing — not caused by rewrite) |
| Regression detected | — | NO (HEALTHY → HEALTHY) |

### History rewrite results

| Repository | Method | Secrets/Paths Purged | Source Integrity | Test/Build | Fresh-Clone Verify | Post-Scan | Stale PR Refs | Fork Risk | Global Erasure |
|---|---|---|---|---|---|---|---|---|---|
| ProFlow | --invert-paths (3 paths) + --replace-text (1 MP access token) | 3 paths (RAILWAY_ENV_FINAL.txt, DEPLOY_CHECKLIST.md, MP_PRODUCTION_VALIDATION.md) + 1 MP access token (APP_USR-<REDACTED_MP_TOKEN>, 24 chars) from backend/config/settings/dev.py + Docs/MP_PRODUCTION_VALIDATION.md history | PASS (1012 files, identical blob SHAs; Docs/MP_PRODUCTION_VALIDATION.md preserved in current tree) | PASS (Django 4.2.7 syntax check, frontend npm build SUCCESS in 10.79s) | PASS (main=514aed8, 1012 files, all secrets purged) | PASS (18 gitleaks findings, all false positives) | YES (refs/pull/2-9/head; PR #1 ref updated by branch force-push) | NO (0 forks) | NO |

### Scope discoveries beyond the canonical plan

- **MP_PRODUCTION_VALIDATION.md (root-level):** discovered a real MP access token (`APP_USR-<REDACTED_MP_TOKEN>-...`) in a historical root-level `MP_PRODUCTION_VALIDATION.md` file not listed in the canonical plan's path-removal set (canonical plan only listed `RAILWAY_ENV_FINAL.txt` and `DEPLOY_CHECKLIST.md`). Added `MP_PRODUCTION_VALIDATION.md` (root-level) to path removal. The same MP access token also appeared in `backend/config/settings/dev.py` and `Docs/MP_PRODUCTION_VALIDATION.md` history — redacted via --replace-text.
- **Docs/MP_PRODUCTION_VALIDATION.md (current tree):** this file exists in the current tree and contains only the MP public key (`APP_USR-fcc88887-...`, UUID format = public key, NOT a secret) and env var name references. It was NOT removed from the current tree — only the MP access token in its history was redacted via --replace-text. An initial filter attempt incorrectly removed it via --invert-paths; the filter was redone correctly.
- **MP public key APP_USR-fcc88887:** appears in 1135 historical files including current-tree source code (`backend/config/settings/dev.py`, `frontend/src/views/wallet/PaymentCards.vue`). This is a Mercado Pago **public key** (UUID format), NOT a secret — it is designed for frontend use. It was intentionally NOT redacted to preserve source integrity.

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
| Current tree CLEAN (security PR merged) | ProFlow, base-corporativa (PR #1 merged Phase 2A.11), FinanceControl, Digital-Signage-Platform, PayFlow-AI, MVP-linkedin-bot, Portfolio-LeonardoFragoso-React, AndaimesPini_Project, LogiFlow, API_Analyze, Bot_IqOption (PR #5 merged Phase 2A.11) | 11 repos clean |
| Current tree has credentials (PR open, not merged) | NONE | 0 repos blocked |
| Repository deleted (not executable) | Bet-IA-BOT | 1 repo — NOT_APPLICABLE_REPOSITORY_DELETED (see HISTORY_SANITIZATION_PLAN.md DELETED_REPOSITORY_AUDIT_RECORD) |

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

### base-corporativa PR #1 — MERGED Phase 2A.11

| Field | Value |
|---|---|
| Pre-merge head SHA | `e1655bb3166fa120ecaffa8e8f35dfaf33b717ca` |
| Merge SHA | `e40c90fe5e98609509ad6cf0d00406a3f92bbe60` |
| Post-merge main SHA | `e40c90fe5e98609509ad6cf0d00406a3f92bbe60` |
| State | MERGED (squash, 2026-08-18) |
| Current tree | CLEAN — all 10 credentials removed from current tree |
| Runtime gate | CLEARED — NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED (Leonardo confirms not deployed on Railway) |
| **Classification** | **RUNTIME_GATE_CLEARED, CURRENT_TREE_CLEAN** — PR #1 merged after Leonardo confirmed no active Railway deployment. Remaining blocker: OWNER_ATTESTATION_BLOCKER (credential revocation not yet explicitly attested). |
| **Action needed** | Leonardo must provide explicit OWNER_ATTESTED_COMPLETED: old credentials revoked/inactivated. History rewrite can then proceed (assuming no other blockers). |

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

### Bot_IqOption PR #5 — MERGED Phase 2A.11

| Field | Value |
|---|---|
| Pre-merge head SHA | `d3a248eee8be3979a6b96b784393f0a3b629bc69` |
| Merge SHA | `f26b29496dbb7e9c302d65252b1fdc0f956291a7` |
| Post-merge main SHA | `f26b29496dbb7e9c302d65252b1fdc0f956291a7` |
| State | MERGED (squash, 2026-08-18) |
| Current tree | CLEAN — all credentials, session tokens, key files, venv, pycache, logs, db removed from current tree |
| Source integrity | VERIFIED — 295 source files remain (209 Python, 5 frontend, 8 config, 7 docs, 7 project-meta); all source directories (accounts, billing, bot_iqoption, iqoptionapi, trading) preserved; migrations preserved; .env.example and RAILWAY_ENV_TEMPLATE.md are placeholder-only; .gitignore correct |
| Runtime gate | CLEARED — NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED (Leonardo confirms not deployed on Railway) |
| **Classification** | **RAILWAY_RUNTIME_GATE_CLEARED, CURRENT_TREE_CLEAN** — PR #5 merged after Leonardo confirmed no active Railway deployment and source integrity was verified. Remaining blockers: OWNER_ATTESTATION_BLOCKER (credential revocation not yet explicitly attested) + SESSION_BLOCKER (IQ Option session invalidation not yet confirmed). |
| **Action needed** | Leonardo must provide explicit OWNER_ATTESTED_COMPLETED for credential revocation AND confirm IQ Option sessions invalidated. History rewrite can then proceed. |

### Phase 2A.11 — Live PR Gate Update (base-corporativa #1 and Bot_IqOption #5 MERGED)

PR states updated 2026-08-18 after Phase 2A.11 merges. base-corporativa PR #1 and Bot_IqOption PR #5 were merged (squash) after Leonardo confirmed neither is deployed on Railway.

| Repository | Open PRs | Head SHA | Mergeable | Gate impact |
|---|---|---|---|---|
| ProFlow | PR #1, PR #2 (copilot feature branches) | 4d7a463 / aa54292 | UNKNOWN | Close or merge before rewrite |
| base-corporativa | NONE (PR #1 MERGED Phase 2A.11, merge SHA e40c90f) | — | — | None — current tree CLEAN |
| FinanceControl | none | — | — | None |
| Digital-Signage-Platform | PR #4 (security) | 1f9664713c681af83a92ad4647719ab070608a57 | MERGEABLE | OWNER_HANDOFF_BEFORE_MERGE — DO NOT merge |
| FlowTrack | PR #1 (security) | bb1c040cf241607e6aa02b30cd67d9d87fc7725b | MERGEABLE | OWNER_HANDOFF_BEFORE_MERGE — DO NOT merge |
| Bot_IqOption | NONE (PR #5 MERGED Phase 2A.11, merge SHA f26b294) | — | — | None — current tree CLEAN |
| MVP-linkedin-bot | PR #1 (devin bot fix) | 8acdcc36980d27a4684d62d7b5ff81582588c333 | UNKNOWN | Close or merge before rewrite |
| Portfolio-LeonardoFragoso-React | none | — | — | None |
| AndaimesPini_Project | none (security PR #1 merged) | — | — | None |
| PayFlow-AI | none (security PR #1 merged) | — | — | None |
| LogiFlow | none (security PR #1 merged) | — | — | None |
| API_Analyze | none (security PR #1 merged) | — | — | None |

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
| ProFlow | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER, OPEN_PR_GATE (PR #1, #2) |
| base-corporativa | CLEAN (PR #1 merged Phase 2A.11) | PENDING | N/A | N/A | CLEARED | **NO** | OWNER_ATTESTATION_BLOCKER |
| FinanceControl | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| Digital-Signage-Platform | CLEAN | N/A | N/A | PENDING | N/A | **NO** | OWNER_HANDOFF_BLOCKER, OPEN_PR_GATE (PR #4) |
| Bot_IqOption | CLEAN (PR #5 merged Phase 2A.11) | PENDING | PENDING | N/A | CLEARED | **NO** | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER |
| PayFlow-AI | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| FlowTrack | CLEAN | N/A | N/A | PENDING | N/A | **NO** | OWNER_HANDOFF_BLOCKER, SESSION_BLOCKER, OPEN_PR_GATE (PR #1) |
| MVP-linkedin-bot | CLEAN | PENDING | PENDING | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER, SESSION_BLOCKER, OPEN_PR_GATE (PR #1) |
| Portfolio-LeonardoFragoso-React | CLEAN | N/A (PII) | N/A | N/A | N/A | **COMPLETED** | None — PII removal IS the remediation — HISTORY REWRITTEN Phase 2A.12 Batch 1 |
| AndaimesPini_Project | CLEAN | N/A (data) | N/A | N/A | N/A | **COMPLETED** | None — data artifact removal IS the remediation — HISTORY REWRITTEN Phase 2A.12 Batch 1 |
| LogiFlow | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER |
| API_Analyze | CLEAN | PENDING | N/A | N/A | N/A | **NO** | OWNER_ATTESTATION_BLOCKER, FORK_RISK (1 fork) |

> **Phase 2A.10.1 correction:** Bet-IA-BOT was removed from this active readiness table (repository deleted in Phase 2A.10 — see HISTORY_SANITIZATION_PLAN.md DELETED_REPOSITORY_AUDIT_RECORD). AndaimesPini_Project was added (data artifact, current tree clean after security PR #1 merge, no credential rotation dependency → READY). This raises READY repositories from 1 to 2 and active candidates from 11 to 12.

### Completed Repositories: 2 of 12

**Portfolio-LeonardoFragoso-React** and **AndaimesPini_Project** have COMPLETED history sanitization (Phase 2A.12 Batch 1). PII/client-data artifacts permanently removed from all rewritten history. Upstream branches force-pushed. Fresh-clone verification passed. Gitleaks clean.

#### Post-Rewrite Remediation States (Phase 2A.12.1)

| Repository | UPSTREAM_HISTORY_SANITIZED | GITHUB_MANAGED_STALE_REFS | GITHUB_SUPPORT_REQUEST | GLOBAL_ERASURE_PROVEN |
|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | YES | YES (refs/pull/1/head → old SHA 1b9da04) | PENDING_OWNER_SUBMISSION | NO |
| AndaimesPini_Project | YES | YES (refs/pull/1/head → old SHA b66dd80) | PENDING_OWNER_SUBMISSION | NO |

> **GITHUB_SUPPORT_CLEANUP_REQUIRED = YES** for both repositories: old commits with sensitive artifacts remain reachable through GitHub-managed `refs/pull/1/head` refs. GitHub support should be contacted to garbage-collect these stale PR refs. Upstream history is sanitized; global erasure is NOT proven until GitHub cleans the PR refs.
>
> **Phase 2A.12.1:** Support request drafts prepared in `GITHUB_SUPPORT_CLEANUP_PACKET.md`. Leonardo will submit manually. No support request submitted automatically.

### Ready Repositories: 0 of 12

No repositories are currently READY for history rewrite. The two previously-ready repos have been completed.

### Blocked Repositories: 10 of 12

All other repositories are BLOCKED. The most common blocker is OWNER_ATTESTATION_BLOCKER — Leonardo has stated credentials were changed (OWNER_REPORTED) but has not yet provided explicit per-item attestation of revocation (OWNER_ATTESTED_COMPLETED). When Leonardo provides explicit attestation, the following repos would become READY (assuming no other blockers):
- **base-corporativa, FinanceControl, PayFlow-AI, LogiFlow, API_Analyze** — would become READY with OWNER_ATTESTED_COMPLETED (current tree already clean, runtime gate cleared, no other blockers; API_Analyze also has FORK_RISK to document)
- **ProFlow** — would need OWNER_ATTESTED_COMPLETED + OPEN_PR_GATE resolved (PR #1, #2)
- **MVP-linkedin-bot** — would need OWNER_ATTESTED_COMPLETED + SESSION_BLOCKER resolved + OPEN_PR_GATE resolved (PR #1)
- **Bot_IqOption** — would need OWNER_ATTESTED_COMPLETED + SESSION_BLOCKER resolved (current tree clean, runtime gate cleared)
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
