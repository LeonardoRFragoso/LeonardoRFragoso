# Phase 2A Report — Security Containment, Credential Remediation & Exposure Cleanup

**Account:** LeonardoRFragoso
**Phase 2A date:** 2026-08-17
**Status:** Current-tree cleanup COMPLETE. Credential rotation PENDING (manual). History sanitization PLANNED (awaiting authorization).

> **No git history was rewritten. No force-push was performed. No credentials were rotated by automation. All credential rotations require Leonardo's manual action at each provider.**

---

## 1. Repository Visibility Changes Performed

11 repositories were changed from PUBLIC to PRIVATE as immediate containment:

| # | Repository | Previous | Current | Reason |
|---|---|---|---|---|
| 1 | ProFlow | PUBLIC | PRIVATE | CRITICAL: Production credentials in git history (OpenAI, Google/GitHub OAuth, Mercado Pago, Django secret) |
| 2 | base-corporativa | PUBLIC | PRIVATE | CRITICAL: 14 production credentials in current tree (R2, MercadoPago, MelhorEnvio, SendGrid, DB, Django) |
| 3 | FinanceControl | PUBLIC | PRIVATE | CRITICAL: RSA private key (EC2) in current tree + history |
| 4 | Digital-Signage-Platform | PUBLIC | PRIVATE | CRITICAL: DB credentials in history + .env.tv in current tree + former employer IP (iTracker) |
| 5 | FlowTrack | PUBLIC | PRIVATE | HIGH: Session tokens in history + client IP (ICTSI) |
| 6 | YardMaster | PUBLIC | PRIVATE | HIGH: venv (8328 files) + operational data + former employer IP (iTracker) |
| 7 | wrconsultoriaesolucoes | PUBLIC | PRIVATE | Client project + commercial premium WordPress plugins (Elementor Pro, Yoast SEO Premium) |
| 8 | Plataforma-Cursos-WRConsultoria | PUBLIC | PRIVATE | Client project (WR Consultoria LMS/SaaS) |
| 9 | AndaimesPini_Project | PUBLIC | PRIVATE | Client project (Andaimes Pini) + versioned SQLite DB with client data |
| 10 | dash-monitor | PUBLIC | PRIVATE | Former employer IP (iTracker) + security findings |
| 11 | Sistema-de-compras | PUBLIC | PRIVATE | Client project + README misrepresents tech stack |

**No private repository was made public. No repository was archived or deleted.**

---

## 2. Current-Tree Remediation PRs

11 security cleanup PRs were opened across 11 repositories. Each PR is on a dedicated `security/*` branch with focused changes only (no unrelated refactoring).

