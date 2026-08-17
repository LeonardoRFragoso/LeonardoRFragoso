# Execution Plan — GitHub Portfolio Reorganization

**Account:** LeonardoRFragoso
**Phase 1 audit date:** 2026-08-17

> **Every destructive or visibility-changing operation in Phases 2–7 requires explicit human approval before execution.** No action will be taken without Leonardo's sign-off.

## Phase Summary

| Phase | Description | Destructive? | Requires Approval? |
|---|---|---|---|
| Phase 1 | Read-only audit + governance baseline (THIS PHASE — COMPLETE) | No | N/A |
| Phase 2A | Urgent exposure/security fixes | Yes (history rewrite) | Yes, per-repo |
| Phase 2B | Visibility changes (public → private) | Yes (visibility) | Yes, per-repo |
| Phase 2C | Archive stale repositories | Yes (archive) | Yes, per-repo |
| Phase 2D | Cleanup PRs and branches | Yes (close PRs, delete branches) | Yes, per-repo |
| Phase 3 | Flagship production-readiness audits | No (read-only) | N/A |
| Phase 4 | GitHub profile rewrite | No (README only) | Review before publish |
| Phase 5 | Personal portfolio rebuild | No (new code) | Review before deploy |
| Phase 6 | Software-house rebrand/site | No (new code) | Review before deploy |
| Phase 7 | Public case studies | No (new repos/docs) | Review before publish |

---
## Phase 2A — Urgent Exposure / Security Fixes

**Goal:** Rotate compromised credentials and scrub git history for all CRITICAL/HIGH findings.

**Prerequisite:** Confirm with Leonardo that all listed credentials have been ROTATED at their source (AWS, Cloudflare, MercadoPago, OpenAI, Google, GitHub, SendGrid, MelhorEnvio, database, EC2 key pairs, LinkedIn session). History scrubbing is pointless if live credentials remain active.

### Repositories Requiring History Scrubbing

| Priority | Repository | Credentials to Rotate | History Tool |
|---|---|---|---|
| CRITICAL | ProFlow | OpenAI API key, Google OAuth, GitHub OAuth, Mercado Pago token, Django secret | git-filter-repo or BFG |
| CRITICAL | base-corporativa | AWS/Cloudflare R2 keys, MercadoPago tokens, MelhorEnvio tokens, SendGrid API key, DB URL, Django superuser password | git-filter-repo or BFG |
| CRITICAL | Bot_IqOption | MercadoPago credentials, JWT trading session tokens, user API keys | git-filter-repo or BFG |
| CRITICAL | MVP-linkedin-bot | LinkedIn session tokens, Chrome profile | git-filter-repo or BFG |
| CRITICAL | FinanceControl | EC2 RSA key pair (Finance2.pem) | git-filter-repo or BFG |
| CRITICAL | Digital-Signage-Platform | DB credentials (root password), JWT secret | git-filter-repo or BFG |
| HIGH | FlowTrack | Session/CSRF tokens, SECRET_KEY | git-filter-repo or BFG |
| HIGH | Bet-IA-BOT | API-Football API key | git-filter-repo or BFG |
| HIGH | Portfolio-LeonardoFragoso-React | Remove personal/business PDFs (CNPJ card, contrato social, CV) | git-filter-repo or BFG |

### Steps (per repository, after credential rotation)

1. **Confirm rotation:** Verify all credentials have been rotated at source.
2. **Backup:** Create a full backup clone before any history rewrite.
3. **Remove from current tree:** Delete secret files, add to `.gitignore`.
4. **Scrub history:** Use `git-filter-repo` (preferred) or BFG Repo-Cleaner to remove secret files/blobs from all commits.
5. **Force-push:** `git push --force --all` and `git push --force --tags`. (Requires explicit approval.)
6. **Verify:** Run `gitleaks detect` on the rewritten repo to confirm no findings.
7. **Remove versioned artifacts:** Remove `node_modules/`, `venv/`, `.pyc`, SQLite DBs, PDFs from tree and history.

### Repositories Requiring Versioned Artifact Cleanup

