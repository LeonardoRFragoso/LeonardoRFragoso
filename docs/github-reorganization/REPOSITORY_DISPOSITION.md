# Repository Disposition — Phase 2A.10 (Visibility totals corrected Phase 2A.10.1, runtime state updated Phase 2A.11, history rewrite Batch 1 Phase 2A.12, Batch 2 Phase 2A.13, Batch 3 Phase 2A.14, ProFlow Phase 2A.15)

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Phase 2A.10.1 update:** 2026-08-18 (visibility totals reconciled against live GitHub metadata)
**Phase 2A.11 update:** 2026-08-18 (Railway runtime state reconciled — only ProFlow active)
**Phase 2A.12 Batch 1 update:** 2026-08-18 (history rewrite executed for Portfolio + AndaimesPini)
**Phase 2A.13 Batch 2 update:** 2026-08-18 (history rewrite executed for FinanceControl, PayFlow-AI, LogiFlow, base-corporativa after owner attestation gate)
**Phase 2A.14 Batch 3 update:** 2026-08-18 (history rewrite executed for API_Analyze, Bot_IqOption, MVP-linkedin-bot after owner attestation + session closure gate)
**Phase 2A.15 update:** 2026-08-18 (ProFlow production-safe history rewrite executed after owner attestation + production redeploy authorization gate; Railway + Vercel redeploy triggered and healthy)
**Phase 2A.16 update:** 2026-08-18 (Phase 2A security closure — Digital-Signage-Platform and FlowTrack formally deferred as DEFERRED_EXTERNAL_OWNER_HANDOFF; PERSONAL_PORTFOLIO_SECURITY_GATE=PASS; PHASE_2B_ALLOWED=YES)
**Operation:** Repository deletion batch (13 repositories deleted)

> **CRITICAL:** This document records the intentional deletion of 13 repositories that no longer have strategic, portfolio, historical, or operational value. All 13 repositories were backed up locally (mirror clone + git bundle) before deletion. No credential values are listed.

## Disposition Categories

| Category | Description |
|---|---|
| ACTIVE_SHOWCASE_CANDIDATE | Repositories suitable for portfolio showcase (Phase 2B will finalize rankings) |
| ACTIVE_SUPPORTING | Active repositories that support showcase projects but are not showcase candidates themselves |
| PRIVATE_ACTIVE | Private repositories with active development |
| CLIENT_OR_IP_PRIVATE | Private repositories containing client work or intellectual property |
| FORMER_EMPLOYER_PRIVATE | Private repositories from former employer (ICTSI/iTracker) — handoff required |
| DELETED_HIRING_TEST | Deleted: old hiring-process technical exercises |
| DELETED_STUDY_PROJECT | Deleted: learning/study repositories whose skills are represented elsewhere |
| DELETED_NO_STRATEGIC_VALUE | Deleted: no strategic reason to retain |

## Deleted Repositories (13)

### DELETED_HIRING_TEST (2 repositories)

| Repository | Visibility | Default Branch | Reason |
|---|---|---|---|
| LeonardoRFragoso/-Backend-Pipefy-AWS-no-Mundo-Invest | public | main | Old hiring-process technical exercise. No longer represents desired portfolio. |
| LeonardoRFragoso/IronForceAI-Teste | public | main | Old hiring-process technical exercise. No longer represents desired portfolio. |

### DELETED_STUDY_PROJECT (4 repositories)

| Repository | Visibility | Default Branch | Reason |
|---|---|---|---|
| LeonardoRFragoso/AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes | public | main | Learning/study repository. Relevant skills represented by stronger projects. |
| LeonardoRFragoso/pimenta | public | main | Learning/study repository. Relevant skills represented by stronger projects. |
| LeonardoRFragoso/PRODERJ | public | main | Learning/study repository. Relevant skills represented by stronger projects. |
| LeonardoRFragoso/sanduicherie | public | main | Learning/study repository. Relevant skills represented by stronger projects. |

### DELETED_NO_STRATEGIC_VALUE (7 repositories)

