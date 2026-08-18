# Git History Sanitization Plan — Phase 2A (Updated Phase 2A.8)

**Account:** LeonardoRFragoso
**Phase 2A date:** 2026-08-17
**Phase 2A.7 update:** 2026-08-18
**Phase 2A.8 update:** 2026-08-18
**Status:** PLAN ONLY — **DO NOT EXECUTE without Leonardo's explicit per-repo authorization**

> **CRITICAL:** History rewriting is DESTRUCTIVE and irreversible. It rewrites all commit SHAs, breaks forks, breaks open PRs, and requires force-push. This document is a PLAN only. No history rewrite has been performed or will be performed without explicit authorization.

## Phase 2A.8 Update — Post-Rotation Reconciliation

Leonardo reports exposed credentials have been manually changed. Post-rotation reconciliation (see `POST_ROTATION_RECONCILIATION.md`) determined:

1. **3 of 41 items READY for history sanitization** (PII items: 33, 35, 36 — removal IS the remediation)
2. **38 of 41 items still BLOCKED** for one or more reasons:
   - Provider-side revocation not independently verified (OWNER_REPORTED only)
   - Current-tree exposure not cleaned (PRs not merged or not created)
   - Session invalidation not independently verified
   - Owner handoff to ICTSI not completed
3. **Only Portfolio-LeonardoFragoso-React is READY** for history sanitization (PII-only, current tree clean)
4. **11 of 12 repositories are BLOCKED** — see per-repository table below

### Per-Repository History Sanitization Readiness