| Repository | Artifacts to Remove |
|---|---|
| AndaimesPini_Project | SQL dumps |
| Bot_IqOption | venv, SQL dumps |
| Digital-Signage-Platform | large media |
| FinanceControl | binaries, SQL dumps |
| Legal-AI-Copilot | venv, build/dist, binaries, large media |
| LogiFlow | ZIP backups |
| MVP-linkedin-bot | venv, binaries, large media |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | node_modules |
| Portfolio-LeonardoFragoso-React | large media |
| SaaS | SQL dumps |
| Sistema-de-compras | binaries, SQL dumps |
| YardMaster | venv, binaries, SQL dumps |
| base-corporativa | build/dist |
| dash-monitor | binaries, large media |
| pimenta | node_modules |
| wrconsultoriaesolucoes | binaries, ZIP backups, large media |

---
## Phase 2B — Visibility Changes

**Goal:** Make private all repositories that contain client/employer IP, third-party licensed software, or are pending security/IP review.

### Repositories to Make Private

| Repository | Current | Reason | Priority |
|---|---|---|---|
| wrconsultoriaesolucoes | PUBLIC | Client project (WR Consultoria) + commercial premium WordPress plugins (Elementor Pro, Yoast SEO Premium) | HIGH |
| Digital-Signage-Platform | PUBLIC | Former employer IP (iTracker) + compromised DB credentials in history | CRITICAL |
| FlowTrack | PUBLIC | Client project (ICTSI) + session tokens in history + README still names ICTSI | HIGH |
| YardMaster | PUBLIC | Former employer IP (iTracker) + 8328 venv files + operational data in git | HIGH |
| nao-conformidade | PRIVATE | Already private (iTracker branding) — keep private | N/A |
| AndaimesPini_Project | PUBLIC | Client project (Andaimes Pini) + versioned db.sqlite3 + 18 .sqlite_backup files | HIGH |
| Sistema-de-compras | PUBLIC | Client project + README misrepresents tech stack (claims Vue/FastAPI, actual is Streamlit) | MEDIUM |
| dash-monitor | PUBLIC | Former employer IP (iTracker) + security findings | HIGH |
| base-corporativa | PUBLIC | 14 CRITICAL gitleaks findings — production credentials in tracked files | CRITICAL |
| Legal-AI-Copilot | PUBLIC | Hiring challenge with third-party case materials + versioned venv (11,836 files) | MEDIUM |
| pimenta | PUBLIC | Adult-content landing page with versioned node_modules — not professional portfolio material | LOW |
| ProFlow | PUBLIC | CRITICAL production credentials in history + seed/simulated data | CRITICAL |

### Repositories to Make Public

| Repository | Current | Reason |
|---|---|---|
| DevPro | PRIVATE | IP-safe (Category A), 0 secrets, clean tree, strong autonomous agents showcase. Fix default branch first. |

---
## Phase 2C — Archive Stale Repositories

**Goal:** Archive repositories that are no longer relevant to the professional portfolio.

### Archive Candidates

| Repository | Current | Reason |
|---|---|---|
| SGE-Django | PRIVATE | ARCHIVED_HISTORICAL — 1 commit, 2024-05-05, 25KB, stock management tutorial. No recent activity. |
| IronForceAI-Teste | PUBLIC | PROTOTYPE — hiring challenge using public CEAP data. Minimal code, not portfolio-quality. |
| aviator-banca | PRIVATE | MVP — simple CRUD app, no tests/CI/Docker. Not portfolio-relevant. |
| -Backend-Pipefy-AWS-no-Mundo-Invest | PUBLIC | Hiring challenge for Mundo Invest (Grupo EWZ Capital). Keep as historical record but archive — Pipefy integration is simulated/mock. |
| alzi-project | PRIVATE | PROTOTYPE — keep private, archive. Contains personal data spreadsheets. |
| Bet-IA-BOT | PRIVATE | ADVANCED_MVP but contains hardcoded API key. Keep private, archive after security fix. |
| Bot_IqOption | PRIVATE | ADVANCED_MVP but 201 gitleaks findings. Keep private, archive after security fix. |
| MVP-linkedin-bot | PRIVATE | MVP — LinkedIn automation bot with Chrome profile and personal data committed. Keep private, archive after security fix. |
| exnova-api | PRIVATE | MVP — exchange API wrapper. Keep private, archive. |
| FragTech-Fintech | PUBLIC | PROTOTYPE — bolt.new scaffold, 3 commits, no tests/CI/Docker. Rebuild as FragTech showcase (Phase 6). |
| SaaS | PRIVATE | MVP — generic SaaS scaffold. Keep private, archive. |
| API_Analyze | PUBLIC | ADVANCED_MVP but single commit, no tests/CI/Docker, db.sqlite3 committed. Demote to secondary or archive. |
| FinanceControl | PUBLIC | ADVANCED_MVP but CRITICAL RSA key exposure. Fix security first, then archive or rebuild. |

