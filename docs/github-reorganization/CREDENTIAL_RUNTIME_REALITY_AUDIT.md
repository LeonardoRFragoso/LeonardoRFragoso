# Credential Runtime Reality Audit — Phase 2A.7

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Status:** READ-ONLY AUDIT — No credentials rotated, no sessions invalidated, no history rewritten

> **CRITICAL:** This audit classifies each item in the original `CREDENTIAL_ROTATION_MATRIX.md` (39 items) plus 2 additional items discovered in Phase 2A.6.1 (MVP-linkedin-bot LinkedIn password + Telegram bot token) = **41 total items**. Each item is reclassified based on runtime evidence, not assumed priority. No credential values are listed.

## Methodology

For each item, evidence was gathered from:
1. GitHub repository metadata (visibility, last push, archived status)
2. GitHub deployment API (deployment history, environments)
3. Recent commit history (activity timeline)
4. Repository description and README content
5. Deployment configuration files (vercel.json, railway.json, Dockerfile, Procfile, .github/workflows)
6. PR state and mergeability
7. Known employer/client context from documentation

## Repository Runtime Classification

| Repository | Visibility | Deployments | Last Commit | Runtime Status | Evidence |
|---|---|---|---|---|---|
| ProFlow | PRIVATE | Railway Production (2026-08-18) | 2026-08-18 | ACTIVE_PRODUCTION | Description: "em produção (proflow.pro)"; Railway deployments + railway.json + Dockerfile + Procfile + CI workflows; recent commits |
| PayFlow-AI | PUBLIC | Vercel Production (2026-08-18) | 2026-08-18 | ACTIVE_PRODUCTION | Vercel production deployments on 2026-08-18 (post-security-merge); CI workflow |
| FinanceControl | PRIVATE | None | 2026-08-18 (merge only) | INACTIVE | No deployments; no CI; last real commit 2026-02-01; security merge 2026-08-18 |
| Bet-IA-BOT | PRIVATE | None | 2026-08-18 (merge only) | INACTIVE | No deployments; no CI; last real commit 2026-03-23; security merge 2026-08-18 |
| MVP-linkedin-bot | PRIVATE | Railway (2026-06-12, stale) | 2026-08-18 (merge) | INACTIVE | Last Railway deployment 2026-06-12; no CI; no deployment config in repo; personal automation tool |
| LogiFlow | PUBLIC | Vercel Production (2026-06-11) | 2026-06-11 | ACTIVE_PRODUCTION | 3 Vercel production deployments (app, site, motorista); description: "SaaS CRM/TMS"; last commit 2026-06-11 |
| API_Analyze | PUBLIC | None | 2026-01-27 | INACTIVE | No deployments; no CI; last commit 2026-01-27; API project with no active hosting |
| Portfolio | PUBLIC | Vercel Production (2026-08-18) | 2026-08-18 | ACTIVE_PRODUCTION | Vercel production deployments; description: "leonardofragosodev.netlify.app" |
| AndaimesPini | PRIVATE | Vercel Production (2026-08-18) | 2026-08-18 | ACTIVE_PRODUCTION | Vercel production deployments on 2026-08-18 (post-security-merge) |
| base-corporativa | PRIVATE | Railway Production (2026-08-17) | 2026-04-27 | ACTIVE_PRODUCTION | Description: "em produção"; Railway deployments; last real commit 2026-04-27 (security PR not yet merged) |
| Digital-Signage-Platform | PRIVATE | None | 2026-01-23 | ARCHIVED_IN_PRACTICE | No deployments; no CI; last commit 2026-01-23; former employer (ICTSI/iTracker) system |
| FlowTrack | PRIVATE | None | 2026-06-11 | ARCHIVED_IN_PRACTICE | No deployments; no CI; description: "em produção no Porto do Rio de Janeiro (ICTSI)"; former employer system |
| Bot_IqOption | PRIVATE | Railway Production (2026-06-11, stale) | 2026-06-11 | INACTIVE | Railway deployments exist but stale (last 2026-06-11); no CI; no recent activity |