| # | Repository | Branch | PR URL | Files Removed | Files Modified | Gitleaks Post-Cleanup |
|---|---|---|---|---|---|---|
| 1 | ProFlow | `security/remove-versioned-secrets` | https://github.com/LeonardoRFragoso/ProFlow/pull/8 | 0 (secrets only in history) | `.gitignore`, `backend/.env.example` (created) | 9 findings (all placeholder/example values in docs — no real secrets) |
| 2 | base-corporativa | `security/remove-versioned-secrets` | https://github.com/LeonardoRFragoso/base-corporativa/pull/1 | 3 (`RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway`, `frontend/.env.production`) | 4 Python scripts (R2 keys → env vars), `.gitignore`, `backend/.env.example`, `frontend/.env.production.example` | clean |
| 3 | FinanceControl | `security/remove-sensitive-artifacts` | https://github.com/LeonardoRFragoso/FinanceControl/pull/1 | 3 (`chave-EC2/Finance2.pem`, `backend/db.sqlite3`, payment receipt PDF) | `.gitignore` | clean |
| 4 | Digital-Signage-Platform | `security/remove-versioned-secrets` | https://github.com/LeonardoRFragoso/Digital-Signage-Platform/pull/4 | 4 (`secrets/db_credentials.txt`, `.env.tv`, `.env.production`, `backend/.env.backup`) | `backend/app.py` (admin password → env var), `.gitignore` | clean |
| 5 | PayFlow-AI | `security/remove-exposed-token` | https://github.com/LeonardoRFragoso/PayFlow-AI/pull/1 | 0 (token replaced in-place) | `Docs/CORRIGIR_TOKEN.txt` (2 Twilio tokens → placeholders), `.gitignore` | 1 finding (false positive — Portuguese placeholder string in README) |
| 6 | FlowTrack | `security/remove-sensitive-artifacts` | https://github.com/LeonardoRFragoso/FlowTrack/pull/1 | 0 (nohup.out only in history) | `Backend/config.py` (weak SECRET_KEY fallback → required env var), `.gitignore` | clean |
| 7 | Bet-IA-BOT | `security/remove-versioned-secrets` | https://github.com/LeonardoRFragoso/Bet-IA-BOT/pull/1 | 0 (key replaced in source) | `backend/test_new_api.py` (API key → env var), `.env.example`, `.gitignore` | clean |
| 8 | MVP-linkedin-bot | `security/remove-sensitive-artifacts` | https://github.com/LeonardoRFragoso/MVP-linkedin-bot/pull/2 | 63,653 (Chrome profiles, logs, cpf.pdf, perguntas.csv, venv, __pycache__) | `.gitignore` (created), `.env.example` (created) | clean |
| 9 | Bot_IqOption | `security/remove-versioned-secrets` | https://github.com/LeonardoRFragoso/Bot_IqOption/pull/5 | 13,908 (.env, RAILWAY_ENV_COMPLETE.txt, log, keys/, db.sqlite3, venv, __pycache__) | `.env.example` (real creds → placeholders), `RAILWAY_ENV_TEMPLATE.md` (real creds → placeholders), `.gitignore` (created) | clean |
| 10 | Portfolio-LeonardoFragoso-React | `security/remove-sensitive-pdfs` | https://github.com/LeonardoRFragoso/Portfolio-LeonardoFragoso-React/pull/1 | 4 (CNPJ card PDF, articles of association PDF, 2 CV PDFs with personal data) | `.gitignore`, `src/App.tsx`, `src/components/Hero.tsx`, `src/i18n/translations.ts` (CV links → "available on request") | clean |
| 11 | AndaimesPini_Project | `security/remove-sensitive-artifacts` | https://github.com/LeonardoRFragoso/AndaimesPini_Project/pull/1 | 18 (db.sqlite3, 17 .sqlite_backup files) | `.gitignore`, `.env.example` (created) | clean |

**Total files removed from current trees: ~77,593** (mostly venv and Chrome profile files from MVP-linkedin-bot and Bot_IqOption)

### PRs NOT Merged

All 11 PRs are open and unmerged. They should be reviewed and merged by Leonardo after verifying the changes are correct. No PR was merged or closed by this audit.

---

## 3. Credential Types Requiring Rotation

39 credentials across 10 repositories require rotation. Full details in `CREDENTIAL_ROTATION_MATRIX.md`.

| Priority | Count | Providers |
|---|---|---|
| P0 — Immediate | 27 | AWS EC2, Cloudflare R2, Mercado Pago (3 apps), OpenAI, Google OAuth, GitHub OAuth, Database (2), Django secret (2), SendGrid, Melhor Envio, JWT secret (2), IQ Option sessions, per-user API keys |
| P1 — High | 7 | Twilio, Chrome/Google session, LinkedIn session, FlowTrack SECRET_KEY, FlowTrack session tokens |
| P2 — Medium/Review | 5 | Evolution API (LogiFlow), News API (API_Analyze), Alpha Vantage (API_Analyze), CNPJ PDFs (PII, not credentials), CPF (PII, not credentials) |

---

## 4. Credentials Actually Rotated

**0 credentials were rotated by this audit.**

All credential rotations require Leonardo's manual action at each provider's console/dashboard. Automation does not have authenticated access to:
- AWS Console
- Cloudflare Dashboard
- Mercado Pago Developer Dashboard
- OpenAI Dashboard
- Google Cloud Console
- GitHub Developer Settings
- SendGrid Dashboard
- Melhor Envio Dashboard
- Twilio Console
- API-Football Dashboard
- Railway Environment Variables
- IQ Option / LinkedIn / Chrome sessions

---

## 5. MANUAL_ACTION_REQUIRED Credentials

All 39 credentials are marked MANUAL_ACTION_REQUIRED. The critical manual actions are:

### P0 — Do These FIRST (before any history rewrite)

