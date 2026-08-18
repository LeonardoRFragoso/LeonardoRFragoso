# Credential Rotation Matrix — Phase 2A (Updated Phase 2A.7)

**Account:** LeonardoRFragoso
**Phase 2A date:** 2026-08-17
**Phase 2A.7 update:** 2026-08-18
**Status:** ACTIVE — Leonardo must perform all rotations manually

> **CRITICAL:** No credential values are listed in this document. All credentials committed to Git must be treated as COMPROMISED regardless of whether the repository is now private or the file was removed from the current tree. Removing a file, making a repo private, or rewriting history does NOT make a credential safe — rotation/revocation at the provider is required.

## Rotation Priority Order

- **P0 — Immediate:** Cloud/storage access keys, payment provider secrets, database credentials, private RSA/SSH keys, OAuth client secrets, OpenAI/Twilio/SendGrid API credentials
- **P1 — High:** Application signing secrets (Django/JWT), webhook secrets, session secrets
- **P2 — Medium:** Expired historical sessions/tokens, development-only keys, example-file leaks

## Status Legend

| Status | Meaning |
|---|---|
| NOT_STARTED | Rotation not yet attempted |
| MANUAL_ACTION_REQUIRED | Leonardo must perform this rotation manually — no automated access available |
| ROTATED | New credential created, old one replaced in deployment environment |
| REVOKED | Old credential revoked/disabled at provider |
| VALIDATED | Post-rotation health check confirmed application works with new credential |
| NOT_APPLICABLE | Credential is not real or not in use |

---

## P0 — Immediate Rotation Required