---

## Per-Item Runtime Reality Audit

### CREDENTIALS (Third-party service credentials)

| # | Repo | Provider | Type | Current Tree | History | Repo Visibility | Project Status | Active Deploy? | Remediation Class | Confidence | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ProFlow | Django | SECRET_KEY | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Railway production deployments active; secret in history when repo was PUBLIC |
| 2 | ProFlow | OpenAI | API key | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | AI features in production; key in history when repo was PUBLIC |
| 3 | ProFlow | Google | OAuth client secret | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Google login in production; secret in history when repo was PUBLIC |
| 4 | ProFlow | GitHub | OAuth client secret | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | GitHub login in production; secret in history when repo was PUBLIC |
| 5 | ProFlow | Mercado Pago | Access token | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Payment flow in production; token in history when repo was PUBLIC |
| 6 | ProFlow | Mercado Pago | Client secret | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Payment auth in production; secret in history when repo was PUBLIC |
| 7 | ProFlow | Mercado Pago | Webhook secret | No | Yes | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Webhook validation in production; secret in history when repo was PUBLIC |
| 8 | base-corporativa | Cloudflare R2 | R2 access key | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | R2 storage in production; key still in current tree (PR not yet merged) |
| 9 | base-corporativa | Cloudflare R2 | R2 secret key | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Same as above |
| 10 | base-corporativa | Mercado Pago | Access token | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Payment flow in production; token still in current tree |
| 11 | base-corporativa | Mercado Pago | Public key | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Frontend payment rendering in production |
| 12 | base-corporativa | Melhor Envio | Client ID | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | MEDIUM | Shipping quote flow; check if ID can be rotated or app needs re-registration |
| 13 | base-corporativa | Melhor Envio | Client secret | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Shipping auth in production |
| 14 | base-corporativa | Melhor Envio | API token | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Shipping API calls in production |
| 15 | base-corporativa | PostgreSQL | Database URL | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | DB connections in production |
| 16 | base-corporativa | Django | Superuser password | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | HIGH | Admin login in production |
| 17 | base-corporativa | SendGrid | API key | Yes | No | PRIVATE | ACTIVE_PRODUCTION | Yes (Railway) | ROTATE_AND_REDEPLOY | HIGH | Email sending in production |
| 18 | FinanceControl | AWS EC2 | RSA private key | Yes | Yes | PRIVATE | INACTIVE | No | REVOKE_ONLY | MEDIUM | No active deployments; check if EC2 instance still running; keypair permanently compromised |
| 19 | Digital-Signage-Platform | MySQL | DB credentials | Yes | Yes | PRIVATE | ARCHIVED_IN_PRACTICE | No | OWNER_HANDOFF | HIGH | Former employer (ICTSI/iTracker) infrastructure; Leonardo should NOT rotate employer's DB without authorization |
| 20 | Digital-Signage-Platform | Application | JWT secret key | Yes | Yes | PRIVATE | ARCHIVED_IN_PRACTICE | No | OWNER_HANDOFF | HIGH | Former employer (ICTSI/iTracker) system; Leonardo must NOT rotate independently; notify ICTSI; if decommissioned, no action needed |
| 21 | Bot_IqOption | Mercado Pago | Production access token | Yes | Yes | PRIVATE | INACTIVE | Stale (Railway) | REVOKE_ONLY | MEDIUM | Railway deployments stale (last 2026-06-11); no recent activity; revoke token if service not in use |
| 22 | Bot_IqOption | Mercado Pago | Production client secret | Yes | Yes | PRIVATE | INACTIVE | Stale (Railway) | REVOKE_ONLY | MEDIUM | Same as above |
| 23 | Bot_IqOption | Mercado Pago | Public key | Yes | Yes | PRIVATE | INACTIVE | Stale (Railway) | REVOKE_ONLY | MEDIUM | Same as above |
| 24 | Bot_IqOption | Mercado Pago | Client ID | Yes | Yes | PRIVATE | INACTIVE | Stale (Railway) | UNKNOWN_REQUIRES_MANUAL_CHECK | MEDIUM | Check if client ID needs rotation or just the secret |
| 25 | Bot_IqOption | Django/App | SECRET_KEY | Yes | Yes | PRIVATE | INACTIVE | Stale (Railway) | GENERATE_NEW_LOCAL_SECRET | MEDIUM | If service is inactive, generate new secret only if redeploying |
| 28 | PayFlow-AI | Twilio | Auth token | Yes | Yes | PUBLIC | ACTIVE_PRODUCTION | Yes (Vercel) | ROTATE_AND_REDEPLOY | MEDIUM | Vercel production active; token appears real; if Twilio not used in current deployment, REVOKE_ONLY |
| 34 | Bet-IA-BOT | API-Football | API key | Yes | Yes | PRIVATE | INACTIVE | No | REVOKE_ONLY | MEDIUM | No deployments; no active usage; revoke key at API-Football |
| 37 | LogiFlow | Evolution API | API key | Yes | Yes | PUBLIC | ACTIVE_PRODUCTION | Yes (Vercel) | ROTATE_AND_REDEPLOY | MEDIUM | Vercel production active; WhatsApp integration may use this key |
| 38 | API_Analyze | News API | API key | Yes | Yes | PUBLIC | INACTIVE | No | REVOKE_ONLY | MEDIUM | No deployments; no active usage; revoke if real |
| 39 | API_Analyze | Alpha Vantage | API key | Yes | Yes | PUBLIC | INACTIVE | No | REVOKE_ONLY | MEDIUM | No deployments; no active usage; revoke if real |