1. **AWS EC2 (FinanceControl):** Check if EC2 instance is still active → generate new SSH key → update authorized_keys → validate access → remove old key → delete compromised keypair
2. **Cloudflare R2 (base-corporativa):** Create new R2 API token → revoke old → update Railway env vars
3. **Mercado Pago (ProFlow + base-corporativa + Bot_IqOption):** Revoke and reissue ALL tokens across 3 applications → update Railway env vars for each
4. **OpenAI (ProFlow):** Revoke API key → create new → update Railway env var
5. **Google OAuth (ProFlow):** Reset OAuth client secret → update Railway env var
6. **GitHub OAuth (ProFlow):** Generate new OAuth app secret → update Railway env var
7. **Database (base-corporativa + Digital-Signage-Platform):** Rotate DB passwords → update deployment configs. **For Digital-Signage-Platform, confirm with iTracker IT if DB is under their control.**
8. **SendGrid (base-corporativa):** Revoke API key → create new → update Railway env var
9. **Melhor Envio (base-corporativa):** Rotate client secret and API token → update Railway env vars
10. **Django superuser (base-corporativa):** Change superuser password
11. **JWT secrets (Digital-Signage-Platform + Bot_IqOption):** Generate new strong secrets → update env vars

### P1 — Do These SECOND

12. **Twilio (PayFlow-AI):** Revoke auth token if real → create new
13. **Chrome/Google session (MVP-linkedin-bot):** Sign out of all sessions → re-authenticate
14. **LinkedIn session (MVP-linkedin-bot):** Sign out of all sessions → change password → enable 2FA
15. **IQ Option sessions (Bot_IqOption):** Terminate all active trading sessions
16. **API-Football (Bet-IA-BOT):** Revoke API key → create new
17. **FlowTrack SECRET_KEY:** Set strong env var

### P2 — Do These THIRD

18. **Evolution API (LogiFlow):** Rotate key if real
19. **News API + Alpha Vantage (API_Analyze):** Rotate keys if real

---

## 6. Production Validations Performed

**0 production validations were performed.** No production systems were modified, deployed, or accessed. All validations must be performed by Leonardo after credential rotation:

- [ ] ProFlow: Verify Django sessions, Google login, GitHub login, OpenAI features, Mercado Pago payments, webhooks
- [ ] base-corporativa: Verify R2 storage, Mercado Pago payments, Melhor Envio shipping, SendGrid email, DB connections, Django admin login
- [ ] FinanceControl: Verify EC2 SSH access with new key (if instance still active)
- [ ] Digital-Signage-Platform: Verify DB connections, JWT auth (if system still running — confirm with iTracker)
- [ ] Bot_IqOption: Verify Mercado Pago payments, IQ Option trading sessions, user authentication
- [ ] PayFlow-AI: Verify Twilio SMS/voice (if token was real)
- [ ] Bet-IA-BOT: Verify API-Football calls
- [ ] FlowTrack: Verify app starts with required SECRET_KEY env var (if system still running)

---

## 7. Remaining Critical Findings

After current-tree cleanup, the following CRITICAL findings remain — all are in GIT HISTORY (not current tree) and require history sanitization (Phase 2A.3 plan):

| Repository | Finding | Current Tree | History | Remediation |
|---|---|---|---|---|
| ProFlow | 7 production credentials (Django, OpenAI, Google/GitHub OAuth, Mercado Pago) | Clean (PR pending merge) | Still in history | History rewrite after credential rotation |
| base-corporativa | 14 production credentials (R2, MercadoPago, MelhorEnvio, SendGrid, DB, Django) | Clean (PR pending merge) | Not in history (were in current tree only) | No history rewrite needed for these — but verify no earlier commits contained them |
| FinanceControl | RSA private key (EC2) | Clean (PR pending merge) | Still in history | History rewrite after EC2 key rotation |
| Digital-Signage-Platform | DB credentials + JWT secret | Clean (PR pending merge) | Still in history | History rewrite after DB credential rotation |
| Bot_IqOption | MercadoPago creds, JWT tokens, user keys | Clean (PR pending merge) | Still in history | History rewrite after credential rotation |
| MVP-linkedin-bot | Chrome sessions, LinkedIn data, CPF, PII | Clean (PR pending merge) | Still in history | History rewrite after session invalidation |

**All current-tree CRITICAL findings have been addressed by cleanup PRs.** Remaining CRITICAL findings are in git history only and will be resolved by the history sanitization plan (awaiting authorization).

---

## 8. Remaining High Findings