| Repository | Current Tree | History Sanitization | Blocker |
|---|---|---|---|
| ProFlow | EXPOSURE in docs | **BLOCKED** | Docs files still contain SendGrid/MP credentials; follow-up cleanup PR needed |
| base-corporativa | EXPOSURE (PR #1 open) | **BLOCKED** | PR #1 not merged; old credentials still in current tree |
| FinanceControl | CLEAN | **BLOCKED** | Provider-side revocation of EC2 key not verified |
| Digital-Signage-Platform | CLEAN | **BLOCKED** | Owner handoff to ICTSI not completed |
| Bot_IqOption | EXPOSURE (PR #5 open) | **BLOCKED** | PR #5 not merged; Railway auto-deploy unconfirmed; old credentials still in current tree |
| PayFlow-AI | CLEAN | **BLOCKED** | Provider-side revocation of Twilio token not verified |
| FlowTrack | CLEAN | **BLOCKED** | Owner handoff to ICTSI not completed |
| MVP-linkedin-bot | CLEAN | **BLOCKED** | Session invalidation not independently verified; provider revocation not verified |
| Bet-IA-BOT | CLEAN | **BLOCKED** | Provider-side revocation of API-Football key not verified |
| Portfolio | CLEAN | **READY** | PII removal IS the remediation; current tree clean; history rewrite can proceed for PII only |
| LogiFlow | EXPOSURE (no PR) | **BLOCKED** | No cleanup PR created; Evolution API key still in 5 docs files |
| API_Analyze | EXPOSURE (no PR) | **BLOCKED** | No cleanup PR created; API keys still in .env.example |

### Phase 2A.7 Update — Factual Dependency Changes (preserved)

1. **MVP-linkedin-bot PR #2 has been MERGED** (merge SHA: `c2afbcd5`). Current tree is clean. History sanitization is still needed for the original credential/PII commits.
2. **Two additional compromised credentials discovered** in Phase 2A.6.1: Telegram bot token (item 40) and LinkedIn password (item 41). These must be added to the history sanitization scope for MVP-linkedin-bot.
3. **Four env-dependent PRs reclassified** based on runtime evidence (see `CREDENTIAL_RUNTIME_REALITY_AUDIT.md`):
   - base-corporativa: MERGE_READY_AFTER_ROTATION (conditional) — merge after Leonardo confirms env vars set
   - Digital-Signage-Platform: OWNER_HANDOFF_BEFORE_MERGE — notify ICTSI first
   - FlowTrack: OWNER_HANDOFF_BEFORE_MERGE — notify ICTSI first
   - Bot_IqOption: NEEDS_MANUAL_CONFIRMATION — Railway auto-deploy state unconfirmed
4. **Former-employer systems (ICTSI/iTracker)**: History sanitization for Digital-Signage-Platform and FlowTrack should only proceed after OWNER_HANDOFF is completed and ICTSI has confirmed credential rotation.
5. **Credential rotation status**: Leonardo reports credentials changed (OWNER_REPORTED). Provider-side revocation not independently verified by Devin.

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

## Per-Repository Sanitization Plan

### 1. ProFlow

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC when secrets were committed |
| **Forks possible** | Yes — was public. Check `gh api repos/LeonardoRFragoso/ProFlow/forks` |
| **Paths to purge** | `RAILWAY_ENV_FINAL.txt`, `DEPLOY_CHECKLIST.md` |
| **Branches affected** | All branches containing these files in history |
| **Tags affected** | Check `git tag` — likely none |
| **Open PR impact** | PR #1 and #2 (both stale, close candidates) — will need force-update or close first |
| **Force-push required** | Yes — `git push --force --mirror` |
| **Collaborator impact** | Any local clones will need re-clone |
| **Deployment integration** | Railway — no direct integration with git history (deploys from branch HEAD) |
| **Worthwhile?** | **YES** — was public, contains payment/OAuth/OpenAI credentials. High risk of automated scraping. |
| **Prerequisite** | All 7 credentials (items #1-#7 in rotation matrix) must be ROTATED first |
| **Recommended command** | `git filter-repo --invert-paths --path RAILWAY_ENV_FINAL.txt --path DEPLOY_CHECKLIST.md` |
| **Backup strategy** | `git clone --mirror` to local backup before rewrite |
| **Authorization required** | Leonardo must explicitly approve |

### 2. base-corporativa

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. Secrets are in CURRENT TREE (not just history). |
| **Forks possible** | Yes — was public |
| **Paths to purge** | `RAILWAY_ENV_ATUALIZADO.txt`, `backend/.env.railway` |
| **Also purge from source** | R2 keys hardcoded in `backend/fix_product_images_r2.py`, `backend/list_r2_images.py`, `backend/upload_pdfs_to_r2.py`, `backend/upload_product_images_to_r2.py` — use `--replace-text` to redact the key values from all historical versions |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Railway — deploys from branch HEAD, not history |
| **Worthwhile?** | **YES** — was public, contains R2/payment/email/DB credentials in current tree. |
| **Prerequisite** | All 10 credentials (items #8-#17 in rotation matrix) must be ROTATED first |
| **Recommended command** | `git filter-repo --invert-paths --path RAILWAY_ENV_ATUALIZADO.txt --path backend/.env.railway` then `git filter-repo --replace-text` with the R2 key values to redact them from Python script history |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |

### 3. FinanceControl

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. RSA key in current tree AND history. |
| **Forks possible** | Yes — was public |
| **Paths to purge** | `chave-EC2/Finance2.pem`, `backend/chave-EC2/Finance2.pem` (historical path), `backend/db.sqlite3`, `ReciboDePagamento_3_01122025173256_408_b479a41d.pdf` |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None identified |
| **Worthwhile?** | **YES** — was public, contains RSA private key for EC2. EC2 keypair must be rotated first. |
| **Prerequisite** | EC2 keypair (item #18 in rotation matrix) must be ROTATED/REVOKED first |
| **Recommended command** | `git filter-repo --invert-paths --path chave-EC2/Finance2.pem --path backend/chave-EC2/Finance2.pem --path backend/db.sqlite3 --path "ReciboDePagamento_3_01122025173256_408_b479a41d.pdf"` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |

### 4. Digital-Signage-Platform

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. DB credentials in history. |
| **Forks possible** | Yes — was public |
| **Paths to purge** | `secrets/db_credentials.txt`, `.env.tv`, `.env.production` |
| **Also purge** | Historical DB credentials in `backend/app.py`, `backend/tools/migrate_sqlite_to_mysql.py`, `backend/.env.production.example` — use `--replace-text` to redact the `tvs_itracker` DB URL and password values |
| **Branches affected** | All branches (2 branches) |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Former employer (iTracker) — confirm no active CI/CD integration |
| **Worthwhile?** | **YES** — was public, contains former employer DB credentials. Legal review recommended. |
| **Prerequisite** | DB credentials (item #19) and JWT secret (item #20) must be ROTATED first. **Confirm with iTracker IT if DB is under their control.** |
| **Recommended command** | `git filter-repo --invert-paths --path secrets/db_credentials.txt --path .env.tv --path .env.production` then `git filter-repo --replace-text` with DB URL/password values |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve. **Legal review recommended due to former employer IP.** |

### 5. FlowTrack

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. Session tokens in history. |
| **Forks possible** | Yes — was public |
| **Paths to purge** | `nohup.out` |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Client (ICTSI) — confirm no active CI/CD |
| **Worthwhile?** | **YES** — was public, contains 179 session/CSRF tokens from production operations system. |
| **Prerequisite** | Session tokens (item #30) should be invalidated first. SECRET_KEY (item #29) should be rotated. |
| **Recommended command** | `git filter-repo --invert-paths --path nohup.out` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve. **Legal review recommended due to client IP.** |

### 6. Bot_IqOption

| Field | Value |
|---|---|
| **Visibility** | PRIVATE (was already private) |
| **Public when leaked** | No — was always private. Lower risk of external scraping. |
| **Forks possible** | Unlikely (private repo) |
| **Paths to purge** | `bot_iqoption_v2/backend/.env`, `bot_iqoption_v2/backend/RAILWAY_ENV_COMPLETE.txt`, `bot_iqoption_v2/backend/bot_iqoption.log`, `bot_iqoption_v2/backend/keys/` (entire directory), `bot_iqoption_v2/backend/db.sqlite3`, `bot_iqoption_v2/backend/venv/` (entire directory) |
| **Also purge** | Real MERCADOPAGO_CLIENT_SECRET values in historical versions of `.env.example` and `RAILWAY_ENV_TEMPLATE.md` — use `--replace-text` |
| **Branches affected** | All branches (5 branches) |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Railway — deploys from branch HEAD |
| **Worthwhile?** | **MODERATE** — was always private, but contains production MercadoPago credentials and 197 JWT tokens. Worthwhile for hygiene but lower urgency than public repos. |
| **Prerequisite** | All MercadoPago credentials (items #21-#24), SECRET_KEY (#25), session tokens (#26), user keys (#27) must be ROTATED first |
| **Recommended command** | `git filter-repo --invert-paths --path bot_iqoption_v2/backend/.env --path bot_iqoption_v2/backend/RAILWAY_ENV_COMPLETE.txt --path bot_iqoption_v2/backend/bot_iqoption.log --path bot_iqoption_v2/backend/keys --path bot_iqoption_v2/backend/db.sqlite3 --path bot_iqoption_v2/backend/venv` then `git filter-repo --replace-text` with MERCADOPAGO_CLIENT_SECRET values |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |

### 7. MVP-linkedin-bot

| Field | Value |
|---|---|
| **Visibility** | PRIVATE (was already private) |
| **Public when leaked** | No — was always private |
| **Forks possible** | Unlikely (private repo) |
| **Paths to purge** | `Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot/` (entire directory), `Auto_job_applier_linkedIn/V2-Completa/chrome_profile_linkedin_bot/` (entire directory), `Auto_job_applier_linkedIn/V1/logs/` (entire directory), `cpf.pdf`, `perguntas.csv`, any `venv/` directories |
| **Branches affected** | All branches (2 branches) |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | PR #1 (devin bot fix) — will need force-update or close first |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None identified |
| **Worthwhile?** | **MODERATE** — was always private, but contains Chrome session tokens and personal ID. Large repo (~867MB) — history rewrite will be slow. |
| **Prerequisite** | Chrome/Google session (#31) and LinkedIn session (#32) must be invalidated first |
| **Recommended command** | `git filter-repo --invert-paths --path Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot --path Auto_job_applier_linkedIn/V2-Completa/chrome_profile_linkedin_bot --path Auto_job_applier_linkedIn/V1/logs --path cpf.pdf --path perguntas.csv` |
| **Backup strategy** | `git clone --mirror` to local backup (will be large) |
| **Authorization required** | Leonardo must explicitly approve. **Note:** PR #1 should be reviewed/merged or closed before rewrite. |

### 8. Bet-IA-BOT

| Field | Value |
|---|---|
| **Visibility** | PRIVATE (was already private) |
| **Public when leaked** | No |
| **Forks possible** | Unlikely |
| **Paths to purge** | N/A — the API key is hardcoded in `backend/test_new_api.py` (not a separate file). Use `--replace-text` to redact the key value from all historical versions. |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | None identified |
| **Worthwhile?** | **LOW** — single API key in a private repo. Lower priority. Can be deferred. |
| **Prerequisite** | API-Football key (#34) must be ROTATED first |
| **Recommended command** | `git filter-repo --replace-text <(echo 'ACTUAL_API_KEY_VALUE==>REDACTED')` (the cleanup PR already replaces it with env var loading) |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve. **Low priority — can defer.** |

### 9. Portfolio-LeonardoFragoso-React

| Field | Value |
|---|---|
| **Visibility** | PUBLIC (stays public) |
| **Public when leaked** | Yes — is PUBLIC |
| **Forks possible** | Yes — is public |
| **Paths to purge** | `public/Docs/cartao cnpj.pdf`, `public/Docs/contrato-social-cnpj.pdf` |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Vercel/Netlify — deploys from branch HEAD |
| **Worthwhile?** | **YES** — is public, contains personal/business registration documents. PII exposure. |
| **Prerequisite** | None — these are PII documents, not credentials. No rotation needed. |
| **Recommended command** | `git filter-repo --invert-paths --path "public/Docs/cartao cnpj.pdf" --path "public/Docs/contrato-social-cnpj.pdf"` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |

### 10. AndaimesPini_Project

| Field | Value |
|---|---|
| **Visibility** | Now PRIVATE |
| **Public when leaked** | Yes — was PUBLIC. SQLite DB with client data was in current tree. |
| **Forks possible** | Yes — was public |
| **Paths to purge** | `database/db.sqlite3`, all `*.sqlite_backup` files |
| **Branches affected** | All branches |
| **Tags affected** | Check `git tag` |
| **Open PR impact** | None (0 open PRs) |
| **Force-push required** | Yes |
| **Collaborator impact** | Local clones need re-clone |
| **Deployment integration** | Railway + Vercel — deploys from branch HEAD |
| **Worthwhile?** | **YES** — was public, contains client business data in SQLite DB. |
| **Prerequisite** | None — these are data artifacts, not credentials. |
| **Recommended command** | `git filter-repo --invert-paths --path database/db.sqlite3 --use-base-name --path '*.sqlite_backup'` |
| **Backup strategy** | `git clone --mirror` to local backup |
| **Authorization required** | Leonardo must explicitly approve |

---

## Execution Order (When Authorized)

### Tier 1 — Was PUBLIC + Contains Credentials (Highest Risk)

1. **ProFlow** — payment/OAuth/OpenAI credentials, was public
2. **base-corporativa** — R2/payment/email/DB credentials, was public, in current tree
3. **FinanceControl** — RSA EC2 key, was public, in current tree
4. **Digital-Signage-Platform** — DB credentials + JWT secret, was public
5. **Portfolio-LeonardoFragoso-React** — PII documents, is public
6. **AndaimesPini_Project** — client data, was public
7. **FlowTrack** — session tokens, was public

### Tier 2 — Was PRIVATE + Contains Credentials (Moderate Risk)

8. **Bot_IqOption** — MercadoPago + JWT + user keys, was private
9. **MVP-linkedin-bot** — Chrome/LinkedIn sessions + PII, was private

### Tier 3 — Low Priority

10. **Bet-IA-BOT** — single API key, was private, can defer

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

---

## Summary

| Tier | Repos | Risk | Action |
|---|---|---|---|
| Tier 1 (was public + credentials) | ProFlow, base-corporativa, FinanceControl, Digital-Signage-Platform, Portfolio-LeonardoFragoso-React, AndaimesPini_Project, FlowTrack | HIGH | Rewrite after credential rotation |
| Tier 2 (was private + credentials) | Bot_IqOption, MVP-linkedin-bot | MODERATE | Rewrite after credential rotation |
| Tier 3 (low priority) | Bet-IA-BOT | LOW | Can defer |

**Total repos requiring history rewrite: 10**
**History rewrites performed in Phase 2A: 0** (PLAN ONLY — awaiting authorization)
