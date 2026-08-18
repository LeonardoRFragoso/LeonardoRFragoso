# Repository Disposition — Phase 2A.10

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
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

## Backup Location

All 13 repositories were backed up before deletion:
- **Directory:** `github-deletion-backups/phase-2a-10/`
- **Format:** git mirror clone + git bundle
- **Manifest:** `DELETE_MANIFEST.md` in backup directory