### SESSIONS (Session tokens, browser profiles, runtime auth)

| # | Repo | Provider | Type | Current Tree | History | Repo Visibility | Project Status | Active Deploy? | Remediation Class | Confidence | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 26 | Bot_IqOption | IQ Option API | JWT trading session tokens (197) | Yes | Yes | PRIVATE | INACTIVE | Stale | INVALIDATE_SESSION | MEDIUM | Session tokens in log file; terminate all active IQ Option sessions; re-auth creates new tokens |
| 30 | FlowTrack | Application | Session/CSRF tokens (179) | No | Yes | PRIVATE | ARCHIVED_IN_PRACTICE | No | INVALIDATE_SESSION | MEDIUM | Runtime session tokens from production log (nohup.out); if system decommissioned at ICTSI, sessions likely expired; if still running, OWNER_HANDOFF |
| 31 | MVP-linkedin-bot | Google Chrome | Browser session tokens | Yes | Yes | PRIVATE | INACTIVE | No | INVALIDATE_SESSION | HIGH | Chrome profile committed; sign out of all Chrome/Google sessions; re-authenticate |
| 32 | MVP-linkedin-bot | LinkedIn | Session data in logs | Yes | Yes | PRIVATE | INACTIVE | No | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | HIGH | LinkedIn session data exposed in logs; sign out of all LinkedIn sessions; change password; enable 2FA |
| 40 | MVP-linkedin-bot | Telegram | Bot token | No (sanitized) | Yes | PRIVATE | INACTIVE | No | REVOKE_ONLY | HIGH | Token was in git history; revoke old bot token and create new one via BotFather |
| 41 | MVP-linkedin-bot | LinkedIn | Password (encrypted + in test) | No (sanitized) | Yes | PRIVATE | INACTIVE | No | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | HIGH | Real password was in test fixture + encrypted in tenant JSON; change LinkedIn password; invalidate sessions |

### PII (Personal data — not credentials)