| Repository | Visibility | Default Branch | Reason |
|---|---|---|---|
| LeonardoRFragoso/alzi-project | private | main | No strategic reason to retain. |
| LeonardoRFragoso/dash-monitor | private | main | No strategic reason to retain. |
| LeonardoRFragoso/aviator-banca | private | main | No strategic reason to retain. |
| LeonardoRFragoso/Sistema-de-compras | private | main | No strategic reason to retain. |
| LeonardoRFragoso/nao-conformidade | private | main | No strategic reason to retain. |
| LeonardoRFragoso/SGE-Django | private | master | No strategic reason to retain. |
| LeonardoRFragoso/Bet-IA-BOT | private | main | No strategic reason to retain. Security audit trail preserved (item #34). |

## Bet-IA-BOT Security Audit Trail

Bet-IA-BOT participated in the canonical 41-item security audit:
- **Item #34:** API-Football API key (REVOKE_ONLY)
- **REPOSITORY_LIFECYCLE:** DELETED_BY_OWNER
- **History sanitization:** NOT_APPLICABLE_REPOSITORY_DELETED (GitHub repository no longer exists)
- **Canonical item #34:** preserved — classification remains REVOKE_ONLY
- **Evidence state:** unchanged (OWNER_REPORTED)
- **Repository deletion does NOT prove credential revocation**

## Remaining Repositories (30)

The following 30 repositories remain in the account. Final portfolio showcase rankings will be determined in Phase 2B.

| Repository | Visibility | Provisional Category |
|---|---|---|
| LeonardoRFragoso | public | ACTIVE_SHOWCASE_CANDIDATE |
| ProFlow | private | ACTIVE_SHOWCASE_CANDIDATE |
| DevPro | private | ACTIVE_SHOWCASE_CANDIDATE |
| desafio-focon | public | ACTIVE_SHOWCASE_CANDIDATE |
| Legal-AI-Copilot | public | ACTIVE_SHOWCASE_CANDIDATE |
| LogiFlow | public | ACTIVE_SHOWCASE_CANDIDATE |
| PayFlow-AI | public | ACTIVE_SHOWCASE_CANDIDATE |
| Pagae | public | ACTIVE_SHOWCASE_CANDIDATE |
| Oraculo | public | ACTIVE_SHOWCASE_CANDIDATE |
| vigil-ai | public | ACTIVE_SHOWCASE_CANDIDATE |
| Portfolio-LeonardoFragoso-React | public | ACTIVE_SHOWCASE_CANDIDATE |
| MVP-linkedin-bot | private | ACTIVE_SUPPORTING |
| FinanceControl | private | ACTIVE_SUPPORTING |
| API_Analyze | public | ACTIVE_SUPPORTING |
| base-corporativa | private | PRIVATE_ACTIVE |
| Bot_IqOption | private | PRIVATE_ACTIVE |
| Digital-Signage-Platform | private | FORMER_EMPLOYER_PRIVATE |
| FlowTrack | private | FORMER_EMPLOYER_PRIVATE |
| devpro-e2e-sandbox | private | ACTIVE_SUPPORTING |
| AndaimesPini_Project | private | CLIENT_OR_IP_PRIVATE |
| exnova-api | private | CLIENT_OR_IP_PRIVATE |
| Plataforma-Cursos-WRConsultoria | private | CLIENT_OR_IP_PRIVATE |
| wrconsultoriaesolucoes | private | CLIENT_OR_IP_PRIVATE |
| SaaS | private | PRIVATE_ACTIVE |
| FragTech-Fintech | public | ACTIVE_SHOWCASE_CANDIDATE |
| Go-API-Gestao-de-Projetos-e-Tarefas | public | ACTIVE_SHOWCASE_CANDIDATE |
| MedFlow_Finance | public | ACTIVE_SHOWCASE_CANDIDATE |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | public | ACTIVE_SHOWCASE_CANDIDATE |
| PyScriptTech | public | ACTIVE_SHOWCASE_CANDIDATE |
| YardMaster | private | PRIVATE_ACTIVE |

> **Note:** Provisional categories are preliminary. Final portfolio showcase rankings belong to Phase 2B and are NOT finalized here.

## Repository Count

| Metric | Value |
|---|---|
| Before deletion | 43 |
| Deleted | 13 |
| After deletion | 30 |
| Delta | -13 |

## Visibility Totals (live, reconciled Phase 2A.10.1)

> **Phase 2A.10.1 correction:** Visibility totals below are recomputed from live GitHub repository metadata on 2026-08-18 (`gh repo list LeonardoRFragoso --limit 100 --json name,visibility`). The earlier Phase 2A.10 report value of 16 public / 14 private is STALE and must not be trusted. The invariant `PUBLIC + PRIVATE = 30` holds.

| Metric | Value |
|---|---|
| ACCOUNT_TOTAL_REPOS | 30 |
| PUBLIC_REPOS | 15 |
| PRIVATE_REPOS | 15 |
| PUBLIC + PRIVATE | 30 |

## Backup Location

All 13 repositories were backed up before deletion:
- **Directory:** `github-deletion-backups/phase-2a-10/`
- **Format:** git mirror clone + git bundle
- **Manifest:** `DELETE_MANIFEST.md` in backup directory

## Railway Runtime State (Phase 2A.11 — OWNER_ATTESTED_RUNTIME_STATE)

Leonardo explicitly confirms that **the only project currently deployed on Railway is ProFlow**. This attestation applies ONLY to Railway deployment state. It does NOT prove credential revocation, provider-side key invalidation, session invalidation, password changes, or ICTSI owner authorization.

| Repository | Railway Deployment | Evidence |
|---|---|---|
| ProFlow | ACTIVE_PRODUCTION | OWNER_ATTESTED_RUNTIME_STATE — only active Railway project |
| base-corporativa | NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED | Leonardo confirms not deployed on Railway |
| Bot_IqOption | NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED | Leonardo confirms not deployed on Railway |
| Digital-Signage-Platform | NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED | Leonardo confirms not deployed on Railway (also ICTSI-owned) |
| FlowTrack | NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED | Leonardo confirms not deployed on Railway (also ICTSI-owned) |
| MVP-linkedin-bot | NO_ACTIVE_RAILWAY_DEPLOYMENT_OWNER_ATTESTED | Leonardo confirms not deployed on Railway |

### Phase 2A.11 Cleanup PR Merges

| Repository | PR | Pre-merge head | Merge SHA | Current Tree |
|---|---|---|---|---|
| base-corporativa | #1 | e1655bb3166fa120ecaffa8e8f35dfaf33b717ca | e40c90fe5e98609509ad6cf0d00406a3f92bbe60 | CLEAN |
| Bot_IqOption | #5 | d3a248eee8be3979a6b96b784393f0a3b629bc69 | f26b29496dbb7e9c302d65252b1fdc0f956291a7 | CLEAN |

## Phase 2A.12 Batch 1 — History Rewrite Record

First actual history rewrite phase. Two repositories rewritten sequentially with immutable backups, pre-push integrity checks, and fresh-clone verification.

| Repository | Pre-rewrite main SHA | Post-rewrite main SHA | Paths Removed | Backup | Bundle | Post-rewrite scan | Fork risk | GitHub support cleanup |
|---|---|---|---|---|---|---|---|---|
| Portfolio-LeonardoFragoso-React | 4d9fc8880cad0b69b6e35eaf59b54a1be6d869d3 | 2a067f9a058d5941274779b036f811e4202b2c57 | `public/Docs/cartao cnpj.pdf`, `public/Docs/contrato-social-cnpj.pdf`, `dist/Docs/cartao cnpj.pdf`, `dist/Docs/contrato-social-cnpj.pdf` | VERIFIED (76M mirror) | VERIFIED (4 refs) | PASS (gitleaks clean, PII absent) | 0 forks | YES (refs/pull/1/head retains old history) |
| AndaimesPini_Project | 23c1a53d67378754ae6acb0e39753549f812f6e9 | be192a64116359a11e4619ae78a94686a0b7be41 | `database/db.sqlite3`, `database/db.sqlite3-shm`, `database/db.sqlite3-wal`, `*.sqlite_backup` (17 files) | VERIFIED (1.3M mirror) | VERIFIED (4 refs) | PASS (gitleaks clean, SQLite artifacts absent) | 0 forks | YES (refs/pull/1/head retains old history) |

### Lifecycle status

- REWRITE_COMPLETED = 2 (Portfolio-LeonardoFragoso-React, AndaimesPini_Project)
- REWRITE_PENDING = 10
- UPSTREAM_HISTORY_SANITIZED = YES for both completed repos
- GLOBAL_ERASURE_UNPROVEN = YES for both (GitHub-managed PR refs retain old history)
- GITHUB_SUPPORT_CLEANUP_REQUIRED = YES for both

## Phase 2A.13 Batch 2 — History Rewrite Record

Second history rewrite phase. Four repositories rewritten sequentially (FinanceControl → PayFlow-AI → LogiFlow → base-corporativa) after the owner attestation gate passed. Immutable backups, pre-push integrity checks, and fresh-clone verification performed for each. No secret values printed in any report, PR, or commit.

| Repository | Pre-rewrite main SHA | Post-rewrite main SHA | Method | Backup | Bundle | Source Integrity | Post-rewrite scan | Fork risk | GitHub support cleanup |
|---|---|---|---|---|---|---|---|---|---|
| FinanceControl | feb1ffdc97ef3971193248ee9b61dc1d8dbcd031 | 3a1c40d5881acd046e3ba1551dd66d9084ada37a | --invert-paths (5 paths: RSA key, 2 SQLite DBs, PDF) | VERIFIED | VERIFIED | PASS (341 files, identical blob SHAs) | PASS (1 benign historical README placeholder) | 0 forks | YES (refs/pull/1/head) |
| PayFlow-AI | afdcb7b58b187c146e15848659192205c08a882b | 003291b613b85ad90fb005810d5290aa79ed69ac | --replace-text (2 Twilio auth token values, 32-hex) | VERIFIED | VERIFIED | PASS (375 files, identical blob SHAs) | PASS (1 benign README placeholder SECRET_KEY) | 0 forks | YES (refs/pull/1/head) |
| LogiFlow | 90df4b0b727c37e9840f7002d394080f63086e08 | b82451f612d7043367e3789489a36073dff4531c | --replace-text (1 Evolution API key, 27 chars) | VERIFIED | VERIFIED | PASS (715 files, identical blob SHAs) | PASS (305 false positives only) | 0 forks | YES (refs/pull/1/head) |
| base-corporativa | e40c90fe5e98609509ad6cf0d00406a3f92bbe60 | 33f7d1999cfd56fc2a09f362ea859ec074b064e7 | --invert-paths (3 env files) + --replace-text (6 secrets: 2 R2 keys, 3 env-file secrets, SendGrid key) | VERIFIED | VERIFIED | PASS (584 files, identical blob SHAs) | PASS (3 current-tree placeholders in example docs) | 0 forks | YES (refs/pull/1/head) |

### Deployment-risk decisions (owner-authorized)

- base-corporativa: Railway deployment records present but owner-attested inactive (PROCEED)
- FinanceControl: no deployment integration (PROCEED)
- PayFlow-AI: active Vercel production deployment — owner explicitly authorized force-push accepting Vercel redeploy (PROCEED)
- LogiFlow: 4 active Vercel production deployments — owner explicitly authorized force-push accepting Vercel redeploy (PROCEED)

### Lifecycle status (updated)

- REWRITE_COMPLETED = 6 (Portfolio-LeonardoFragoso-React, AndaimesPini_Project, FinanceControl, PayFlow-AI, LogiFlow, base-corporativa)
- REWRITE_PENDING = 6 (ProFlow, Digital-Signage-Platform, FlowTrack, Bot_IqOption, MVP-linkedin-bot, API_Analyze)
- COMPLETED + READY + BLOCKED = 6 + 0 + 6 = 12 (= ACTIVE_REWRITE_CANDIDATES)
- UPSTREAM_HISTORY_SANITIZED = YES for all 6 completed repos
- GLOBAL_ERASURE_UNPROVEN = YES for all 6 (GitHub-managed PR refs retain old history)
- GITHUB_SUPPORT_CLEANUP_REQUIRED = YES for all 6
- OWNER_ATTESTED_COMPLETED = YES for items #8-#17, #18, #28, #37 (NOT PROVIDER_VERIFIED)

## Phase 2A.14 Batch 3 — History Rewrite Record

Third history rewrite phase. Three repositories rewritten sequentially (API_Analyze → Bot_IqOption → MVP-linkedin-bot) after the owner attestation + session closure gate passed. Immutable backups, pre-push integrity checks, and fresh-clone verification performed for each. No secret values, PII, or session data printed in any report, PR, or commit.

| Repository | Pre-rewrite main SHA | Post-rewrite main SHA | Method | Backup | Bundle | Source Integrity | Post-rewrite scan | Fork risk | GitHub support cleanup |
|---|---|---|---|---|---|---|---|---|---|
| API_Analyze | e521658aa32c2fa568e6190a08ac26a6013315af | 6b3beb4e2624ad9e2bc66c1836d1a4d9aa5a44e0 | --replace-text (2 API key values: News API 16-char, Alpha Vantage 32-hex) | VERIFIED | VERIFIED | PASS (210 files, identical blob SHAs) | PASS (0 gitleaks findings) | YES (1 fork: kabann-1978/API_Analyze-B3, NOT modified) | YES (refs/pull/1/head) |
| Bot_IqOption | f26b29496dbb7e9c302d65252b1fdc0f956291a7 | 4b24fd33923ade683a8e6ba5dda59b356c42489d | --invert-paths (7 paths: .env, RAILWAY_ENV_COMPLETE.txt, bot_iqoption.log, keys/, db.sqlite3, venv/, bot-iq.pem [scope discovery]) + --replace-text (1 MP_CLIENT_SECRET) | VERIFIED | VERIFIED | PASS (295 files, identical blob SHAs) | PASS (0 gitleaks findings) | NO (0 forks) | YES (refs/pull/5/head) |
| MVP-linkedin-bot | c2afbcd5e35867bd585ed89ac1641d8a6430bf02 | 749ef218395628e28139a49aeaa61dee270802f6 | --invert-paths (6 directories: 3 chrome_profile_linkedin_bot, V1/logs, 2 venv; + 15 PII files: cpf.pdf, perguntas.csv, Profile.pdf, 7 CV PDFs, 2 application CSVs, resume.pdf) | VERIFIED | VERIFIED | PASS (206 files; 1 empty .gitkeep placeholder removed as part of logs/ cleanup) | PASS (0 gitleaks findings) | NO (0 forks) | YES (refs/pull/1/head + refs/pull/2/head) |

### Open PR gate resolution

- MVP-linkedin-bot PR #1 (fix numeric question in PT-BR, 1 unique commit 8acdcc36) was closed by owner authorization to unblock the history rewrite. The fix commit is preserved in branch `devin/1781123382-fix-numeric-question-no-preposition` and can be re-applied after the rewrite.

### Lifecycle status (updated)

- REWRITE_COMPLETED = 9 (Portfolio-LeonardoFragoso-React, AndaimesPini_Project, FinanceControl, PayFlow-AI, LogiFlow, base-corporativa, API_Analyze, Bot_IqOption, MVP-linkedin-bot)
- REWRITE_PENDING = 3 (ProFlow, Digital-Signage-Platform, FlowTrack)
- COMPLETED + READY + BLOCKED = 9 + 0 + 3 = 12 (= ACTIVE_REWRITE_CANDIDATES)
- UPSTREAM_HISTORY_SANITIZED = YES for all 9 completed repos
- GLOBAL_ERASURE_UNPROVEN = YES for all 9 (GitHub-managed PR refs retain old history)
- GITHUB_SUPPORT_CLEANUP_REQUIRED = YES for all 9
- OWNER_ATTESTED_COMPLETED = YES for items #1-#7, #8-#17, #18, #21-#27, #28, #37, #38-#41 (NOT PROVIDER_VERIFIED)
- OWNER_ATTESTED_SESSION_INVALIDATED = YES for items #26, #31, #32 (NOT PROVIDER_VERIFIED)
- FORK_RISK = YES for API_Analyze (1 fork: kabann-1978/API_Analyze-B3 — NOT modified, may retain old secrets)

## Phase 2A.15 — ProFlow Production-Safe History Rewrite Record

Fourth history rewrite phase. ProFlow is the ONLY repository in Leonardo's account currently deployed on Railway (env: independent-respect/production) AND Vercel (Production + Preview environments). Both platforms deploy from main branch HEAD. Force-pushing rewritten main triggered redeployment on both platforms. Owner explicitly authorized the force-push and possible production redeploy.

| Repository | Pre-rewrite main SHA | Post-rewrite main SHA | Method | Backup | Bundle | Source Integrity | Test/Build | Post-rewrite scan | Production | Fork risk | GitHub support cleanup |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ProFlow | 390ea2b6ef2e44c0e548b4f4e4b60bee303b1a08 | 514aed8a38a3744d29860631400b707e1d0bb672 | --invert-paths (3 paths: RAILWAY_ENV_FINAL.txt, DEPLOY_CHECKLIST.md, MP_PRODUCTION_VALIDATION.md) + --replace-text (1 MP access token APP_USR-<REDACTED_MP_TOKEN> in dev.py + Docs/MP_PRODUCTION_VALIDATION.md history) | VERIFIED | VERIFIED | PASS (1012 files, identical blob SHAs; Docs/MP_PRODUCTION_VALIDATION.md preserved) | PASS (Django 4.2.7 syntax, frontend npm build SUCCESS) | PASS (18 false-positive findings) | Railway + Vercel redeploy triggered, HEALTHY before and after (www.proflow.pro HTTP 200) | NO (0 forks) | YES (refs/pull/2-9/head) |

### Open PR gate resolution

- PR #2 (copilot/add-mercado-pago-subscription) classified as STALE_EQUIVALENT_TO_MAIN (only 7 genuinely new files: task JSONs, test file, logos — no useful unique application work). Closed.
- PR #1 (copilot/eldest-turtle) classified as UNIQUE_WORK_PRESERVED (92 genuinely new source files: MP subscription, badges, payments, AI engine, auth). Remained open. Branch force-pushed with all 92 new source files preserved.

### Production safety

- Deployed commit before: 390ea2b6ef (= main HEAD)
- Deployed commit after: 514aed8a38 (= rewritten main HEAD)
- Railway deploy triggered: YES (railway-app[bot], 514aed8a38, 2026-08-18T21:43:28Z)
- Vercel Production deploy triggered: YES (vercel[bot], 514aed8a38, 2026-08-18T21:44:04Z)
- Frontend health: www.proflow.pro HTTP 200 before and after (HEALTHY → HEALTHY)
- API health: api.proflow.pro HTTP 404 before and after (normal — no root view)
- CI workflow: failure before and after (pre-existing — not caused by rewrite)
- Regression: NO

### Lifecycle status (updated)

- REWRITE_COMPLETED = 10 (Portfolio-LeonardoFragoso-React, AndaimesPini_Project, FinanceControl, PayFlow-AI, LogiFlow, base-corporativa, API_Analyze, Bot_IqOption, MVP-linkedin-bot, ProFlow)
- REWRITE_PENDING = 2 (Digital-Signage-Platform, FlowTrack — former-employer scope, OUT OF SCOPE)
- COMPLETED + READY + BLOCKED = 10 + 0 + 2 = 12 (= ACTIVE_REWRITE_CANDIDATES)
- UPSTREAM_HISTORY_SANITIZED = YES for all 10 completed repos
- GLOBAL_ERASURE_UNPROVEN = YES for all 10 (GitHub-managed PR refs retain old history)
- GITHUB_SUPPORT_CLEANUP_REQUIRED = YES for all 10
- OWNER_ATTESTED_COMPLETED = YES for items #1-#7, #8-#17, #18, #21-#27, #28, #37, #38-#41 (NOT PROVIDER_VERIFIED)
- OWNER_ATTESTED_SESSION_INVALIDATED = YES for items #26, #31, #32 (NOT PROVIDER_VERIFIED)
- FORK_RISK = YES for API_Analyze (1 fork: kabann-1978/API_Analyze-B3 — NOT modified, may retain old secrets)

## Phase 2A.16 — Security Closure & Former-Employer Deferral

### Former-employer repository finalization

| Repository | Classification | SECURITY_REMEDIATION_OWNER | LEONARDO_HISTORY_REWRITE_AUTHORIZED | PORTFOLIO_SHOWCASE_ELIGIBLE | PUBLIC_VISIBILITY_ALLOWED | Lifecycle | PR Status |
|---|---|---|---|---|---|---|---|
| Digital-Signage-Platform | FORMER_EMPLOYER_PRIVATE | ICTSI/iTracker | NO | NO | NO | DEFERRED_EXTERNAL_OWNER_HANDOFF | PR #4 OPEN, MERGEABLE — intentionally NOT merged |
| FlowTrack | FORMER_EMPLOYER_PRIVATE | ICTSI/iTracker | NO | NO | NO | DEFERRED_EXTERNAL_OWNER_HANDOFF | PR #1 OPEN, MERGEABLE — intentionally NOT merged |

> Both former-employer repos remain PRIVATE. They are NOT classified as ACTIVE_SHOWCASE_CANDIDATE. Their GitHub visibility was NOT modified (already private). Their PRs were NOT merged or closed. Their history was NOT rewritten. Their credentials/sessions were NOT rotated. DO_NOT_EXECUTE_WITHOUT_EXTERNAL_OWNER_AUTHORIZATION.

### Final lifecycle status (Phase 2A complete)

- REWRITE_COMPLETED = 10
- DEFERRED_EXTERNAL_OWNER = 2 (Digital-Signage-Platform, FlowTrack)
- PORTFOLIO_OWNED_HISTORY_PENDING = 0
- BLOCKED_EXTERNAL_OWNER = 2
- PERSONAL_PORTFOLIO_SECURITY_GATE = PASS
- PHASE_2B_ALLOWED = YES
- Canonical security items = 41 (preserved — no renumbering, no deletion)
- Unresolved former-employer items: #19, #20, #29, #30 (EXTERNAL_OWNER_DEFERRED)