---
## Phase 2D — Cleanup PRs and Branches

**Goal:** Close stale PRs, delete stale branches, fix default branch anomalies.

### PRs to Close

| Repository | PR # | Classification | Action |
|---|---|---|---|
| devpro-e2e-sandbox | 5-15 | AUTOMATED_TEST_ARTIFACT | Close all 15 automated PRs, delete devpro/* and devin/* branches |
| ProFlow | 1 | STALE_CLOSE_CANDIDATE | Close WIP Copilot PR (not updated since 2025-12-22) |
| ProFlow | 2 | STALE_CLOSE_CANDIDATE | Close WIP Copilot PR (not updated since 2026-05-03) |
| YardMaster | 17 | STALE_CLOSE_CANDIDATE + BLOCKED | Close PR (12+ months stale, tests failing). Make repo private first. |
| nao-conformidade | 5 | SUPERSEDED | Close (duplicate of PR #7) |
| nao-conformidade | 7 | STALE_CLOSE_CANDIDATE | Close (12+ months stale) |
| nao-conformidade | 15 | STALE_CLOSE_CANDIDATE | Close (12+ months stale) |

### PRs to Review/Merge

| Repository | PR # | Classification | Action |
|---|---|---|---|
| DevPro | 4 | ACTIVE | Review Phase 3B provider resilience PR — appears ready for review |
| MVP-linkedin-bot | 1 | READY_TO_REVIEW | Review PT-BR numeric question fix. Address security issues first. |

### Default Branch Fixes

| Repository | Current Default | New Default | Action |
|---|---|---|---|
| DevPro | `feat/devpro-foundation` | `main` | Change default branch (main is 26 commits ahead) |
| MedFlow_Finance | `master` | `main` | Rename for consistency |
| SGE-Django | `master` | `main` | Rename, or leave if archiving |

### Branch Cleanup

| Repository | Branches | Action |
|---|---|---|
| devpro-e2e-sandbox | 17 branches (devpro/*, devin/*) | Delete all automated branches after closing PRs |
| nao-conformidade | 26 branches (codex/*) | Delete stale codex/* branches after closing PRs |
| YardMaster | 19 branches | Delete stale branches after making repo private |
| desafio-focon | 16 branches | Review and delete stale feature branches |

---
## Phase 3 — Flagship Production-Readiness Audits

**Goal:** Deep-dive into flagship showcase repos to verify and improve production readiness.

### Repositories for Deep Audit

| Repository | Focus |
|---|---|
| Pagae | Verify e2e test coverage, payment provider integration, CPF/CNPJ encryption roadmap |
| DevPro | Verify multi-executor orchestration, provider fallback, live execution reliability |
| sanduicherie | Verify E2E test coverage, CI pipeline, production deployment |
| desafio-focon | Verify Clean Architecture compliance, migration integrity, test coverage |
| vigil-ai | Verify multi-agent orchestration, async execution, audit logging |
| Go-API-Gestao | Add tests and CI to support 'production-ready' claim (or correct the claim) |
| Oraculo | Correct 'production-ready' claim. Add CI. Improve test coverage. |

---
## Phase 4 — GitHub Profile Rewrite

**Goal:** Rewrite the `LeonardoRFragoso/LeonardoRFragoso` profile README to reflect the new positioning.

- Update bio: Software Engineer | Backend Engineering | SaaS | Enterprise Systems | Applied AI | Autonomous Agents | Production Engineering
- Pin the 6 recommended repositories
- Add a concise professional summary with links to case studies
- Remove or update the `cobrinha.yml` workflow if no longer needed
- Ensure no personal data or sensitive information in the profile README

---
## Phase 5 — Personal Portfolio Rebuild

**Goal:** Rebuild `Portfolio-LeonardoFragoso-React` as a modern professional portfolio.

- Remove sensitive PDFs (CNPJ card, contrato social, CV) from public/ and git history
- Rebuild with the 6 pinned repos as featured projects
- Add sanitized case studies for private projects (WR, ICTSI, iTracker)
- Update iTracker/ICTSI references — replace with sanitized 'enterprise systems' case studies
- Deploy on Vercel/Netlify

---
## Phase 6 — Software-House Rebrand / Site

**Goal:** Rebrand and launch the software house using `PyScriptTech` as the base.

- Rebrand PyScriptTech: find/replace branding across 30+ source files, update localStorage prefixes (@pyscript:*), swap social links, update domain/Supabase project, rename 50+ docs
- Rebuild FragTech-Fintech as a genuine FragTech showcase (current is a bolt.new scaffold)
- Create software-house landing page with client cases, products, and R&D sections
- Integrate with ProFlow (after security fixes and making it private)

### Software-House Project Classification

| Category | Projects |
|---|---|
| CLIENT CASES | wrconsultoriaesolucoes (WR Consultoria), Plataforma-Cursos-WRConsultoria (WR Training), FlowTrack (ICTSI), Digital-Signage-Platform (iTracker), YardMaster (iTracker), nao-conformidade (iTracker), dash-monitor (iTracker), AndaimesPini_Project (Andaimes Pini), Sistema-de-compras (client) |
| PRODUCTS | Pagae (fintech SaaS), sanduicherie (restaurant SaaS), ProFlow (project management SaaS), Oraculo (AI data platform), PayFlow-AI (AI payments) |
| R&D / LABS | DevPro (AI agent orchestration), vigil-ai (multi-agent AI), AgentesIA-Consultoria (multi-agent AI), Bot_IqOption/exnova-api/aviator-banca (trading bots) |
| PERSONAL PORTFOLIO | LeonardoRFragoso (profile README), Portfolio-LeonardoFragoso-React (portfolio site), PyScriptTech (software-house site) |
| FORMER EMPLOYER EXPERIENCE | Digital-Signage-Platform (iTracker), YardMaster (iTracker), nao-conformidade (iTracker), dash-monitor (iTracker), FlowTrack (ICTSI) |

**Important:** FoconFlow (desafio-focon) must remain clearly labeled as a technical/product case (Category C — hiring challenge) unless explicit evidence of a commercial client engagement is found. No such evidence was found in Phase 1.

**Important:** WR Training Platform (Plataforma-Cursos-WRConsultoria) may become a commercial client case, but source code should default to private.

---
## Phase 7 — Public Case Studies

**Goal:** Create public sanitized case study repositories for private projects.

For each case study:
- Create a new public repository (e.g., `case-study-wr-training-platform`)
- Include: architecture overview, tech stack, challenges, solutions, outcomes, diagrams
- Exclude: source code, client data, credentials, production URLs, internal documentation
- Require legal review for former employer projects (iTracker, ICTSI)

### Case Study Repositories to Create

| Case Study | Source Project | Legal Review Required? |
|---|---|---|
| WR Consultoria QSMS Platform | wrconsultoriaesolucoes | Yes (commercial plugins) |
| WR Training Platform (LMS) | Plataforma-Cursos-WRConsultoria | Yes (client project) |
| ICTSI Port Terminal Operations | FlowTrack | Yes (former employer) |
| iTracker Digital Signage | Digital-Signage-Platform | Yes (former employer) |
| iTracker Yard Management | YardMaster | Yes (former employer) |
| iTracker Non-Conformity Management | nao-conformidade | Yes (former employer) |
| Transport CRM SaaS | LogiFlow | No (personal product) |
| Healthcare Financial Management | MedFlow_Finance | No (personal product) |

---
## Approval Gates

Each phase requires explicit approval before execution:

| Gate | Required Approval |
|---|---|
| Phase 2A — per repository | Leonardo confirms credentials rotated + approves history rewrite |
| Phase 2B — per repository | Leonardo approves each visibility change |
| Phase 2C — per repository | Leonardo approves each archive |
| Phase 2D — per repository | Leonardo approves each PR close / branch delete / default branch change |
| Phase 3 | Leonardo approves deep audit scope |
| Phase 4 | Leonardo reviews and approves new profile README |
| Phase 5 | Leonardo reviews and approves new portfolio |
| Phase 6 | Leonardo reviews and approves software-house brand |
| Phase 7 | Leonardo reviews and approves each case study. Legal review for employer projects. |

---
## Validation Checklist (Phase 1 Complete)

- [x] Every owned repository was inventoried (43/43)
- [x] Public/private counts reconcile (32 public, 11 private)
- [x] No repository visibility changed
- [x] No repository archived
- [x] No repository deleted
- [x] No branch deleted
- [x] No PR closed
- [x] No production system modified
- [x] No secret value printed
- [x] Audit files render correctly as Markdown
- [x] git diff contains ONLY documentation in LeonardoRFragoso/LeonardoRFragoso