| # | Repo | Type | Current Tree | History | Remediation Class | Evidence |
|---|---|---|---|---|---|---|
| 33 | MVP-linkedin-bot | CPF (Brazilian national ID) | No (removed) | Yes | REMOVE_PII_FROM_HISTORY | CPF in cpf.pdf and config files; removed from current tree; history sanitization needed |
| 35 | Portfolio | CNPJ card PDF | No (removed) | Yes | REMOVE_PII_FROM_HISTORY | CNPJ card in public/Docs; removed from current tree; repo was PUBLIC |
| 36 | Portfolio | Articles of association PDF | No (removed) | Yes | REMOVE_PII_FROM_HISTORY | Contrato social in public/Docs; removed from current tree; repo was PUBLIC |
| — | MVP-linkedin-bot | Full name, phone, address, salary, cover letter | No (sanitized) | Yes | REMOVE_PII_FROM_HISTORY | PII in personals.py, questions.py, seed scripts, JSON configs; sanitized in Phase 2A.6.1; history still contains originals |
| — | MVP-linkedin-bot | CV/resume PDFs (6 files) | No (removed) | Yes | REMOVE_PII_FROM_HISTORY | 6 PDFs removed in Phase 2A.6; history still contains them |
| — | MVP-linkedin-bot | Application history CSVs (4 files) | No (removed) | Yes | REMOVE_PII_FROM_HISTORY | 4 CSVs removed in Phase 2A.6; history still contains them |
| — | MVP-linkedin-bot | Debug screenshots (26 files) | No (removed) | Yes | REMOVE_PII_FROM_HISTORY | 26 screenshots removed in Phase 2A.6; history still contains them |

### LOCAL_APP_SECRETS (Application-internal secrets, not third-party)

| # | Repo | Type | Current Tree | History | Project Status | Remediation Class | Owner | Evidence |
|---|---|---|---|---|---|---|---|---|
| 20 | Digital-Signage-Platform | JWT secret key | Yes | Yes | ARCHIVED_IN_PRACTICE | OWNER_HANDOFF | ICTSI/iTracker | Former employer system; Leonardo must NOT rotate independently; notify ICTSI; if decommissioned, no action needed |
| 25 | Bot_IqOption | Django/app SECRET_KEY | Yes | Yes | INACTIVE | GENERATE_NEW_LOCAL_SECRET | Leonardo | Generate new secret only if redeploying |
| 29 | FlowTrack | Weak fallback SECRET_KEY | Yes | Yes | ARCHIVED_IN_PRACTICE | OWNER_HANDOFF | ICTSI/iTracker | Former employer system; Leonardo must NOT rotate independently; notify ICTSI; if decommissioned, no action needed |

> **Note on item #20:** Phase 2A.7 originally classified this as GENERATE_NEW_LOCAL_SECRET. This was corrected in Phase 2A.7.1 to OWNER_HANDOFF because the owner is ICTSI/iTracker. Leonardo must not independently generate or rotate an employer-owned production secret. The handoff may later result in: (a) owner rotates it, (b) owner confirms system decommissioned, or (c) no action required.

> **Note on item #29:** Same rationale as item #20. FlowTrack is an ICTSI system. OWNER_HANDOFF, not GENERATE_NEW_LOCAL_SECRET.

> **Note on item #19:** TYPE is CREDENTIAL (not EMPLOYER_SECRET — ownership is expressed via OWNER column, not TYPE). OWNER = ICTSI/iTracker. REMEDIATION_CLASS = OWNER_HANDOFF.

> **Note on item #30:** TYPE is SESSION. OWNER = ICTSI/iTracker. REMEDIATION_CLASS = OWNER_HANDOFF.

---

## Totals (computed by validate_credential_matrix.py)

> **Invariant:** All totals are computed programmatically from the 41 canonical rows in `CREDENTIAL_ROTATION_MATRIX.md`. Run `python3 validate_credential_matrix.py` to verify.

### By Type (sum = 41)

