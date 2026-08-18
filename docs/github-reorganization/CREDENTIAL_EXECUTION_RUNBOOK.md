# Credential Execution Runbook — Phase 2A.7

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Status:** PLAN ONLY — No actions executed. No credentials rotated. No sessions invalidated.

> **CRITICAL:** This runbook organizes future manual credential remediation in safe batches. Do NOT execute any step until you have read the `CREDENTIAL_RUNTIME_REALITY_AUDIT.md` and confirmed the classifications. No credential values are listed.

## Execution Principles

1. **Rotate BEFORE history rewrite.** Credentials must be rotated at the provider before any git history sanitization.
2. **Active services first.** Rotate credentials for ACTIVE_PRODUCTION services before inactive ones.
3. **Test after each rotation.** Verify the service works with the new credential before revoking the old one.
4. **Revoke after replacement.** Only revoke the old credential after the new one is confirmed working.
5. **Former-employer: handoff, don't rotate.** For ICTSI/iTracker systems, notify the owner — do not rotate independently.
6. **Never log secrets.** Do not paste credential values into tickets, chat, or documentation.

---

## Batch 1 — ACTIVE_PRODUCTION Critical (Do First)

### 1.1 ProFlow (7 credentials — all ROTATE_AND_REDEPLOY)

**Context:** SaaS in production at proflow.pro. Railway deployment active. Repo was PUBLIC when secrets were committed — all are COMPROMISED.

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | Django | `SECRET_KEY` | 1. Generate new strong secret. 2. Update Railway env var. 3. Redeploy. 4. Verify users can log in (old sessions invalidated). 5. Revoke old secret (it's just a string — replacing it revokes it). |
| 2 | OpenAI | `OPENAI_API_KEY` | 1. Go to OpenAI dashboard. 2. Create new API key. 3. Update Railway env var. 4. Redeploy. 5. Verify AI features work. 6. Revoke old key in OpenAI dashboard. 7. Verify old key fails. |
| 3 | Google OAuth | `GOOGLE_OAUTH_CLIENT_SECRET` | 1. Go to Google Cloud Console → APIs & Services → Credentials. 2. Reset OAuth client secret. 3. Update Railway env var. 4. Redeploy. 5. Verify Google login works. 6. Verify old secret fails. |
| 4 | GitHub OAuth | `GITHUB_OAUTH_CLIENT_SECRET` | 1. Go to GitHub → Settings → Developer settings → OAuth Apps. 2. Generate new client secret. 3. Update Railway env var. 4. Redeploy. 5. Verify GitHub login works. 6. Verify old secret fails. |
| 5 | Mercado Pago | `MERCADOPAGO_ACCESS_TOKEN` | 1. Go to MP developer dashboard. 2. Revoke and reissue access token. 3. Update Railway env var. 4. Redeploy. 5. Verify payment flow works. 6. Verify old token fails. |
| 6 | Mercado Pago | `MERCADOPAGO_CLIENT_SECRET` | 1. Go to MP dashboard. 2. Rotate client secret. 3. Update Railway env var. 4. Redeploy. 5. Verify payment auth works. |
| 7 | Mercado Pago | `MERCADOPAGO_WEBHOOK_SECRET` | 1. Go to MP dashboard. 2. Regenerate webhook secret. 3. Update Railway env var. 4. Redeploy. 5. Verify webhook signature validation works. |

### 1.2 base-corporativa (10 credentials — all ROTATE_AND_REDEPLOY)

**Context:** E-commerce in production at basecorporativa.store. Railway deployment active. Credentials still in current tree (PR #1 not yet merged).

> **IMPORTANT:** Merge PR #1 ONLY AFTER setting all env vars in Railway. Merging without env vars will break production.

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | Cloudflare R2 | `R2_ACCESS_KEY` + `R2_SECRET_KEY` | 1. Go to Cloudflare dashboard → R2 → API tokens. 2. Create new API token. 3. Update Railway env vars (both key and secret). 4. Verify R2 storage operations work. 5. Revoke old token. |
| 2 | Mercado Pago | `MERCADOPAGO_ACCESS_TOKEN` | 1. Go to MP developer dashboard. 2. Revoke and reissue. 3. Update Railway env var. 4. Verify payment flow. 5. Verify old token fails. |
| 3 | Mercado Pago | `MERCADOPAGO_PUBLIC_KEY` | 1. Go to MP dashboard. 2. Rotate public key. 3. Update Railway env var. 4. Verify frontend payment rendering. |
| 4 | Melhor Envio | `MELHOR_ENVIO_CLIENT_ID` | 1. Check Melhor Envio dashboard if client ID can be rotated. 2. If not, may need app re-registration. 3. Update Railway env var. 4. Verify shipping quote flow. |
| 5 | Melhor Envio | `MELHOR_ENVIO_CLIENT_SECRET` | 1. Go to Melhor Envio dashboard. 2. Rotate client secret. 3. Update Railway env var. 4. Verify shipping auth. |
| 6 | Melhor Envio | `MELHOR_ENVIO_API_TOKEN` | 1. Go to Melhor Envio dashboard. 2. Revoke and reissue API token. 3. Update Railway env var. 4. Verify shipping API calls. |
| 7 | PostgreSQL | `DATABASE_URL` | 1. Go to Railway database settings. 2. Rotate DB password. 3. Update DATABASE_URL env var. 4. Verify DB connections. |
| 8 | Django | `DJANGO_SUPERUSER_PASSWORD` | 1. Use `python manage.py changepassword <username>` or Django admin. 2. Verify admin login with new password. |
| 9 | SendGrid | `SENDGRID_API_KEY` | 1. Go to SendGrid dashboard. 2. Revoke old key, create new key. 3. Update Railway env var. 4. Verify email sending. 5. Verify old key fails. |

**After all env vars are set:** Merge PR #1. Verify production still works.

### 1.3 PayFlow-AI (1 credential — ROTATE_AND_REDEPLOY if Twilio used)

**Context:** Vercel production active. Repo is PUBLIC. Twilio token in history.

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | Twilio | `TWILIO_AUTH_TOKEN` | 1. Check if Twilio is actually used in current deployment. 2. If yes: go to Twilio console, revoke auth token, create new token, update Vercel env var, verify SMS/voice. 3. If no: REVOKE_ONLY — just revoke the token in Twilio console. |

### 1.4 LogiFlow (1 credential — ROTATE_AND_REDEPLOY)

**Context:** Vercel production active (3 apps). Repo is PUBLIC. Evolution API key in docs.

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | Evolution API | `EVOLUTION_API_KEY` | 1. Go to Evolution API dashboard. 2. Rotate key. 3. Update Vercel env var. 4. Verify WhatsApp integration. 5. Update docs with placeholder (not real key). |

---

## Batch 2 — INACTIVE Services (Revoke Only)

### 2.1 FinanceControl (1 credential — REVOKE_ONLY)

| Order | Provider | Type | Steps |
|---|---|---|---|
| 1 | AWS EC2 | RSA private key | 1. Check if EC2 instance(s) still active in AWS console. 2. If active: generate new SSH key, update authorized_keys, validate access, remove old key, delete compromised keypair. 3. If terminated: no action needed (keypair useless without instance). |

### 2.2 Bet-IA-BOT (1 credential — REVOKE_ONLY)

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | API-Football | `API_FOOTBALL_KEY` | 1. Go to API-Football dashboard. 2. Revoke key. 3. No replacement needed (project inactive). |

### 2.3 Bot_IqOption (5 credentials — REVOKE_ONLY / GENERATE_NEW_LOCAL_SECRET)

**Context:** Railway deployments stale (last 2026-06-11). Project appears inactive.

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | Mercado Pago | `MERCADOPAGO_ACCESS_TOKEN` | 1. Go to MP dashboard. 2. Revoke token. 3. No replacement unless redeploying. |
| 2 | Mercado Pago | `MERCADOPAGO_CLIENT_SECRET` | 1. Go to MP dashboard. 2. Revoke. 3. No replacement unless redeploying. |
| 3 | Mercado Pago | `MERCADOPAGO_PUBLIC_KEY` | 1. Go to MP dashboard. 2. Revoke. 3. No replacement unless redeploying. |
| 4 | Mercado Pago | `MERCADOPAGO_CLIENT_ID` | 1. Check if client ID needs rotation. 2. If yes, re-register app. 3. If no, no action. |
| 5 | Django/App | `SECRET_KEY` | 1. If redeploying: generate new strong secret. 2. If not redeploying: no action. |

### 2.4 API_Analyze (2 credentials — REVOKE_ONLY)

| Order | Provider | Env Var | Steps |
|---|---|---|---|
| 1 | News API | `NEWS_API_KEY` | 1. Go to News API dashboard. 2. Revoke key if real. 3. Replace .env.example with placeholder. |
| 2 | Alpha Vantage | `ALPHA_VANTAGE_API_KEY` | 1. Go to Alpha Vantage dashboard. 2. Revoke key if real. 3. Replace .env.example with placeholder. |

---

## Batch 3 — Sessions (Invalidate)

### 3.1 MVP-linkedin-bot (3 items)

| Order | Provider | Type | Steps |
|---|---|---|---|
| 1 | LinkedIn | Password + sessions | 1. Go to LinkedIn → Settings → Security. 2. Change password. 3. Sign out of all sessions. 4. Enable 2FA if not already. 5. Re-authenticate only trusted devices. |
| 2 | LinkedIn | Session data in logs | Covered by step 1 above (sign out of all sessions). |
| 3 | Google Chrome | Browser session tokens | 1. Sign out of Chrome/Google in all sessions. 2. Re-authenticate. 3. The committed Chrome profile allows session hijacking — treat as compromised. |
| 4 | Telegram | Bot token | 1. Open Telegram, message @BotFather. 2. Use `/revoke` or `/token` to revoke old bot token and get new one. 3. Update `TELEGRAM_BOT_TOKEN` env var. |

### 3.2 Bot_IqOption (1 item)

| Order | Provider | Type | Steps |
|---|---|---|---|
| 1 | IQ Option | JWT trading session tokens (197) | 1. Log into IQ Option. 2. Terminate all active sessions (Settings → Security → Active Sessions). 3. Change password if warranted. 4. Re-authenticate only trusted devices. |

---

## Batch 4 — Former-Employer Handoff (Do NOT Rotate Independently)

### 4.1 Digital-Signage-Platform (ICTSI/iTracker)

| Order | Item | Steps |
|---|---|---|
| 1 | Identify ICTSI contact | 1. Find current IT/security contact at ICTSI/iTracker. 2. Prepare notification (without secret values). |
| 2 | Notify ICTSI | 1. Notify that DB credentials and JWT secret for the Digital-Signage-Platform were committed to GitHub. 2. Provide repository name and affected file paths (not values). 3. Request they rotate the MySQL DB user/root passwords and JWT secret. |
| 3 | Record handoff | 1. Update CREDENTIAL_ROTATION_MATRIX.md with handoff status. 2. If ICTSI confirms rotation, update status to ROTATED by OWNER. |
| 4 | After handoff | If system is confirmed decommissioned, update classification to ALREADY_INVALIDATED_WITH_EVIDENCE. |

### 4.2 FlowTrack (ICTSI — Porto do Rio de Janeiro)

| Order | Item | Steps |
|---|---|---|
| 1 | Identify ICTSI contact | 1. Find current IT/security contact at ICTSI (Porto do Rio). 2. Prepare notification. |
| 2 | Notify ICTSI | 1. Notify that SECRET_KEY and session/CSRF tokens for FlowTrack were committed to GitHub. 2. Provide repository name and affected file paths. 3. Request they rotate the SECRET_KEY and invalidate active sessions. |
| 3 | Record handoff | 1. Update CREDENTIAL_ROTATION_MATRIX.md with handoff status. 2. If ICTSI confirms rotation, update status. |
| 4 | After handoff | If system is confirmed decommissioned, update classification. |

---

## Batch 5 — PII History Sanitization (After All Credentials Rotated)

> **DO NOT START until Batch 1-4 are complete.** History rewrite before credential rotation is pointless.

### PII Items (REMOVE_PII_FROM_HISTORY)

| Repo | Items | Steps |
|---|---|---|
| MVP-linkedin-bot | CPF, full name, phone, address, salary, cover letter, 6 CV PDFs, 4 CSVs, 26 screenshots | Use git-filter-repo to purge affected files and patterns from all history. See HISTORY_SANITIZATION_PLAN.md. |
| Portfolio | CNPJ card PDF, articles of association PDF | Use git-filter-repo to purge public/Docs/*.pdf from all history. Repo was PUBLIC. |
| All repos with credentials | All credential values in history | Use git-filter-repo --replace-text to replace each known secret value with REDACTED. |

---

## Post-Rotation Checklist

For each credential rotated:
- [ ] New credential created at provider
- [ ] Old credential revoked at provider
- [ ] Deployment environment updated with new credential value
- [ ] Application redeployed (if required)
- [ ] Critical flow health-checked (login, payment, email, storage, etc.)
- [ ] Old credential verified as unusable
- [ ] Status updated in CREDENTIAL_ROTATION_MATRIX.md

For each session invalidated:
- [ ] All active sessions terminated
- [ ] Password changed (if applicable)
- [ ] 2FA enabled/confirmed (if available)
- [ ] Re-authentication completed on trusted devices only

For each owner handoff:
- [ ] Owner/contact identified
- [ ] Notification sent (without secret values)
- [ ] Owner confirmed receipt
- [ ] Owner confirmed rotation/revocation
- [ ] Status updated in CREDENTIAL_ROTATION_MATRIX.md

---

## First Manual Actions (Ordered by Risk)

1. **ProFlow: Rotate Django SECRET_KEY** — active production, was PUBLIC, session hijacking possible
2. **ProFlow: Rotate OpenAI API key** — active production, was PUBLIC, unauthorized API usage possible
3. **ProFlow: Rotate Mercado Pago tokens** — active production, was PUBLIC, payment fraud possible
4. **ProFlow: Rotate Google + GitHub OAuth secrets** — active production, was PUBLIC, account takeover possible
5. **base-corporativa: Rotate R2 keys** — active production, credentials in current tree
6. **base-corporativa: Rotate Mercado Pago tokens** — active production, credentials in current tree
7. **base-corporativa: Rotate DB password** — active production, credentials in current tree
8. **base-corporativa: Rotate SendGrid + Melhor Envio** — active production, credentials in current tree
9. **MVP-linkedin-bot: Change LinkedIn password** — was in git history, account takeover possible
10. **MVP-linkedin-bot: Revoke Telegram bot token** — was in git history, bot hijacking possible
11. **MVP-linkedin-bot: Invalidate Chrome/Google sessions** — browser profile committed, session hijacking possible
12. **PayFlow-AI: Rotate Twilio token** — active production, was PUBLIC
13. **LogiFlow: Rotate Evolution API key** — active production, repo is PUBLIC
14. **Bot_IqOption: Revoke Mercado Pago tokens** — inactive but tokens are live
15. **Bot_IqOption: Terminate IQ Option sessions** — 197 session tokens exposed
16. **FinanceControl: Check/revoke EC2 keypair** — inactive but keypair may still work
17. **Bet-IA-BOT: Revoke API-Football key** — inactive
18. **API_Analyze: Revoke News API + Alpha Vantage keys** — inactive
19. **Digital-Signage-Platform: Notify ICTSI** — former employer handoff
20. **FlowTrack: Notify ICTSI** — former employer handoff
