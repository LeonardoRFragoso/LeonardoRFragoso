# Repository Disposition — Phase 2A.10 (Visibility totals corrected Phase 2A.10.1, runtime state updated Phase 2A.11, history rewrite Batch 1 Phase 2A.12)

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Phase 2A.10.1 update:** 2026-08-18 (visibility totals reconciled against live GitHub metadata)
**Phase 2A.11 update:** 2026-08-18 (Railway runtime state reconciled — only ProFlow active)
**Phase 2A.12 Batch 1 update:** 2026-08-18 (history rewrite executed for Portfolio + AndaimesPini)
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