| Type | Count |
|---|---|
| CREDENTIAL | 31 |
| SESSION | 4 |
| LOCAL_APP_SECRET | 3 |
| PII | 3 |
| **Total** | **41** |

### By Remediation Class (sum = 41)

| Remediation Class | Count |
|---|---|
| ROTATE_AND_REDEPLOY | 18 |
| REVOKE_ONLY | 8 |
| INVALIDATE_SESSION | 2 |
| CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | 3 |
| OWNER_HANDOFF | 4 |
| GENERATE_NEW_LOCAL_SECRET | 1 |
| REMOVE_PII_FROM_HISTORY | 3 |
| UNKNOWN_REQUIRES_MANUAL_CHECK | 2 |
| NOT_APPLICABLE | 0 |
| ALREADY_INVALIDATED_WITH_EVIDENCE | 0 |
| **Total** | **41** |

### By Project Runtime Status (sum = 41)

| Runtime Status | Total Items | Credentials | Sessions | Local App Secrets | PII |
|---|---|---|---|---|---|
| ACTIVE_PRODUCTION | 21 | 19 | 0 | 0 | 2 |
| INACTIVE | 16 | 12 | 2 | 1 | 1 |
| ARCHIVED_IN_PRACTICE | 4 | 1 | 1 | 2 | 0 |
| **Total** | **41** | **31** | **4** | **3** | **3** |

### By Owner (sum = 41)

| Owner | Items |
|---|---|
| Leonardo | 37 |
| ICTSI/iTracker | 4 |
| **Total** | **41** |

### Additional PII Observations (not part of the 41 canonical items)

The following PII items were identified during the MVP-linkedin-bot audit but are documented as grouped observations, NOT as individual canonical items. They do not affect the 41-item arithmetic:

- Full name, phone, address, salary, cover letter (in personals.py, questions.py, seed scripts, JSON configs)
- 6 CV/resume PDFs
- 4 application history CSVs
- 26 debug screenshots

These are all classified as REMOVE_PII_FROM_HISTORY and will be addressed during history sanitization (after credential rotation).

---

## Four Env-Dependent PRs Re-Audit

### base-corporativa PR #1

| Field | Value |
|---|---|
| Head SHA | `e1655bb3166fa120ecaffa8e8f35dfaf33b717ca` |
| Mergeable | MERGEABLE (CLEAN) |
| Active deployment | YES — Railway production (basecorporativa.store) |
| Would merge trigger auto-deploy | YES — Railway watches main branch |
| Where env vars configured | Railway dashboard |
| Are required values replacements for exposed credentials | YES — R2 keys, MP tokens, DB URL, SendGrid, Melhor Envio all exposed |
| Is project inactive | NO — active production e-commerce |
| Client/former employer | NO — appears to be Leonardo's own commercial project |
| **Classification** | **BLOCKED_ACTIVE_PRODUCTION** — merging without setting env vars FIRST would break production |

### Digital-Signage-Platform PR #4

| Field | Value |
|---|---|
| Head SHA | `1f9664713c681af83a92ad4647719ab070608a57` |
| Mergeable | MERGEABLE (CLEAN) |
| Active deployment | NO — no deployments; last commit 2026-01-23 |
| Would merge trigger auto-deploy | NO — no deployment config |
| Where env vars configured | Local `.env.tv` or deployment server |
| Are required values replacements for exposed credentials | YES — DB credentials, JWT secret |
| Is project inactive | YES — archived in practice |
| Client/former employer | YES — ICTSI/iTracker |
| **Classification** | **OWNER_HANDOFF_BEFORE_MERGE** — former employer system; notify ICTSI before merging; if decommissioned, can merge safely |

### FlowTrack PR #1

