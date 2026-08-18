# Showcase Strategy — Phase 1 Audit

**Account:** LeonardoRFragoso
**Audit date:** 2026-08-17

## Proposed Public GitHub Profile Positioning

The public profile should communicate:

- **Software Engineer** — rigorous, production-minded backend engineering
- **Backend Engineering** — Python (Django/FastAPI), Go, Java/Spring
- **SaaS** — multi-tenant, payment-integrated, deploy-ready platforms
- **Enterprise Systems** — domain-driven, migration-backed, scalable
- **Applied AI** — RAG, NL2SQL, AI-powered fintech
- **Autonomous Agents** — multi-agent orchestration, async pipelines
- **Production Engineering** — CI/CD, Docker, testing, observability

## Recommended 6 Pinned Repositories

Optimized for: quality, technical depth, business credibility, diversity, real engineering evidence.

### 1. Pagae — SaaS / Fintech / Production Engineering

**Evidence:** Django + Celery + PostgreSQL + Redis + Vue. 104 tests (incl. e2e MVP flow), CI green (ruff + Django checks + migration check + pytest with coverage + Docker build + frontend build/lint/test), Docker (dev + prod), Railway deploy config. Provider-agnostic payments (PaymentProvider interface, sandbox + Celcoin scaffold). Domain-driven architecture with repository pattern + services + async events via Celery. Original Brazilian fintech brand with explicit no-IP-copy disclaimer. Honest README scopes itself as 'MVP (atual)' with a clear roadmap.

**Why pin:** Strongest overall showcase: green CI, 104 tests, clean DDD Django, Docker, deploy config, 16 docs. Covers SaaS, Production Engineering, Backend, Fintech.

**Action:** Currently PUBLIC, IP-safe (Category A). No changes needed.

### 2. DevPro — Autonomous Agents / AI Orchestration