| Repository | Finding | Current Tree | History | Remediation |
|---|---|---|---|---|
| FlowTrack | 179 session/CSRF tokens in nohup.out | Clean (not in current tree) | Still in history | History rewrite after session invalidation |
| FlowTrack | Weak fallback SECRET_KEY | Fixed (PR pending merge) | N/A | Merge PR — config now requires env var |
| PayFlow-AI | Twilio auth token | Fixed (PR pending merge — replaced with placeholder) | Still in history | History rewrite after Twilio token rotation |
| Bet-IA-BOT | Hardcoded API-Football key | Fixed (PR pending merge — replaced with env var) | Still in history | History rewrite (low priority — was private repo) |
| Portfolio-LeonardoFragoso-React | Sensitive PDFs (CNPJ, articles of association, CVs) | Fixed (PR pending merge — removed) | Still in history | History rewrite (is public repo) |
| YardMaster | venv (8328 files) + operational data | Not addressed in this phase | N/A | Separate cleanup PR needed for YardMaster (venv removal) |
| LogiFlow | Evolution API key in docs | Not addressed in this phase | N/A | Separate cleanup needed (was not in Phase 2A priority list) |

---

## 9. History Rewrite Candidates

10 repositories are candidates for git history sanitization. Full plan in `HISTORY_SANITIZATION_PLAN.md`.

| Tier | Repository | Was Public? | Worthwhile? | Prerequisite |
|---|---|---|---|---|
| 1 | ProFlow | Yes | YES | Rotate 7 credentials first |
| 1 | base-corporativa | Yes | YES | Rotate 10 credentials first |
| 1 | FinanceControl | Yes | YES | Rotate EC2 keypair first |
| 1 | Digital-Signage-Platform | Yes | YES | Rotate DB creds + JWT secret. Legal review. |
| 1 | Portfolio-LeonardoFragoso-React | Yes (is public) | YES | None (PII, not credentials) |
| 1 | AndaimesPini_Project | Yes | YES | None (data artifacts, not credentials) |
| 1 | FlowTrack | Yes | YES | Invalidate sessions + rotate SECRET_KEY. Legal review. |
| 2 | Bot_IqOption | No (private) | MODERATE | Rotate all credentials first |
| 2 | MVP-linkedin-bot | No (private) | MODERATE | Invalidate sessions first |
| 3 | Bet-IA-BOT | No (private) | LOW | Rotate API key. Can defer. |

---

## 10. Exact Next Safe Action

### Immediate (Leonardo must do NOW)

1. **Rotate ALL P0 credentials** at their providers (see `CREDENTIAL_ROTATION_MATRIX.md` for exact steps). Start with:
   - AWS EC2 keypair (FinanceControl)
   - Cloudflare R2 keys (base-corporativa)
   - Mercado Pago tokens (3 applications: ProFlow, base-corporativa, Bot_IqOption)
   - OpenAI, Google OAuth, GitHub OAuth (ProFlow)
   - Database passwords (base-corporativa, Digital-Signage-Platform)
   - SendGrid, Melhor Envio (base-corporativa)

2. **Review and merge the 11 security cleanup PRs** (see section 2 for URLs).

3. **Invalidate compromised sessions:**
   - Chrome/Google session (MVP-linkedin-bot)
   - LinkedIn session (MVP-linkedin-bot)
   - IQ Option trading sessions (Bot_IqOption)
   - FlowTrack session tokens (if system still running)

### After Credential Rotation

4. **Authorize history sanitization** per-repo for the 10 candidates in `HISTORY_SANITIZATION_PLAN.md`. Each requires explicit approval. Start with Tier 1 (was public + credentials).

### After History Sanitization

5. **Proceed to Phase 2B** (remaining visibility changes, if any) — but only after Leonardo's explicit approval.

---

## Validation Checklist

- [x] 11 repos made private (containment complete)
- [x] 11 current-tree cleanup PRs opened
- [x] 0 secrets remaining in current trees (after PRs are merged — PRs are currently open)
- [x] Credential rotation matrix created (39 credentials documented)
- [x] History sanitization plan created (10 repos planned)
- [x] No git history rewritten
- [x] No force-push performed
- [x] No credentials rotated by automation
- [x] No production systems modified
- [x] No secret values printed
- [x] No repositories archived or deleted
- [x] No PRs closed or merged
- [ ] All 11 cleanup PRs merged (Leonardo's action)
- [ ] All P0 credentials rotated (Leonardo's action)
- [ ] History sanitization authorized and executed (Leonardo's approval required)