| Field | Value |
|---|---|
| Head SHA | `bb1c040cf241607e6aa02b30cd67d9d87fc7725b` |
| Mergeable | MERGEABLE (CLEAN) |
| Active deployment | NO — no deployments; description claims "em produção" but no deployment evidence |
| Would merge trigger auto-deploy | NO — no deployment config |
| Where env vars configured | Local deployment server at ICTSI |
| Are required values replacements for exposed credentials | YES — SECRET_KEY (weak fallback) |
| Is project inactive | Likely YES — no GitHub deployments; last commit 2026-06-11; may be running on ICTSI internal infra |
| Client/former employer | YES — ICTSI (Porto do Rio de Janeiro) |
| **Classification** | **OWNER_HANDOFF_BEFORE_MERGE** — former employer system; if still running on ICTSI infra, they own the SECRET_KEY rotation; if decommissioned, can merge safely |

### Bot_IqOption PR #5

| Field | Value |
|---|---|
| Head SHA | `d3a248eee8be3979a6b96b784393f0a3b629bc69` |
| Mergeable | MERGEABLE (UNSTABLE — checks may be failing) |
| Active deployment | STALE — Railway deployments exist (last 2026-06-11) but no recent activity |
| Would merge trigger auto-deploy | Possibly — Railway may still watch main; would crash without env vars |
| Where env vars configured | Railway dashboard |
| Are required values replacements for exposed credentials | YES — MP tokens, SECRET_KEY, session tokens |
| Is project inactive | YES — last real commit 2026-06-11; no recent activity |
| Client/former employer | NO — appears to be Leonardo's personal trading bot |
| **Classification** | **NEEDS_MANUAL_CONFIRMATION** — Railway deployments exist but are stale (last 2026-06-11). A stale deployment does NOT prove GitHub auto-deploy is disabled. Leonardo must manually confirm one of: (a) Railway project deleted, (b) Railway service disabled, (c) GitHub integration/auto-deploy disabled, or (d) production branch is not main. Do NOT merge until confirmed. |

---

## Evidence Sources

- GitHub REST API (repository metadata, deployments, commits, contents)
- GitHub PR API (mergeable state, head SHA)
- Repository descriptions (production status indicators)
- Deployment environment names (Railway: "scintillating-amazement / production", "magnificent-spontaneity / production", etc.)
- Vercel deployment environments ("Production", "Preview")
- Commit timestamps (activity timeline)
- Known employer context from CREDENTIAL_ROTATION_MATRIX.md and repository descriptions
- Phase 2A.6 and 2A.6.1 audit findings

## Special Notes

### Former-Employer Infrastructure (ICTSI/iTracker)

Digital-Signage-Platform and FlowTrack were developed for ICTSI/iTracker. Leonardo should NOT independently rotate employer production DB or infrastructure credentials. The remediation path is:

1. Identify the current IT/security contact at ICTSI
2. Notify them that credentials for these systems were committed to GitHub (without transmitting secret values)
3. Request that they rotate the affected credentials
4. Record the handoff status in the rotation matrix

If these systems are decommissioned, the credentials are likely already expired/invalidated, and the classification can be updated to ALREADY_INVALIDATED_WITH_EVIDENCE.

### Publicly Exposed Credentials

ProFlow was PUBLIC when secrets were committed. Even though it is now PRIVATE, all 7 ProFlow credentials (items 1-7) must be treated as COMPROMISED and rotated.

PayFlow-AI and LogiFlow are currently PUBLIC. Any credentials in their history are exposed.

Portfolio was PUBLIC when CNPJ/contrato social PDFs were committed. Even though removed from current tree, they remain in history.

### MVP-linkedin-bot Additional Items (40, 41)

Phase 2A.6.1 discovered two additional compromised credentials not in the original matrix:
- **Item 40:** Telegram bot token (hardcoded in quick_get_id.py and get_my_id.py, now sanitized)
- **Item 41:** LinkedIn password (in test fixture as plaintext + encrypted in tenant JSON, now sanitized)

Both were committed to git history and must be treated as compromised. The LinkedIn password requires CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS. The Telegram token requires REVOKE_ONLY (create new token via BotFather).