**Evidence:** Python multi-executor AI agent orchestration platform. 27 tests, CI green, Docker, Alembic migrations. Features: Phase 2 live orchestration, Phase 3A multi-executor, Phase 3B provider fallback & resilience (PR #4). Clean tree, 0 gitleaks findings.

**Why pin:** Best autonomous agents / AI orchestration piece. Demonstrates multi-executor patterns, fallback resilience, live orchestration. High recruiting value (5/5) and current relevance (5/5).

**Action:** Currently PRIVATE. **Recommend making PUBLIC** — IP-safe (Category A), 0 secrets, clean tree. Must fix default branch first (change from `feat/devpro-foundation` to `main`).

### 3. sanduicherie — Production Engineering / SaaS

**Evidence:** Python (Django/FastAPI) restaurant SaaS. Best-in-class testing: unit + integration + E2E tests. CI with PostgreSQL service. Docker Compose. Alembic migrations. Clean git hygiene. 5 gitleaks findings are all test/dummy JWT secret placeholders (not real credentials).

**Why pin:** Demonstrates production engineering rigor: comprehensive test pyramid, CI with real DB service, Docker, migrations. Covers Production Engineering, SaaS, Backend.

**Action:** Currently PUBLIC, IP-safe (Category A). No changes needed.

### 4. desafio-focon — Enterprise Systems / Backend Engineering

**Evidence:** Python Clean Architecture challenge for Fócon Engenharia. 47 tests, 33 migrations, CI green, live Vercel deployment. Domain-driven design with entities, value objects, use cases. Fócon branding is in a hiring challenge context (Category C) — no commercial client engagement evidence.

**Why pin:** Strong enterprise systems showcase: Clean Architecture, 47 tests, 33 migrations, CI green, live deploy. Covers Enterprise Systems, Backend Engineering. High recruiting value (5/5).

**Action:** Currently PUBLIC, IP-safe (Category C — hiring challenge). No changes needed. Must remain labeled as a technical/product case, not a commercial client engagement.

### 5. vigil-ai — Applied AI / Autonomous Agents

**Evidence:** FastAPI + SQLAlchemy 2.0 + Alembic + Vue 3. 5 AI agents (LeadHunter, Enrichment, Engagement, Sales, Orchestrator) with async execution and audit logs. 29 tests. Docker Compose. Render deploy config. Mock mode for AI when API key unset. Hiring challenge for Pareto (fictional 'Vigil.AI Summit' case).

**Why pin:** Excellent multi-agent AI showcase: 5 async agents, testing, deploy readiness. Covers Applied AI, Autonomous Agents. Honest about mock mode. No IP risk (fictional case).

**Action:** Currently PUBLIC, IP-safe (Category C — hiring challenge). No changes needed.

### 6. Go-API-Gestao-de-Projetos-e-Tarefas — Backend Engineering (Go)

**Evidence:** Go/Gin clean layered architecture (handler → service → repository). JWT + RBAC auth. GORM. Vue 3 SPA frontend. Docker. Adds language diversity (Go) to the portfolio.

**Why pin:** Demonstrates Go backend engineering: clean architecture, JWT+RBAC, GORM, Docker. Covers Backend Engineering with language diversity. High recruiting value (4/5).

**Action:** Currently PUBLIC, IP-safe (Category A). No changes needed. **Caveat:** README claims 'Pronto para produção' but has ZERO tests and no CI — this claim should be corrected before pinning.

### Profile Theme Coverage

| Theme | Covered By |
|---|---|
| Software Engineer | All 6 repos |
| Backend Engineering | Pagae, desafio-focon, Go-API-Gestao, sanduicherie |
| SaaS | Pagae, sanduicherie |
| Enterprise Systems | desafio-focon |
| Applied AI | vigil-ai, DevPro |
| Autonomous Agents | DevPro, vigil-ai |
| Production Engineering | Pagae, sanduicherie |

### Language Diversity

| Language | Repos |
|---|---|
| Python | Pagae, DevPro, sanduicherie, desafio-focon, vigil-ai |
| Go | Go-API-Gestao-de-Projetos-e-Tarefas |
| TypeScript/Vue | (frontend in Pagae, vigil-ai, Go-API) |

---
## Public Case Study Recommendations (Private Code, Public Case)

These projects should have their source code made private, but deserve a public sanitized case study:

| Project | Case Study Title | Notes |
|---|---|---|
| wrconsultoriaesolucoes | WR Consultoria WordPress Site | Full WordPress production site with commercial premium plugins. Case study can describe the QSMS consulting platform, service-order management, and implementation kits without publishing licensed plugin code or client data. |
| Plataforma-Cursos-WRConsultoria | WR Training Platform (LMS/SaaS) | Multi-tenant LMS with RLS, JWT, Mercado Pago integration, 32 tests, CI, Docker. Case study can describe the architecture, multi-tenancy approach, and payment integration without exposing client-specific configuration. |
| Digital-Signage-Platform | TVS iTracker Digital Signage Platform | Corporate digital signage system for iTracker/RBT/CLIA port terminals. Case study can describe the architecture and deployment after sanitizing all corporate references and scrubbing history. **Requires legal review first.** |
| FlowTrack | ICTSI Port Terminal Operations System | Production operations system for ICTSI Rio de Janeiro. Case study can describe the operational workflows and architecture after sanitizing. **Requires legal review first.** |
| YardMaster | iTracker Yard Management System | Yard/terminal management with operational data. Case study can describe the domain and features after sanitizing. **Note:** multi-tenant/white-label claims must be corrected — they are not supported by code. |
| nao-conformidade | iTracker Non-Conformity Management | Django-based non-conformity/occurrence tracking system. Case study can describe the workflow and audit trail after sanitizing. |
| LogiFlow | Transport CRM SaaS | Full SaaS CRM for transport companies. FastAPI + Vue 3, DDD, multi-tenant, 16 test files, 4 CI/CD workflows, Helm charts, 9 Alembic migrations, 5 ADRs. Case study can describe the architecture and multi-tenancy approach. |
| MedFlow_Finance | Healthcare Financial Management | PHP/Laravel healthcare finance system. Case study can describe the domain and features after correcting the '100% ready' claim to match actual maturity (ADVANCED_MVP). |

---
## Secondary Public Repositories (Not Pinned)

These can remain public as secondary portfolio evidence but are not strong enough to pin:

- **API_Analyze** — ADVANCED_MVP — Personal financial analysis tool with no tests, CI, or Docker. Safe to keep public as a secondary project. Not showcase-worthy due to lack of testing 
- **AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes** — ADVANCED_MVP — Strong personal SaaS showcase (multi-agent AI, multi-tenant, async pipeline, billing) with good docs and deploy config. Keep public as a portfolio pie
- **-Backend-Pipefy-AWS-no-Mundo-Invest** — ADVANCED_MVP — Strong hiring-challenge artifact demonstrating Clean Architecture, testing, and GraphQL mutation design — valuable as public portfolio evidence. The M
- **FinanceControl** — ADVANCED_MVP — Strong personal product demonstrating full-stack + monetization skills, suitable for public showcase. CRITICAL prerequisite: revoke/rotate the EC2 key
- **LeonardoRFragoso** — PRODUCTION_LIKE — The central profile README repo — must remain public (it IS the GitHub profile). It will become the future central professional README per this audit'
- **Oraculo** — ADVANCED_MVP — Ambitious personal data-intelligence platform with broad architecture (NL2SQL, RAG, knowledge graph). Keep public as a showcase but tone down 'product
- **PRODERJ** — ADVANCED_MVP — Personal study tool with a live demo, original AI-generated content, and explicit disclaimers of government affiliation. Safe to keep public as a show
- **PayFlow-AI** — ADVANCED_MVP — Strong personal SaaS product demonstrating multi-tenant architecture, payments integration and conversational AI. Keep public as a showcase but remedi
- **Plataforma-de-Monitoramento-de-Sistemas-e-APIs** — ADVANCED_MVP — High technical-depth portfolio piece (Clean Architecture, Java 21, observability) that is safe to publish under MIT. Prerequisite: remove versioned no
- **Portfolio-LeonardoFragoso-React** — ADVANCED_MVP — This is the current personal portfolio that will be rebuilt after classification. It is live, public, and serves as the primary professional showcase.