### ProFlow

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Django | Application secret key (SECRET_KEY) | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `SECRET_KEY` | Verify Django session cookies invalidated; users re-login | Yes — generate new secret, update Railway env var, redeploy |
| 2 | OpenAI | API key (sk-proj-...) | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `OPENAI_API_KEY` | Verify AI features still work | Yes — revoke key in OpenAI dashboard, create new key, update Railway env var |
| 3 | Google | OAuth client secret (GOCSPX-...) | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `GOOGLE_OAUTH_CLIENT_SECRET` | Verify Google login still works | Yes — reset OAuth client secret in Google Cloud Console, update Railway env var |
| 4 | GitHub | OAuth client secret | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `GITHUB_OAUTH_CLIENT_SECRET` | Verify GitHub login still works | Yes — generate new OAuth app secret in GitHub Developer Settings, update Railway env var |
| 5 | Mercado Pago | Access token (APP_USR-...) | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `MERCADOPAGO_ACCESS_TOKEN` | Verify payment flow works | Yes — revoke and reissue token in Mercado Pago developer dashboard, update Railway env var |
| 6 | Mercado Pago | Client secret | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `MERCADOPAGO_CLIENT_SECRET` | Verify payment authentication works | Yes — rotate in Mercado Pago dashboard, update Railway env var |
| 7 | Mercado Pago | Webhook secret | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` | No | Yes | Yes | NOT_STARTED | Railway (ProFlow production) | `MERCADOPAGO_WEBHOOK_SECRET` | Verify webhook signature validation works | Yes — regenerate webhook secret in MP dashboard, update Railway env var |

### base-corporativa

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Cloudflare R2 / AWS-compatible | R2 access key | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway`, `backend/fix_product_images_r2.py`, `backend/list_r2_images.py`, `backend/upload_pdfs_to_r2.py`, `backend/upload_product_images_to_r2.py` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `R2_ACCESS_KEY` | Verify R2 storage operations still work | Yes — create new R2 API token in Cloudflare dashboard, revoke old token, update Railway env var |
| 9 | Cloudflare R2 / AWS-compatible | R2 secret key | Same as above | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `R2_SECRET_KEY` | Verify R2 storage operations still work | Yes — rotate alongside R2 access key |
| 10 | Mercado Pago | Access token | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `MERCADOPAGO_ACCESS_TOKEN` | Verify payment flow works | Yes — revoke and reissue in MP dashboard, update Railway env var |
| 11 | Mercado Pago | Public key | `RAILWAY_ENV_ATUALIZADO.txt` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `MERCADOPAGO_PUBLIC_KEY` | Verify frontend payment rendering works | Yes — rotate in MP dashboard, update Railway env var |
| 12 | Melhor Envio | Client ID | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `MELHOR_ENVIO_CLIENT_ID` | Verify shipping quote flow works | Yes — check if client ID can be rotated or if app needs re-registration |
| 13 | Melhor Envio | Client secret | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `MELHOR_ENVIO_CLIENT_SECRET` | Verify shipping auth works | Yes — rotate in Melhor Envio dashboard, update Railway env var |
| 14 | Melhor Envio | API token | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `MELHOR_ENVIO_API_TOKEN` | Verify shipping API calls work | Yes — revoke and reissue in Melhor Envio dashboard, update Railway env var |
| 15 | Database (PostgreSQL/external) | Database URL with credentials | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `DATABASE_URL` | Verify DB connections work with new password | Yes — rotate DB password in Railway/DB provider, update DATABASE_URL env var |
| 16 | Django | Superuser password | `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `DJANGO_SUPERUSER_PASSWORD` | Verify admin login works with new password | Yes — change superuser password via Django admin or `manage.py changepassword` |
| 17 | SendGrid | API key | `backend/.env.railway` | Yes | No | Yes | NOT_STARTED | Railway (base-corporativa production) | `SENDGRID_API_KEY` | Verify email sending works | Yes — revoke key in SendGrid dashboard, create new key, update Railway env var |

### FinanceControl

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 18 | AWS EC2 | RSA private key (keypair) | `chave-EC2/Finance2.pem` (also `backend/chave-EC2/Finance2.pem` in history) | Yes | Yes | Yes — **keypair is permanently compromised** | NOT_STARTED | EC2 instance(s) accessible via this keypair | N/A (SSH key, not env var) | Verify new SSH access works; verify old key removed from authorized_keys | **YES — CRITICAL MANUAL ACTION:** 1) Check if EC2 instance(s) still active. 2) Generate new SSH key pair in AWS console. 3) Update `authorized_keys` on instance(s) with new public key (or use AWS SSM). 4) Validate new SSH access. 5) Remove old public key from `authorized_keys`. 6) Delete/retire compromised keypair in AWS console. **Deleting the .pem file does NOT rotate the key.** |

### Digital-Signage-Platform

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 19 | Database (MySQL) | DB credentials (DB name, user, password, root password) | `secrets/db_credentials.txt` (current tree — may be sanitized to template but still contains non-placeholder values); history commit `17f5403` had real values | Yes | Yes | Yes | NOT_STARTED | iTracker corporate DB (tvs_itracker) | `DATABASE_URL` / DB connection config | Verify DB connections work with new credentials | **YES — MANUAL ACTION:** 1) Rotate DB user password and root password in MySQL. 2) Update deployment config with new credentials. 3) Verify application connects. **Note:** This appears to be former-employer (iTracker) infrastructure. Confirm with iTracker IT before rotating if the DB is still under their control. |
| 20 | Application | JWT secret key | `.env.tv` (current tree) | Yes | Yes | Yes | NOT_STARTED | TVS signage deployment | `JWT_SECRET_KEY` | Verify JWT token validation works with new secret; existing tokens invalidated | Yes — generate new strong JWT secret, update `.env.tv` (or better, use env var injection), redeploy |

### Bot_IqOption

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 21 | Mercado Pago | Production access token | `bot_iqoption_v2/backend/.env`, `RAILWAY_ENV_COMPLETE.txt` | Yes | Yes | Yes | NOT_STARTED | Railway (Bot_IqOption production) | `MERCADOPAGO_ACCESS_TOKEN` | Verify payment flow works | Yes — revoke and reissue in MP dashboard, update Railway env var |
| 22 | Mercado Pago | Production client secret | `.env`, `RAILWAY_ENV_COMPLETE.txt`, `.env.example` (real value!), `RAILWAY_ENV_TEMPLATE.md` (real value!) | Yes | Yes | Yes | NOT_STARTED | Railway (Bot_IqOption production) | `MERCADOPAGO_CLIENT_SECRET` | Verify payment auth works | Yes — rotate in MP dashboard, update Railway env var |
| 23 | Mercado Pago | Public key | `.env` | Yes | Yes | Yes | NOT_STARTED | Railway (Bot_IqOption production) | `MERCADOPAGO_PUBLIC_KEY` | Verify frontend rendering works | Yes — rotate in MP dashboard, update Railway env var |
| 24 | Mercado Pago | Client ID | `.env` | Yes | Yes | Likely | NOT_STARTED | Railway (Bot_IqOption production) | `MERCADOPAGO_CLIENT_ID` | Verify OAuth flow works | Yes — check if client ID needs rotation or just the secret |
| 25 | Application | Django/app secret key | `RAILWAY_ENV_COMPLETE.txt` | Yes | Yes | Yes | NOT_STARTED | Railway (Bot_IqOption production) | `SECRET_KEY` | Verify session validation works | Yes — generate new secret, update Railway env var |
| 26 | IQ Option API | JWT trading session tokens (197 tokens) | `bot_iqoption_v2/backend/bot_iqoption.log` | Yes | Yes | Yes — sessions are compromised | NOT_STARTED | IQ Option trading sessions | N/A (session tokens, not env vars) | Verify trading sessions terminated; new sessions require re-authentication | Yes — terminate all active IQ Option sessions. These are runtime session tokens, not static credentials. Re-authentication will create new tokens. |
| 27 | Application | Per-user API key files | `bot_iqoption_v2/backend/keys/user_2_key.key`, `user_3_key.key`, `user_4_key.key` | Yes | Yes | Yes | NOT_STARTED | Per-user authentication | N/A (key files) | Verify user authentication still works after key regeneration | Yes — regenerate per-user keys if the authentication system supports it. If keys are derived from user passwords, password resets may be needed. |

---

## P1 — High Priority Rotation

### PayFlow-AI

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 28 | Twilio | Auth token (32-hex) | `Docs/CORRIGIR_TOKEN.txt` | Yes | Yes | Yes (if real — appears real) | NOT_STARTED | Twilio account / PayFlow-AI deployment | `TWILIO_AUTH_TOKEN` | Verify SMS/voice features work | Yes — revoke auth token in Twilio console, create new token, update deployment env var |

### FlowTrack

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 29 | Application | Weak fallback SECRET_KEY | `Backend/config.py` | Yes | Yes | Yes (weak default) | NOT_STARTED | ICTSI/FlowTrack deployment | `SECRET_KEY` | Verify app starts with new required env var | Yes — set a strong SECRET_KEY in the deployment environment. Remove the weak fallback from config.py (cleanup PR handles this). |
| 30 | Application | Session/CSRF tokens (179 findings) | `nohup.out` (history only) | No | Yes | Yes — sessions compromised | NOT_STARTED | ICTSI operations system | N/A (runtime session tokens) | Verify old sessions invalidated | Yes — these are runtime session tokens from a production log. Invalidate active sessions if the system is still running. If the system is decommissioned, mark as NOT_APPLICABLE. |

### MVP-linkedin-bot

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 31 | Google Chrome | Browser session tokens (policy_recovery_token, receiver_id_hash_token, hex_encoded_hmac_key) | `Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot/`, `V2-Completa/chrome_profile_linkedin_bot/` | Yes | Yes | Yes — Chrome/Google session compromised | NOT_STARTED | Chrome browser profile | N/A (browser session) | Verify Chrome sync/sign-in requires re-authentication | Yes — sign out of Chrome/Google in all sessions. Re-authenticate. The committed Chrome profile allows session hijacking. |
| 32 | LinkedIn | Session data in logs | `Auto_job_applier_linkedIn/V1/logs/log.txt` | Yes | Yes | Yes — LinkedIn session data exposed | NOT_STARTED | LinkedIn account | N/A (session data) | Verify LinkedIn account security | Yes — sign out of all LinkedIn sessions (Settings → Security → Sessions). Change LinkedIn password if any auth tokens were exposed. Enable 2FA if not already. |
| 33 | Personal | CPF (Brazilian national ID) | `cpf.pdf` | Yes | Yes | N/A — not a credential but PII | NOT_APPLICABLE | N/A | N/A | N/A | No rotation needed — document removed from tree. Consider identity monitoring. |

### Bet-IA-BOT

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 34 | API-Football | API key | `backend/test_new_api.py` (line 11) | Yes | Yes | Yes | NOT_STARTED | API-Football account | `API_FOOTBALL_KEY` | Verify API calls work with new key | Yes — revoke key in API-Football dashboard, create new key, update env var |

---

## P2 — Medium Priority / Review

### Portfolio-LeonardoFragoso-React

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 35 | Personal/Business | CNPJ card PDF | `public/Docs/cartao cnpj.pdf` | Yes | Yes | N/A — PII, not a credential | NOT_APPLICABLE | N/A | N/A | N/A | No rotation — document removed from tree. Monitor for identity misuse. |
| 36 | Personal/Business | Articles of association PDF | `public/Docs/contrato-social-cnpj.pdf` | Yes | Yes | N/A — PII, not a credential | NOT_APPLICABLE | N/A | N/A | N/A | No rotation — document removed from tree. |

### LogiFlow

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 37 | Evolution API | API key (logiflow-evolution-key-2025) | Multiple docs files (8 occurrences) | Yes | Yes | Yes (appears real) | NOT_STARTED | Evolution API / LogiFlow | `EVOLUTION_API_KEY` | Verify WhatsApp integration works | Yes — rotate key in Evolution API dashboard, update env var, update docs with placeholder |

### API_Analyze

| # | Provider | Credential Type | Location | Current Tree | History | Rotation Required | Rotation Status | Deployment(s) Affected | Env Vars Affected | Post-Rotation Validation | Manual Action Required |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 38 | News API | API key | `V2/backend/.env.example` | Yes | Yes | Yes (if real — 32-char hex, not placeholder) | NOT_STARTED | None (no deployment) | `NEWS_API_KEY` | N/A — no active deployment | Yes — rotate key in News API dashboard if real. Replace .env.example with placeholder. |
| 39 | Alpha Vantage | API key | `V2/backend/.env.example` | Yes | Yes | Yes (if real — not placeholder pattern) | NOT_STARTED | None (no deployment) | `ALPHA_VANTAGE_API_KEY` | N/A — no active deployment | Yes — rotate key in Alpha Vantage dashboard if real. Replace .env.example with placeholder. |

---

## Summary

| Priority | Count | Status |
|---|---|---|
| P0 — Immediate | 27 credentials across 5 repos | ALL NOT_STARTED / MANUAL_ACTION_REQUIRED |
| P1 — High | 7 credentials across 4 repos | ALL NOT_STARTED / MANUAL_ACTION_REQUIRED |
| P2 — Medium/Review | 5 items across 3 repos | NOT_STARTED or NOT_APPLICABLE |
| **Total credentials requiring rotation** | **39** | **0 rotated** |

### Critical Manual Actions for Leonardo

**Before anything else — P0 credentials (do these FIRST):**

1. **AWS EC2 (FinanceControl):** Check if the EC2 instance is still active. If so, generate a new SSH key, update authorized_keys, validate access, remove old key, delete compromised keypair.
2. **Cloudflare R2 (base-corporativa):** Create new R2 API token, revoke old token, update Railway env vars for base-corporativa.
3. **Mercado Pago (ProFlow + base-corporativa + Bot_IqOption):** Revoke and reissue ALL Mercado Pago tokens across 3 separate applications. Update Railway env vars for each.
4. **OpenAI (ProFlow):** Revoke API key, create new key, update Railway env var.
5. **Google OAuth (ProFlow):** Reset OAuth client secret in Google Cloud Console, update Railway env var.
6. **GitHub OAuth (ProFlow):** Generate new OAuth app secret, update Railway env var.
7. **Database credentials (base-corporativa + Digital-Signage-Platform):** Rotate DB passwords. For Digital-Signage-Platform, confirm with iTracker IT if DB is under their control.
8. **SendGrid (base-corporativa):** Revoke API key, create new key, update Railway env var.
9. **Melhor Envio (base-corporativa):** Rotate client secret and API token, update Railway env vars.
10. **Django superuser (base-corporativa):** Change superuser password.
11. **JWT secrets (Digital-Signage-Platform + Bot_IqOption):** Generate new strong secrets, update env vars.

**Then P1:**

12. **Twilio (PayFlow-AI):** Revoke auth token if real, create new token.
13. **Chrome/Google session (MVP-linkedin-bot):** Sign out of all Chrome/Google sessions, re-authenticate.
14. **LinkedIn session (MVP-linkedin-bot):** Sign out of all LinkedIn sessions, change password, enable 2FA.
15. **IQ Option sessions (Bot_IqOption):** Terminate all active trading sessions.
16. **API-Football (Bet-IA-BOT):** Revoke API key, create new key.
17. **FlowTrack SECRET_KEY:** Set strong env var, remove weak fallback.

**Then P2:**

18. **Evolution API (LogiFlow):** Rotate key if real.
19. **News API + Alpha Vantage (API_Analyze):** Rotate keys if real.

### Post-Rotation Checklist

For each production credential rotated:
- [ ] New credential created at provider
- [ ] Old credential revoked at provider
- [ ] Deployment environment updated with new credential value
- [ ] Application redeployed (if required)
- [ ] Critical flow health-checked (login, payment, email, storage, etc.)
- [ ] Status updated in this matrix to ROTATED → REVOKED → VALIDATED

**Do NOT update this matrix with credential values. Only update the status field.**

---

## Phase 2A.7 Update — Runtime Reality Reclassification

**Date:** 2026-08-18
**Reference:** See `CREDENTIAL_RUNTIME_REALITY_AUDIT.md` for full evidence and `CREDENTIAL_EXECUTION_RUNBOOK.md` for execution steps.

### New Columns Added

Each item now has the following additional classifications:

| Column | Description |
|---|---|
| TYPE | CREDENTIAL, SESSION, PII, LOCAL_APP_SECRET |
| PROJECT_RUNTIME_STATUS | ACTIVE_PRODUCTION, ACTIVE_DEVELOPMENT, INACTIVE, ARCHIVED_IN_PRACTICE |
| REMEDIATION_CLASS | See allowed values below |
| OWNER | Leonardo, ICTSI/iTracker, or UNKNOWN |
| ACTIVE_DEPLOYMENT | YES / NO / STALE |
| NEXT_MANUAL_ACTION | Specific next step |

### Allowed Remediation Classes

- ROTATE_AND_REDEPLOY — Create new credential, deploy, verify, revoke old
- REVOKE_ONLY — Just revoke at provider, no replacement needed
- INVALIDATE_SESSION — Terminate active sessions
- CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS — Change password + terminate sessions
- OWNER_HANDOFF — Notify owner (former employer), do not rotate independently
- GENERATE_NEW_LOCAL_SECRET — Generate new app-internal secret if redeploying
- REMOVE_PII_FROM_HISTORY — PII to be purged from git history after credential rotation
- NOT_APPLICABLE — Not a real credential or not in use
- ALREADY_INVALIDATED_WITH_EVIDENCE — Confirmed already invalid
- UNKNOWN_REQUIRES_MANUAL_CHECK — Needs manual verification

### Updated Summary Table

| # | Repo | Provider | Type | TYPE | PROJECT_RUNTIME_STATUS | REMEDIATION_CLASS | OWNER | ACTIVE_DEPLOYMENT | NEXT_MANUAL_ACTION |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ProFlow | Django | SECRET_KEY | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Generate new secret, update Railway, redeploy |
| 2 | ProFlow | OpenAI | API key | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Revoke old key, create new, update Railway |
| 3 | ProFlow | Google | OAuth secret | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Reset OAuth secret in Google Cloud Console |
| 4 | ProFlow | GitHub | OAuth secret | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Generate new OAuth secret in GitHub |
| 5 | ProFlow | Mercado Pago | Access token | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Revoke and reissue in MP dashboard |
| 6 | ProFlow | Mercado Pago | Client secret | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Rotate in MP dashboard |
| 7 | ProFlow | Mercado Pago | Webhook secret | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Regenerate in MP dashboard |
| 8 | base-corporativa | Cloudflare R2 | Access key | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Create new R2 token, revoke old, update Railway |
| 9 | base-corporativa | Cloudflare R2 | Secret key | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Rotate alongside access key |
| 10 | base-corporativa | Mercado Pago | Access token | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Revoke and reissue in MP dashboard |
| 11 | base-corporativa | Mercado Pago | Public key | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Rotate in MP dashboard |
| 12 | base-corporativa | Melhor Envio | Client ID | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Check if rotatable or needs re-registration |
| 13 | base-corporativa | Melhor Envio | Client secret | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Rotate in Melhor Envio dashboard |
| 14 | base-corporativa | Melhor Envio | API token | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Revoke and reissue in Melhor Envio dashboard |
| 15 | base-corporativa | PostgreSQL | Database URL | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Rotate DB password in Railway |
| 16 | base-corporativa | Django | Superuser password | CREDENTIAL | ACTIVE_PRODUCTION | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | Leonardo | YES | Change via manage.py changepassword |
| 17 | base-corporativa | SendGrid | API key | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Revoke old, create new, update Railway |
| 18 | FinanceControl | AWS EC2 | RSA private key | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | NO | Check if EC2 active; if not, no action |
| 19 | Digital-Signage | MySQL | DB credentials | CREDENTIAL | ARCHIVED_IN_PRACTICE | OWNER_HANDOFF | ICTSI/iTracker | NO | Notify ICTSI IT/security |
| 20 | Digital-Signage | Application | JWT secret | LOCAL_APP_SECRET | ARCHIVED_IN_PRACTICE | OWNER_HANDOFF | ICTSI/iTracker | NO | Notify ICTSI; if decommissioned: no action; if running: handoff |
| 21 | Bot_IqOption | Mercado Pago | Access token | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | STALE | Revoke in MP dashboard |
| 22 | Bot_IqOption | Mercado Pago | Client secret | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | STALE | Revoke in MP dashboard |
| 23 | Bot_IqOption | Mercado Pago | Public key | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | STALE | Revoke in MP dashboard |
| 24 | Bot_IqOption | Mercado Pago | Client ID | CREDENTIAL | INACTIVE | UNKNOWN_REQUIRES_MANUAL_CHECK | Leonardo | STALE | Check if client ID needs rotation |
| 25 | Bot_IqOption | Django/App | SECRET_KEY | LOCAL_APP_SECRET | INACTIVE | GENERATE_NEW_LOCAL_SECRET | Leonardo | STALE | Generate new if redeploying |
| 26 | Bot_IqOption | IQ Option | JWT session tokens (197) | SESSION | INACTIVE | INVALIDATE_SESSION | Leonardo | STALE | Terminate all IQ Option sessions |
| 27 | Bot_IqOption | Application | Per-user API key files | CREDENTIAL | INACTIVE | UNKNOWN_REQUIRES_MANUAL_CHECK | Leonardo | STALE | Regenerate if auth system supports it |
| 28 | PayFlow-AI | Twilio | Auth token | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Revoke in Twilio console, create new |
| 29 | FlowTrack | Application | SECRET_KEY | LOCAL_APP_SECRET | ARCHIVED_IN_PRACTICE | OWNER_HANDOFF | ICTSI/iTracker | NO | Notify ICTSI/iTracker; if decommissioned: no action |
| 30 | FlowTrack | Application | Session/CSRF tokens (179) | SESSION | ARCHIVED_IN_PRACTICE | OWNER_HANDOFF | ICTSI/iTracker | NO | Notify ICTSI/iTracker; if decommissioned: sessions expired |
| 31 | MVP-linkedin-bot | Google Chrome | Browser session tokens | SESSION | INACTIVE | INVALIDATE_SESSION | Leonardo | NO | Sign out of all Chrome/Google sessions |
| 32 | MVP-linkedin-bot | LinkedIn | Session data in logs | SESSION | INACTIVE | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | Leonardo | NO | Sign out of all LinkedIn sessions, change password |
| 33 | MVP-linkedin-bot | CPF | PII | PII | INACTIVE | REMOVE_PII_FROM_HISTORY | Leonardo | NO | History sanitization after credential rotation |
| 34 | Bet-IA-BOT | API-Football | API key | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | NO | Revoke in API-Football dashboard |
| 35 | Portfolio | CNPJ card PDF | PII | PII | ACTIVE_PRODUCTION | REMOVE_PII_FROM_HISTORY | Leonardo | YES | History sanitization (repo was PUBLIC) |
| 36 | Portfolio | Articles of association PDF | PII | PII | ACTIVE_PRODUCTION | REMOVE_PII_FROM_HISTORY | Leonardo | YES | History sanitization (repo was PUBLIC) |
| 37 | LogiFlow | Evolution API | API key | CREDENTIAL | ACTIVE_PRODUCTION | ROTATE_AND_REDEPLOY | Leonardo | YES | Rotate key, update Vercel env var |
| 38 | API_Analyze | News API | API key | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | NO | Revoke if real in News API dashboard |
| 39 | API_Analyze | Alpha Vantage | API key | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | NO | Revoke if real in Alpha Vantage dashboard |
| 40 | MVP-linkedin-bot | Telegram | Bot token | CREDENTIAL | INACTIVE | REVOKE_ONLY | Leonardo | NO | Revoke via @BotFather, create new token |
| 41 | MVP-linkedin-bot | LinkedIn | Password (plaintext + encrypted) | CREDENTIAL | INACTIVE | CHANGE_PASSWORD_AND_INVALIDATE_SESSIONS | Leonardo | NO | Change LinkedIn password, invalidate sessions |

### Updated Totals (computed by validate_credential_matrix.py)

> **Invariant:** All totals are computed programmatically from the 41 canonical rows by `validate_credential_matrix.py`. Do NOT hand-maintain totals independently. Run `python3 validate_credential_matrix.py` after any edit to verify arithmetic.

#### By Type (sum = 41)

| Type | Count |
|---|---|
| CREDENTIAL | 31 |
| SESSION | 4 |
| LOCAL_APP_SECRET | 3 |
| PII | 3 |
| **Total** | **41** |

#### By Remediation Class (sum = 41)

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

#### By Project Runtime Status (sum = 41)

| Runtime Status | Total Items | Credentials | Sessions | Local App Secrets | PII |
|---|---|---|---|---|---|
| ACTIVE_PRODUCTION | 21 | 19 | 0 | 0 | 2 |
| INACTIVE | 16 | 12 | 2 | 1 | 1 |
| ARCHIVED_IN_PRACTICE | 4 | 1 | 1 | 2 | 0 |
| **Total** | **41** | **31** | **4** | **3** | **3** |

#### By Owner (sum = 41)

| Owner | Items |
|---|---|
| Leonardo | 37 |
| ICTSI/iTracker | 4 |
| **Total** | **41** |

---

## Phase 2A.9 — Post-Rotation Reconciliation Status (Updated)

**Date:** 2026-08-18
**Reference:** See `POST_ROTATION_RECONCILIATION.md` for full per-item evidence and readiness analysis.

> **Summary (Phase 2A.9):** Leonardo reports exposed credentials have been manually changed (OWNER_REPORTED). Leonardo has NOT yet provided explicit per-item attestation (OWNER_ATTESTED_COMPLETED). Absence of PROVIDER_VERIFIED is NOT a blocker per Phase 2A.9 evidence model. No credential values are listed.

### Reconciliation Status Per Item

| # | Evidence Level | Current Tree | Primary Readiness State |
|---|---|---|---|
| 1 | OWNER_REPORTED | CLEAN (PR #8 + #9 merged) | WAITING_OWNER_ATTESTATION |
| 2 | OWNER_REPORTED | CLEAN (PR #8 + #9 merged) | WAITING_OWNER_ATTESTATION |
| 3 | OWNER_REPORTED | CLEAN (PR #8 + #9 merged) | WAITING_OWNER_ATTESTATION |
| 4 | OWNER_REPORTED | CLEAN (PR #8 + #9 merged) | WAITING_OWNER_ATTESTATION |
| 5 | OWNER_REPORTED | CLEAN (PR #9 merged — MP creds removed) | WAITING_OWNER_ATTESTATION |
| 6 | OWNER_REPORTED | CLEAN (PR #8 + #9 merged) | WAITING_OWNER_ATTESTATION |
| 7 | OWNER_REPORTED | CLEAN (PR #8 + #9 merged) | WAITING_OWNER_ATTESTATION |
| 8 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 9 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 10 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 11 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 12 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 13 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 14 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 15 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 16 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 17 | OWNER_REPORTED | EXPOSURE (PR #1 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 18 | OWNER_REPORTED | CLEAN (PR #1 merged) | WAITING_OWNER_ATTESTATION |
| 19 | NOT_APPLICABLE (ICTSI-owned) | CLEAN | WAITING_OWNER_HANDOFF |
| 20 | NOT_APPLICABLE (ICTSI-owned) | CLEAN | WAITING_OWNER_HANDOFF |
| 21 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 22 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 23 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 24 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 25 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 26 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_SESSION_INVALIDATION |
| 27 | OWNER_REPORTED | EXPOSURE (PR #5 not merged) | CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION |
| 28 | OWNER_REPORTED | CLEAN (PR #1 merged) | WAITING_OWNER_ATTESTATION |
| 29 | NOT_APPLICABLE (ICTSI-owned) | CLEAN | WAITING_OWNER_HANDOFF |
| 30 | NOT_APPLICABLE (ICTSI-owned) | CLEAN | WAITING_OWNER_HANDOFF |
| 31 | OWNER_REPORTED | CLEAN (PR #2 merged) | WAITING_SESSION_INVALIDATION |
| 32 | OWNER_REPORTED | CLEAN (PR #2 merged) | WAITING_SESSION_INVALIDATION |
| 33 | NOT_APPLICABLE (PII) | CLEAN (PR #2 merged) | READY_FOR_HISTORY_SANITIZATION |
| 34 | OWNER_REPORTED | CLEAN (PR #1 merged) | WAITING_OWNER_ATTESTATION |
| 35 | NOT_APPLICABLE (PII) | CLEAN (PR #1 merged) | READY_FOR_HISTORY_SANITIZATION |
| 36 | NOT_APPLICABLE (PII) | CLEAN (PR #1 merged) | READY_FOR_HISTORY_SANITIZATION |
| 37 | OWNER_REPORTED | CLEAN (PR #1 merged — Phase 2A.9) | WAITING_OWNER_ATTESTATION |
| 38 | OWNER_REPORTED | CLEAN (PR #1 merged — Phase 2A.9) | WAITING_OWNER_ATTESTATION |
| 39 | OWNER_REPORTED | CLEAN (PR #1 merged — Phase 2A.9) | WAITING_OWNER_ATTESTATION |
| 40 | OWNER_REPORTED | CLEAN (PR #2 merged) | WAITING_OWNER_ATTESTATION |
| 41 | OWNER_REPORTED | CLEAN (PR #2 merged) | WAITING_SESSION_INVALIDATION |

### Reconciliation Totals (Phase 2A.9 Corrected)

| Evidence Level | Count |
|---|---|
| OWNER_REPORTED | 33 |
| OWNER_ATTESTED_COMPLETED | 0 |
| NOT_APPLICABLE (PII) | 3 |
| NOT_APPLICABLE (ICTSI-owned) | 4 |
| PROVIDER_VERIFIED | 0 (not a blocker per Phase 2A.9 model) |
| RUNTIME_VERIFIED | 0 (not a blocker per Phase 2A.9 model) |

| Current Tree Status | Count |
|---|---|
| CLEAN | 24 |
| EXPOSURE (PR #1 not merged — base-corporativa) | 10 |
| EXPOSURE (PR #5 not merged — Bot_IqOption) | 7 |

| Primary Readiness State | Count |
|---|---|
| READY_FOR_HISTORY_SANITIZATION | 3 |
| WAITING_OWNER_ATTESTATION | 14 |
| CURRENT_TREE_BLOCKER + WAITING_OWNER_ATTESTATION | 16 |
| CURRENT_TREE_BLOCKER + WAITING_SESSION_INVALIDATION | 1 |
| WAITING_SESSION_INVALIDATION | 3 |
| WAITING_OWNER_HANDOFF | 4 |
| **Total** | **41** |

> **Invariant:** SUM(PRIMARY_READINESS_COUNTS) == 41. Each canonical ID 1..41 has exactly ONE primary readiness state.
