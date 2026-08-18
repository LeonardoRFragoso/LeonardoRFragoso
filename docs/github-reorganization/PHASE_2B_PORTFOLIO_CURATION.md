# Phase 2B — Portfolio Curation Audit & Action Plan

**Account:** LeonardoRFragoso
**Date:** 2026-08-18
**Phase:** 2B (Portfolio Curation — Audit, Ranking & Action Plan)
**Central docs baseline:** `64f7a75c61f7fd939878f383be09aa98c103f5ab`
**Phase 2A status:** COMPLETE — PERSONAL_PORTFOLIO_SECURITY_GATE=PASS — PHASE_2B_ALLOWED=YES

> **READ-ONLY PHASE:** No repository mutations executed. This document is an audit and action plan requiring Leonardo's explicit approval before any changes are made.

---

## Part 1 — Account Summary

| Metric | Value |
|---|---|
| Total repositories | 30 |
| Public | 15 |
| Private | 15 |
| Archived | 0 |

---

## Part 2 — Hard Provenance Exclusions

| Repository | Classification | Reason |
|---|---|---|
| Digital-Signage-Platform | PRIVATE_FORMER_EMPLOYER | ICTSI/iTracker IP — DEFERRED_EXTERNAL_OWNER_HANDOFF |
| FlowTrack | PRIVATE_FORMER_EMPLOYER | ICTSI/iTracker IP — DEFERRED_EXTERNAL_OWNER_HANDOFF |
| YardMaster | PRIVATE_FORMER_EMPLOYER | ICTSI/iTracker IP — PORTFOLIO_EXCLUDED |

**Client/IP-sensitive (remain private unless explicitly authorized):**

| Repository | Classification | Reason |
|---|---|---|
| AndaimesPini_Project | PRIVATE_CLIENT | Client work (Andaimes Pini) |
| base-corporativa | PRIVATE_CLIENT | Client e-commerce (basecorporativa.store) |
| wrconsultoriaesolucoes | PRIVATE_CLIENT | Client WordPress site (WR Consultoria) |
| Plataforma-Cursos-WRConsultoria | PRIVATE_CLIENT | Client LMS (WR Consultoria) |

---

## Part 3 — Top 6 Showcase Repositories (Ranked)

### #1 — PayFlow-AI

| Field | Value |
|---|---|
| PORTFOLIO_SCORE | 84/100 |
| VISIBILITY | PUBLIC |
| STACK | Python 3.11, FastAPI (async), SQLAlchemy 2.0, Next.js 16, TypeScript, PostgreSQL 17, Redis 7, RQ, OpenAI GPT-4o, Twilio WhatsApp, Mercado Pago, Docker, Playwright |
| WHY_SELECTED | Strongest overall: conversational AI financial SaaS with 40 backend test files, E2E tests, Docker, Railway deploy, and active development through 17 sprints. Demonstrates backend depth, AI integration, payment processing, async workers, and automated testing in a single project. |
| TECHNICAL_SIGNAL | Async FastAPI + SQLAlchemy 2.0 + Celery/RQ workers + OCR + webhooks + provider-agnostic payments + JWT auth |
| BUSINESS_SIGNAL | Real financial SaaS solving WhatsApp-based billing automation for MEIs and small businesses |
| RECRUITER_30_SECOND_SIGNAL | "AI financial assistant on WhatsApp with 40+ tests, Docker, and CI" |
| CURRENT_WEAKNESS | CI is failing (3 consecutive failures); README badge claims "629 backend tests" but test directory shows 40 test files (may be test functions within files) |
| REQUIRED_FIX_BEFORE_PINNING | Fix CI pipeline; verify test count claim in README badge matches actual test count |

### #2 — Pagae

| Field | Value |
|---|---|
| PORTFOLIO_SCORE | 79/100 |
| VISIBILITY | PUBLIC |
| STACK | Python 3.13, Django 5, DRF, JWT (simplejwt), Celery, pytest, PostgreSQL 16, Redis 7, Vue 3 + Pinia + Tailwind, Docker, GitHub Actions, Railway |
| WHY_SELECTED | Best Django architecture showcase: 10 domain-isolated apps with repository pattern, service layer, provider-agnostic payments, and CI passing. Demonstrates enterprise domain modeling and clean monolith architecture. |
| TECHNICAL_SIGNAL | 10 domain apps (accounts, merchants, customers, checkout, payments, collections, ledger, settlements, webhooks, notifications) + repository pattern + services + Celery async |
| BUSINESS_SIGNAL | Pix installment checkout SaaS — real Brazilian market problem |
| RECRUITER_30_SECOND_SIGNAL | "Django SaaS with 10 domain modules, repository pattern, CI passing, and Railway staging deploy" |
| CURRENT_WEAKNESS | Single day of commits (Jun 30, 2026); no AI component; test files exist per app but test count not verified |
| REQUIRED_FIX_BEFORE_PINNING | Add repository description and topics; verify test suite runs clean; consider adding a brief architecture diagram to README |

### #3 — Oraculo

| Field | Value |
|---|---|
| PORTFOLIO_SCORE | 72/100 |
| VISIBILITY | PUBLIC |
| STACK | Python 3.11, FastAPI, SQLAlchemy 2, Alembic, DuckDB, FAISS, NetworkX, React 18, Vite, TailwindCSS, PostgreSQL 16, Redis 7, Docker |
| WHY_SELECTED | Deepest AI engineering: NL2SQL engine, hybrid RAG (FAISS + structured data), knowledge graph extraction, anomaly detection, agent actions, and 4 LLM provider integrations. Shows Leonardo can build complex AI systems, not just call APIs. |
| TECHNICAL_SIGNAL | NL2SQL (natural language → SQL via DuckDB) + hybrid RAG (FAISS vector search + SQL) + knowledge graph (NetworkX) + semantic engine + agent action planner + subscription plans |
| BUSINESS_SIGNAL | Enterprise data intelligence platform — connects any data source and answers natural language questions |
| RECRUITER_30_SECOND_SIGNAL | "AI platform with NL2SQL, RAG, and knowledge graph — not just a chatbot" |
| CURRENT_WEAKNESS | README overclaims ("concorrente de Palantir / Databricks / Snowflake"); no CI workflows; only 7 test files; no live demo URL; 5 status/progress report MD files in root clutter the repository |
| REQUIRED_FIX_BEFORE_PINNING | Remove "concorrente de Palantir" claim from README; clean up status report files from root; add CI workflow; add repository description and topics |

### #4 — desafio-focon

| Field | Value |
|---|---|
| PORTFOLIO_SCORE | 69/100 |
| VISIBILITY | PUBLIC |
| STACK | React 19, TypeScript, Vite, Tailwind CSS v4, React Hook Form, Zod, Supabase (PostgreSQL + Auth), Row Level Security, GitHub Actions, Vercel, Playwright |
| WHY_SELECTED | Best frontend + database security showcase: React 19 + Supabase with RLS, Zod validation, 7 E2E Playwright tests, CI passing, and live production URL. Demonstrates frontend competency, database security design, and testing discipline. |
| TECHNICAL_SIGNAL | Feature-based architecture + RLS policies per role + SECURITY DEFINER functions + triggers for historical cost preservation + Zod schemas + E2E tests |
| BUSINESS_SIGNAL | Production tracking and profitability control — real business problem for project-based companies |
| RECRUITER_30_SECOND_SIGNAL | "React 19 + Supabase with Row Level Security, E2E tests, and live demo on Vercel" |
| CURRENT_WEAKNESS | No backend code (Supabase only); no AI; 5 report MD files in root (CORRECTION_REPORT, FOUNDATION_REPORT, etc.); technical test origin may be visible |
| REQUIRED_FIX_BEFORE_PINNING | Clean up report MD files from root; add repository description and topics; consider renaming if "desafio-focon" reveals test origin |

### #5 — LogiFlow

| Field | Value |
|---|---|
| PORTFOLIO_SCORE | 63/100 |
| VISIBILITY | PUBLIC |
| STACK | Python 3.11, FastAPI, SQLAlchemy, Pydantic, Celery, Vue.js 3, Vite, Pinia, TailwindCSS, PostgreSQL 15, Redis 7, Docker, Render.com |
| WHY_SELECTED | Most complex business domain: logistics SaaS with CRM + TMS + fiscal (CT-e/MDF-e) + GPS tracking + driver PWA + client portal + multi-tenant. Shows Leonardo can handle enterprise-scale domain complexity and integrations. |
| TECHNICAL_SIGNAL | Multi-tenant architecture + 4 modules (CRM, TMS, Fiscal, GPS) + Focus NFe/SEFAZ integration + Omie/Bling/Tiny ERP integration + Celery async + driver PWA offline-first |
| BUSINESS_SIGNAL | Logistics SaaS for transport companies — real, complex, high-value market |
| RECRUITER_30_SECOND_SIGNAL | "Logistics SaaS with CRM, TMS, fiscal documents, and GPS tracking — multi-tenant architecture" |
| CURRENT_WEAKNESS | No test files found; CI/CD badges in README but no .github/workflows directory found; README claims "60-70% more accessible than competitors" (unverifiable marketing claim); root directory has loose files (SETUP_RAILWAY_URLS.sh, render.yaml.bak, tasks/) |
| REQUIRED_FIX_BEFORE_PINNING | Add tests; add CI workflow or remove CI badges; remove "60-70%" marketing claim; clean up root directory; add repository description and topics |

### #6 — Go-API-Gestao-de-Projetos-e-Tarefas

| Field | Value |
|---|---|
| PORTFOLIO_SCORE | 58/100 |
| VISIBILITY | PUBLIC |
| STACK | Go 1.23, Gin, GORM, JWT, PostgreSQL 16, Vue.js 3, Pinia, Vue Router, TailwindCSS, Vue I18n, Chart.js, VueDraggable, Docker |
| WHY_SELECTED | Demonstrates Go competency and language breadth: clean layered architecture (handler → service → repository → models) with i18n, Kanban, teams, permissions, and dark mode. Shows Leonardo is not limited to Python. |
| TECHNICAL_SIGNAL | Clean architecture (cmd/api → internal/{config,database,handler,middleware,models,repository,router,service}) + JWT access/refresh + GORM + Vue 3 full frontend |
| BUSINESS_SIGNAL | Project/task management SaaS with teams, Kanban, and real-time notifications |
| RECRUITER_30_SECOND_SIGNAL | "Go + Vue 3 SaaS with clean layered architecture — shows language breadth beyond Python" |
| CURRENT_WEAKNESS | No tests; no CI; no live demo URL; PHASE_1_CLOSURE.md and PHASE_1_SUMMARY.md in root reveal incomplete status; escopo.txt in root |
| REQUIRED_FIX_BEFORE_PINNING | Add tests; add CI workflow; remove PHASE_1_* and escopo.txt from root; add repository description and topics; consider renaming to "TaskFlow" (README title) |

---

## Part 4 — README Overclaim Findings

| Repository | Claim | Verdict | Factual Replacement |
|---|---|---|---|
| Oraculo | "concorrente de Palantir / Databricks / Snowflake" | README_OVERCLAIM | "Plataforma de inteligência sobre dados com NL2SQL, RAG e knowledge graph" |
| Oraculo | "Não é um chatbot" | MISLEADING | It has a chat interface — clarify: "Não é apenas um chatbot — inclui NL2SQL, RAG e graph" |
| LogiFlow | "60-70% mais acessível que concorrentes" | README_OVERCLAIM | Remove — no pricing evidence to support this claim |
| LogiFlow | CI/CD badges showing passing | MISLEADING | No .github/workflows directory found — badges link to non-existent workflows |
| PayFlow-AI | "629 backend tests" badge | UNVERIFIED | 40 test files found — may contain 629 test functions, but this should be verified |
| FlowTrack | "Em Produção" badge | PLAUSIBLE | README claims production at ICTSI — consistent with audit evidence (but repo is PRIVATE_FORMER_EMPLOYER) |
| Digital-Signage-Platform | "White Label Ready" | UNVERIFIED | No white-label transformation code visible in structure |
| FragTech-Fintech | "AI-powered financial platform" | README_OVERCLAIM | No AI implementation visible in code structure — remove "AI-powered" claim |
| SaaS | "Ecossistema SaaS" with 6 products | README_OVERCLAIM | Only 1 product (BI-as-a-Service) has any implementation — 5 are "Planejados" |

---

## Part 5 — Test Evidence Summary

### Projects with strong test evidence

| Repository | Test files | Framework | E2E | CI |
|---|---|---|---|---|
| PayFlow-AI | 40 backend test files | pytest | Playwright (10 scenarios) | YES (failing) |
| DevPro | 16 test files | pytest | NO | YES (passing) |
| Legal-AI-Copilot | 12 test files | pytest | NO | YES (failing) |
| Pagae | Test dirs for 10 apps | pytest | YES (e2e dir) | YES (passing) |
| desafio-focon | 7 E2E test files | Playwright | YES (7 specs) | YES (passing) |
| Oraculo | 7 test files | pytest | NO | NO |
| wrconsultoriaesolucoes | 40+ test files | Playwright | YES (16 suites) | NO |
| Plataforma-Cursos-WRConsultoria | Unknown | Unknown | NO | YES (passing) |
| vigil-ai | 3 test files | pytest | NO | NO |
| devpro-e2e-sandbox | 1 test file | pytest | NO | YES (passing) |

### Projects with weak/no test evidence

| Repository | Tests | CI |
|---|---|---|
| LogiFlow | NONE found | Badges only (no workflows) |
| Go-API-Gestao-de-Projetos-e-Tarefas | NONE | NONE |
| API_Analyze | NONE | NONE |
| FragTech-Fintech | NONE | NONE |
| MedFlow_Finance | NONE | NONE |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | NONE | NONE |
| PyScriptTech | NONE | NONE |
| Portfolio-LeonardoFragoso-React | NONE | NONE |
| ProFlow | 9 test files | YES (failing — pre-existing) |
| AndaimesPini_Project | NONE | NONE |
| base-corporativa | NONE | NONE |
| FinanceControl | NONE | NONE |
| SaaS | NONE | NONE |
| exnova-api | NONE | YES (failing) |
| Bot_IqOption | NONE | NONE |
| MVP-linkedin-bot | NONE | NONE |
| Digital-Signage-Platform | NONE | NONE |
| FlowTrack | NONE | NONE |
| YardMaster | NONE | NONE |

---

## Part 6 — CI Health Findings

| Repository | CI Workflows | Recent Status | Notes |
|---|---|---|---|
| Pagae | ci.yml | PASSING (3/3) | Healthy |
| desafio-focon | ci.yml | PASSING (3/3) | Healthy |
| DevPro | ci.yml | PASSING (2/2) | Healthy |
| Plataforma-Cursos-WRConsultoria | ci.yml | PASSING (2/2) | Healthy |
| devpro-e2e-sandbox | ci.yml | PASSING (2/2) | Healthy |
| PayFlow-AI | ci.yml | FAILING (3/3) | Needs investigation |
| Legal-AI-Copilot | ci.yml | FAILING (3/3) | Needs investigation |
| ProFlow | ci.yml + migrations.yml | FAILING (both) | Pre-existing — not caused by Phase 2A |
| exnova-api | Unknown | FAILING (2/2) | Needs investigation |
| Bot_IqOption | None (dependabot only) | N/A | No CI |
| All others | None | N/A | No CI |

---

## Part 7 — Demo/Production Findings

| Repository | Demo/Production URL | Status | Notes |
|---|---|---|---|
| ProFlow | https://www.proflow.pro | LIVE (HTTP 200) | Active commercial SaaS on Railway + Vercel |
| base-corporativa | https://basecorporativa.store | Claimed live | Client e-commerce |
| PayFlow-AI | https://assistente-financeiro-whatsapp.vercel.app | Claimed live | Demo frontend |
| desafio-focon | https://desafio-focon.vercel.app | LIVE | Production MVP |
| LogiFlow | https://logi-flow-wuhp.vercel.app | Claimed live | Demo frontend |
| AndaimesPini_Project | https://andaimes-pini-project.vercel.app | Claimed live | Client project |
| wrconsultoriaesolucoes | https://wrconsultoriaesolucoes.com.br | Claimed live | Client WordPress site |
| Portfolio-LeonardoFragoso-React | https://portfolio-leonardo-fragoso-react.vercel.app | Claimed live | Old portfolio |
| PyScriptTech | https://pyscript.tech | Claimed live | Company website |
| Bot_IqOption | https://bot-iq-option.vercel.app | Claimed live | Educational bot dashboard |

---

## Part 8 — Professional Positioning

### PRIMARY_POSITIONING

**Python Backend / Full Stack Engineer with Applied AI**

Rationale based on repository evidence:
- Strongest repos are Python backend (FastAPI, Django) with full-stack delivery
- AI work is substantive (NL2SQL, RAG, knowledge graph, agent orchestration) — not just API wrappers
- Production SaaS experience (ProFlow, base-corporativa) demonstrates product engineering
- Go competency adds breadth but Python is clearly the primary stack
- Testing discipline exists in top repos (PayFlow-AI: 40 test files, desafio-focon: 7 E2E)

### SECONDARY_POSITIONING

**SaaS / Product Engineer**

Rationale:
- Multiple SaaS products built (ProFlow, Pagae, PayFlow-AI, LogiFlow, Go-API TaskFlow)
- Production deployment experience (Railway, Vercel, Docker, CI/CD)
- Payment integration expertise (Mercado Pago, Celcoin, Asaas)
- Multi-tenant architecture experience (LogiFlow, MedFlow_Finance)

> Avoid "Full Stack Developer" as primary — it dilutes the backend depth signal. Avoid "AI Engineer" as primary — the AI work is strong but embedded in full-stack products, not standalone AI research.

---

## Part 9 — Recruiter 30-Second Assessment

**What does Leonardo specialize in?**
Python backend engineering with SaaS products and applied AI. The profile README clearly states "Backend Software Engineer | Python · Django · FastAPI | SaaS · Applied AI."

**What technologies look strongest?**
Python (FastAPI, Django), PostgreSQL, Vue.js, Docker, AI/LLM (OpenAI, RAG, NL2SQL). Testing with pytest and Playwright.

**Is there evidence of production software?**
YES — ProFlow (proflow.pro) is a live commercial SaaS. base-corporativa is a live e-commerce. Multiple Vercel demos. This is the strongest signal on the profile.

**Is there evidence of backend architecture?**
YES — Pagae (10 domain apps, repository pattern, service layer), Oraculo (modular architecture with 7 subsystems), LogiFlow (multi-tenant, 4 modules). Clean architecture patterns visible.

**Is there evidence of Full Stack ability?**
YES — Most repos include both backend and frontend (Vue 3 or React). desafio-focon shows frontend-only competency with Supabase.

**Is there meaningful AI work?**
YES — Oraculo (NL2SQL, RAG, knowledge graph), PayFlow-AI (GPT-4o for intent classification, OCR), Legal-AI-Copilot (agent router, guardrails), DevPro (autonomous dev orchestration with OpenAI + Devin). This is applied AI in products, not tutorials.

**Does he test software?**
YES in top repos — PayFlow-AI (40 test files + E2E), desafio-focon (7 E2E), DevPro (16 tests). But MANY repos have zero tests, which weakens the overall signal.

**Which project should the recruiter open first?**
Currently: ProFlow case study in the profile README is the best first impression. After Phase 2B execution: **PayFlow-AI** should be the first pinned repo (strongest public repo with tests, AI, Docker, and payments).

**Current profile weaknesses:**
1. 15 public repos but only 5-6 are showcase quality — weak public repos dilute credibility
2. Several repos have no tests and no CI (LogiFlow, Go-API, API_Analyze, FragTech-Fintech)
3. Profile README links to Digital-Signage-Platform (former-employer repo that is PRIVATE — link returns 404)
4. Two portfolio repos (Portfolio-LeonardoFragoso-React + profile README) duplicate the same signal
5. README overclaims in Oraculo and LogiFlow reduce trust
6. Root directory clutter in several repos (report MD files, escopo.txt, PHASE_1_* files)

---

## Part 10 — Client / Software-House Assessment

**Which repositories prove Leonardo can deliver SaaS?**
- ProFlow (PRIVATE — live commercial SaaS with paying users)
- Pagae (Pix installment checkout SaaS with staging deploy)
- PayFlow-AI (WhatsApp financial SaaS with Railway deploy)
- LogiFlow (logistics SaaS with multi-tenant architecture)

**Which repositories prove internal platforms?**
- Digital-Signage-Platform (PRIVATE — corporate TV management, former employer)
- FlowTrack (PRIVATE — port operations management, former employer)
- YardMaster (PRIVATE — yard management, former employer)
- base-corporativa (PRIVATE — e-commerce platform, client)

**Which repositories prove AI systems?**
- Oraculo (NL2SQL, RAG, knowledge graph — most sophisticated AI)
- PayFlow-AI (GPT-4o intent classification, OCR)
- Legal-AI-Copilot (agent router, guardrails, human review)
- DevPro (PRIVATE — autonomous dev orchestrator with OpenAI + Devin)

**Which repositories prove APIs?**
- All top 6 repos have REST APIs with documentation (OpenAPI/Swagger or DRF docs)
- Go-API demonstrates Go API competency
- MedFlow_Finance demonstrates PHP/Laravel API competency

**Which repositories prove dashboards?**
- LogiFlow (CRM dashboard, TMS dashboard, analytics)
- desafio-focon (financial dashboard, admin approval dashboard)
- Go-API (project dashboard with Chart.js)
- ProFlow (PRIVATE — freelancer dashboard)

**Which repositories prove automation?**
- PayFlow-AI (WhatsApp automation, scheduled reminders, webhooks)
- DevPro (PRIVATE — autonomous development orchestration)
- MVP-linkedin-bot (PRIVATE — LinkedIn auto-applicant)
- Bot_IqOption (PRIVATE — trading bot automation)

**Which repositories prove production deployments?**
- ProFlow (Railway + Vercel — live, healthy)
- base-corporativa (Railway — live e-commerce)
- desafio-focon (Vercel — live MVP)
- PayFlow-AI (Railway — deployed)

**Commercial confidence assessment:**
Leonardo demonstrates the ability to deliver production SaaS, internal platforms, AI systems, and automation. The strongest commercial confidence signals are ProFlow (live commercial product) and the breadth of domains covered (finance, logistics, legal, e-commerce, port operations). The weakness is that most client work is private, so a commercial client evaluating the public profile sees fewer production examples than actually exist.

---

## Part 11 — Proposed Pin Order (Exactly 6)

| Pin | Repository | Score | Primary Signal |
|---|---|---|---|
| #1 | PayFlow-AI | 84 | FastAPI + AI + payments + 40 tests + Docker + Railway |
| #2 | Pagae | 79 | Django 5 + 10 domain apps + repository pattern + CI passing |
| #3 | Oraculo | 72 | NL2SQL + RAG + knowledge graph — deepest AI engineering |
| #4 | desafio-focon | 69 | React 19 + Supabase RLS + E2E tests + live on Vercel |
| #5 | LogiFlow | 63 | Logistics SaaS + multi-tenant + fiscal + GPS — domain complexity |
| #6 | Go-API-Gestao-de-Projetos-e-Tarefas | 58 | Go + clean architecture + Vue 3 — language breadth |

**Collective signal coverage:**
- Python/FastAPI: PayFlow-AI, Oraculo, LogiFlow (3)
- Python/Django: Pagae (1)
- Go: Go-API (1)
- TypeScript/React: desafio-focon (1)
- AI/LLM: PayFlow-AI, Oraculo (2)
- Testing: PayFlow-AI (40 files), desafio-focon (7 E2E), Pagae (per-app)
- CI/CD: PayFlow-AI, Pagae, desafio-focon (3)
- Docker: all 6
- Payments: PayFlow-AI, Pagae (2)
- Multi-tenant: LogiFlow (1)
- Database security: desafio-focon (RLS) (1)
- Business domains: finance, Pix payments, data intelligence, production tracking, logistics, project management

---

## Part 12 — Proposed Visibility Changes

### PUBLIC_TO_PRIVATE (5 repos)

| Repository | Reason |
|---|---|
| API_Analyze | Tutorial-level Streamlit app — no tests, no CI, no Docker. Weakens profile credibility. |
| FragTech-Fintech | "AI-powered" claim unsupported — no AI visible. No tests, no CI. Stale (Jan 2026). |
| PyScriptTech | Company marketing website — low code value. Better represented by ProFlow case study. |
| Portfolio-LeonardoFragoso-React | Duplicates profile README signal. Old portfolio site. |
| MedFlow_Finance | PHP/Laravel — not Leonardo's primary stack. No tests, no CI. 20+ SPRINT report files clutter root. |

### PRIVATE_TO_PUBLIC (0 repos)

No private repos recommended for public visibility. ProFlow and DevPro should remain private with case studies instead.

### ARCHIVE_CANDIDATE (1 repo)

| Repository | Reason |
|---|---|
| SaaS | Only 1 of 6 planned products implemented. README is mostly planning. Last commit Jan 2026. Prototype abandoned. |

### KEEP_PUBLIC_SHOWCASE (6 repos)

PayFlow-AI, Pagae, Oraculo, desafio-focon, LogiFlow, Go-API-Gestao-de-Projetos-e-Tarefas

### KEEP_PUBLIC_SUPPORTING (3 repos)

| Repository | Reason |
|---|---|
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | Shows Java 21 + Spring Boot + Clean Architecture competency — valuable for language breadth |
| LeonardoRFragoso | Profile README repo — must remain public |
| Legal-AI-Copilot | AI + legal domain + RBAC — decent supporting signal after root cleanup |

### KEEP_PRIVATE (15 repos)

ProFlow, DevPro, AndaimesPini_Project, base-corporativa, wrconsultoriaesolucoes, Plataforma-Cursos-WRConsultoria, FinanceControl, Bot_IqOption, MVP-linkedin-bot, exnova-api, devpro-e2e-sandbox, Digital-Signage-Platform, FlowTrack, YardMaster, SaaS (archive)

---

## Part 13 — Case Study Candidates

| Repository | Case Study Recommended? | Rationale |
|---|---|---|
| ProFlow | YES — HIGH PRIORITY | Live commercial SaaS, production architecture, AI integration, payment webhooks, real-time. Case study can showcase without exposing proprietary source. |
| DevPro | YES — MEDIUM PRIORITY | Unique concept (autonomous dev orchestrator). Case study can explain architecture, state machine, and AI orchestration without exposing source. |
| Digital-Signage-Platform | NO | Former-employer IP — excluded from portfolio |
| FlowTrack | NO | Former-employer IP — excluded from portfolio |
| base-corporativa | MAYBE | Client e-commerce in production — case study possible with client permission |

**Case study content guidelines (for ProFlow and DevPro):**
- Problem, architecture, stack, engineering challenges, system diagrams, testing approach, deployment architecture, technical decisions, lessons learned
- Must NOT expose: secrets, production env, customer data, client IP, proprietary source code
- Do NOT create case-study repositories yet — requires Leonardo's approval

---

## Part 14 — README Audit for Top 6

| Repository | README Status | Issues |
|---|---|---|
| PayFlow-AI | README_READY | Minor: verify "629 backend tests" badge claim; CI failing |
| Pagae | README_NEEDS_MINOR_WORK | Missing: demo URL, known limitations section; add architecture diagram |
| Oraculo | README_NEEDS_REWRITE | Remove "Palantir competitor" claim; clean up 5 status report files from root; add demo URL or note |
| desafio-focon | README_NEEDS_MINOR_WORK | Clean up 5 report MD files from root; consider renaming if test origin is undesirable |
| LogiFlow | README_NEEDS_REWRITE | Remove "60-70%" marketing claim; remove fake CI/CD badges; add tests; clean up root files |
| Go-API-Gestao-de-Projetos-e-Tarefas | README_NEEDS_REWRITE | Remove PHASE_1_* files; remove escopo.txt; add tests; add CI; consider renaming to "TaskFlow" |

---

## Part 15 — Metadata Audit for Top 6

| Repository | Proposed Description | Proposed Topics | Demo/Homepage |
|---|---|---|---|
| PayFlow-AI | WhatsApp financial assistant with AI — FastAPI, Next.js, OpenAI GPT-4o, payments | python, fastapi, ai, whatsapp, saas, payments, openai, docker, pytest, nextjs | https://assistente-financeiro-whatsapp.vercel.app |
| Pagae | Pix installment checkout SaaS — Django 5, DRF, Vue 3, Celery, PostgreSQL | python, django, saas, payments, pix, vue, docker, celery, postgresql, drf | (staging URL if available) |
| Oraculo | AI data intelligence platform with NL2SQL, RAG, and knowledge graph — FastAPI, React | python, fastapi, ai, nl2sql, rag, knowledge-graph, duckdb, faiss, react, docker | (none currently) |
| desafio-focon | Production tracking and profitability MVP — React 19, Supabase, RLS, Playwright | react, typescript, supabase, rls, vitest, playwright, tailwind, zod | https://desafio-focon.vercel.app |
| LogiFlow | Logistics SaaS: CRM + TMS + fiscal + GPS for transport companies — FastAPI, Vue 3 | python, fastapi, saas, logistics, crm, tms, vue, postgresql, redis, celery, multi-tenant | https://logi-flow-wuhp.vercel.app |
| Go-API-Gestao-de-Projetos-e-Tarefas | Project management SaaS with Kanban and teams — Go, Gin, Vue 3 | go, gin, vue, saas, project-management, postgresql, docker, jwt, clean-architecture | (none currently) |

---

## Part 16 — Proposed Profile README Structure

**Current state:** The profile README is already good — it has a clear positioning, ProFlow case study, project table, stack, and contact links. Issues: links to Digital-Signage-Platform (private, 404), no link to PayFlow-AI or Pagae, and the "Outros projetos em destaque" table includes a former-employer repo.

**Proposed new structure:**

```
1. Leonardo Fragoso — name + title
2. Professional positioning: "Python Backend / Full Stack Engineer | SaaS · Applied AI"
3. Concise value proposition (2-3 lines)
4. Core stack (compact code block — keep current format)
5. Selected engineering projects (Top 6 table with links + 1-line descriptions)
6. Product / production experience (ProFlow case study — keep current, it's strong)
7. AI / backend focus (brief paragraph — keep current "IA aplicada" competency)
8. Contact links (LinkedIn, Email, PyScript.Tech)
```

**Changes needed:**
- Remove Digital-Signage-Platform from "Outros projetos em destaque" (private, 404)
- Add PayFlow-AI and Pagae to the projects table
- Replace "3+ anos de experiência" stat with verified claim
- Remove "6 sistemas corporativos" claim (refers to former-employer work that can't be verified publicly)
- Keep ProFlow case study section — it's the strongest signal
- Add DevPro as a brief mention (case study candidate)
- Ensure all linked repos are PUBLIC

**Do NOT modify README yet — requires approval.**

---

## Part 17 — 30-Repository Action Matrix

| REPOSITORY | VISIBILITY_NOW | PRIMARY_CLASSIFICATION | PORTFOLIO_SCORE | TECH_SIGNAL | BUSINESS_SIGNAL | README_STATUS | TEST_STATUS | CI_STATUS | DEMO_STATUS | SECURITY_STATUS | PROVENANCE | RECOMMENDED_VISIBILITY | ARCHIVE_RECOMMENDATION | PIN_RECOMMENDATION | CASE_STUDY | ACTION_REQUIRED |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PayFlow-AI | PUBLIC | SHOWCASE_TOP_6 | 84 | FastAPI+AI+payments+async | WhatsApp financial SaaS | README_READY | 40 files + E2E | FAILING | LIVE (Vercel) | CLEAN (Phase 2A.13) | Original | KEEP_PUBLIC_SHOWCASE | NO | PIN #1 | NO | Fix CI; verify test count |
| Pagae | PUBLIC | SHOWCASE_TOP_6 | 79 | Django+10 domain apps+CI | Pix installment checkout | NEEDS_MINOR | Per-app test dirs | PASSING | Staging (Railway) | N/A | Original | KEEP_PUBLIC_SHOWCASE | NO | PIN #2 | NO | Add description+topics; add architecture diagram |
| Oraculo | PUBLIC | SHOWCASE_TOP_6 | 72 | NL2SQL+RAG+knowledge graph | Enterprise data intelligence | NEEDS_REWRITE | 7 files | NONE | NONE | N/A | Original | KEEP_PUBLIC_SHOWCASE | NO | PIN #3 | NO | Remove Palantir claim; clean root; add CI |
| desafio-focon | PUBLIC | SHOWCASE_TOP_6 | 69 | React19+Supabase RLS+E2E | Production tracking MVP | NEEDS_MINOR | 7 E2E specs | PASSING | LIVE (Vercel) | N/A | Semi-original | KEEP_PUBLIC_SHOWCASE | NO | PIN #4 | NO | Clean root report files; add description+topics |
| LogiFlow | PUBLIC | SHOWCASE_TOP_6 | 63 | FastAPI+multi-tenant+fiscal | Logistics SaaS | NEEDS_REWRITE | NONE | FAKE BADGES | LIVE (Vercel) | CLEAN (Phase 2A.13) | Original | KEEP_PUBLIC_SHOWCASE | NO | PIN #5 | NO | Add tests; remove fake badges; remove marketing claim |
| Go-API-Gestao-de-Projetos-e-Tarefas | PUBLIC | SHOWCASE_TOP_6 | 58 | Go+clean architecture+Vue3 | Project management SaaS | NEEDS_REWRITE | NONE | NONE | NONE | N/A | Original | KEEP_PUBLIC_SHOWCASE | NO | PIN #6 | NO | Add tests+CI; clean root; consider rename to TaskFlow |
| Legal-AI-Copilot | PUBLIC | PUBLIC_SUPPORTING | 63 | FastAPI+AI+RBAC+guardrails | Legal contract analysis | NEEDS_WORK | 12 files | FAILING | NONE | N/A | Original | KEEP_PUBLIC_SUPPORTING | NO | NO | NO | Clean root (40+ report files); fix CI |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | PUBLIC | PUBLIC_SUPPORTING | 52 | Java21+Spring Boot+Clean Arch | APM monitoring platform | README_READY | NONE | NONE | NONE | N/A | Original | KEEP_PUBLIC_SUPPORTING | NO | NO | NO | Add tests; add CI; consider if Java is relevant for positioning |
| LeonardoRFragoso | PUBLIC | PROFILE_INFRASTRUCTURE | N/A | N/A | N/A | NEEDS_UPDATE | N/A | N/A | N/A | N/A | Original | KEEP_PUBLIC | NO | N/A | NO | Update profile README per Part 16 |
| API_Analyze | PUBLIC | MAKE_PRIVATE_CANDIDATE | 30 | Streamlit+yFinance tutorial | B3 stock analysis | README_READY | NONE | NONE | NONE | CLEAN (Phase 2A.14) | Tutorial-level | MAKE_PRIVATE | NO | NO | NO | Make private — weakens profile credibility |
| FragTech-Fintech | PUBLIC | MAKE_PRIVATE_CANDIDATE | 35 | React+Node+Prisma | "AI-powered" financial (no AI) | README_OVERCLAIM | NONE | NONE | NONE | N/A | Original | MAKE_PRIVATE | NO | NO | NO | Make private — unsupported AI claim; stale |
| PyScriptTech | PUBLIC | MAKE_PRIVATE_CANDIDATE | 30 | React company website | Marketing site | README_READY | NONE | NONE | LIVE (pyscript.tech) | N/A | Original | MAKE_PRIVATE | NO | NO | NO | Make private — marketing site, low code value |
| Portfolio-LeonardoFragoso-React | PUBLIC | MAKE_PRIVATE_CANDIDATE | 35 | React+TypeScript portfolio | Old portfolio site | README_READY | NONE | NONE | LIVE (Vercel) | CLEAN (Phase 2A.12) | Original | MAKE_PRIVATE | NO | NO | NO | Make private — duplicates profile README |
| MedFlow_Finance | PUBLIC | MAKE_PRIVATE_CANDIDATE | 55 | Laravel11+Vue3 multi-tenant | Medical billing SaaS | NEEDS_WORK | NONE | NONE | NONE | N/A | Original | MAKE_PRIVATE | NO | NO | NO | Make private — not primary stack; cluttered root |
| ProFlow | PRIVATE | PRIVATE_STRATEGIC | 87 | Django+Vue3+AI+payments+real-time | Freelancer SaaS (PRODUCTION) | README_READY | 9 files | FAILING (pre-existing) | LIVE (proflow.pro) | CLEAN (Phase 2A.15) | Original | KEEP_PRIVATE | NO | N/A | YES (high priority) | Do not make public — case study instead |
| DevPro | PRIVATE | PRIVATE_STRATEGIC | 68 | OpenAI+Devin+state machine | Autonomous dev orchestrator | NEEDS_WORK | 16 files | PASSING | NONE | N/A | Original | KEEP_PRIVATE | NO | N/A | YES (medium priority) | Do not make public — case study instead |
| AndaimesPini_Project | PRIVATE | PRIVATE_CLIENT | 40 | React+Django rental mgmt | Client rental system | README_READY | NONE | NONE | LIVE (Vercel) | CLEAN (Phase 2A.12) | Client work | KEEP_PRIVATE | NO | N/A | NO | Do not expose — client IP |
| base-corporativa | PRIVATE | PRIVATE_CLIENT | 50 | React+Django+MercadoPago | Client e-commerce (PRODUCTION) | README_READY | NONE | NONE | LIVE (basecorporativa.store) | CLEAN (Phase 2A.13) | Client work | KEEP_PRIVATE | NO | N/A | MAYBE | Do not expose — client IP |
| wrconsultoriaesolucoes | PRIVATE | PRIVATE_CLIENT | 45 | PHP/WordPress+Playwright | Client WordPress site | README_READY | 40+ Playwright | NONE | LIVE (wrconsultoriaesolucoes.com.br) | N/A | Client work | KEEP_PRIVATE | NO | N/A | NO | Do not expose — client IP |
| Plataforma-Cursos-WRConsultoria | PRIVATE | PRIVATE_CLIENT | 48 | FastAPI+Vue3 LMS | Client LMS platform | README_READY | Unknown | PASSING | NONE | N/A | Client work | KEEP_PRIVATE | NO | N/A | NO | Do not expose — client IP |
| FinanceControl | PRIVATE | PRIVATE_INTERNAL | 38 | Flutter+Django+MercadoPago | Personal finance app | README_READY | NONE | NONE | NONE | CLEAN (Phase 2A.13) | Original | KEEP_PRIVATE | NO | N/A | NO | No action — internal project |
| SaaS | PRIVATE | ARCHIVE_CANDIDATE | 25 | Python+TS BI-as-a-Service | BI SaaS (1 of 6 planned) | README_OVERCLAIM | NONE | NONE | NONE | N/A | Original | KEEP_PRIVATE | YES | N/A | NO | Archive — only 1 of 6 products implemented; abandoned |
| exnova-api | PRIVATE | PRIVATE_INTERNAL | 30 | Python trading bot | Exnova MHI bot | README_READY | NONE | FAILING | NONE | N/A | Original | KEEP_PRIVATE | NO | N/A | NO | No action — internal/trading bot |
| devpro-e2e-sandbox | PRIVATE | PRIVATE_INTERNAL | 20 | Python calculator | DevPro E2E test target | README_READY | 1 file | PASSING | NONE | N/A | Original | KEEP_PRIVATE | NO | N/A | NO | No action — test infrastructure |
| Bot_IqOption | PRIVATE | PRIVATE_INTERNAL | 25 | Python+TS trading bot | IQ Option bot (educational) | README_READY | NONE | NONE | LIVE (Vercel) | CLEAN (Phase 2A.14) | Original | KEEP_PRIVATE | NO | N/A | NO | No action — educational bot |
| MVP-linkedin-bot | PRIVATE | PRIVATE_INTERNAL | 25 | Python+Selenium+Streamlit | LinkedIn auto-applicant | README_READY | NONE | NONE | NONE | CLEAN (Phase 2A.14) | Original | KEEP_PRIVATE | NO | N/A | NO | No action — personal automation |
| Digital-Signage-Platform | PRIVATE | PRIVATE_FORMER_EMPLOYER | N/A | Flask+React+Socket.IO+Redis | Corporate TV management | README_READY | NONE | NONE | NONE | DEFERRED (Phase 2A.16) | Former employer | KEEP_PRIVATE | NO | N/A | NO | DO NOT MODIFY — DEFERRED_EXTERNAL_OWNER_HANDOFF |
| FlowTrack | PRIVATE | PRIVATE_FORMER_EMPLOYER | N/A | Flask+Bootstrap port ops | Port operations (PRODUCTION at ICTSI) | README_READY | NONE | NONE | NONE | DEFERRED (Phase 2A.16) | Former employer | KEEP_PRIVATE | NO | N/A | NO | DO NOT MODIFY — DEFERRED_EXTERNAL_OWNER_HANDOFF |
| YardMaster | PRIVATE | PRIVATE_FORMER_EMPLOYER | N/A | Flask+SQLite yard mgmt | Yard/parking management | README_READY | NONE | NONE | NONE | N/A | Former employer | KEEP_PRIVATE | NO | N/A | NO | DO NOT MODIFY — PORTFOLIO_EXCLUDED |

---

## Part 18 — Proposed Mutation Sets

### PUBLIC_TO_PRIVATE (5)
1. API_Analyze
2. FragTech-Fintech
3. PyScriptTech
4. Portfolio-LeonardoFragoso-React
5. MedFlow_Finance

### PRIVATE_TO_PUBLIC (0)
None.

### ARCHIVE (1)
1. SaaS

### KEEP_PUBLIC_SHOWCASE (6)
1. PayFlow-AI
2. Pagae
3. Oraculo
4. desafio-focon
5. LogiFlow
6. Go-API-Gestao-de-Projetos-e-Tarefas

### KEEP_PUBLIC_SUPPORTING (3)
1. Plataforma-de-Monitoramento-de-Sistemas-e-APIs
2. LeonardoRFragoso (profile README)
3. Legal-AI-Copilot

### KEEP_PRIVATE (15)
ProFlow, DevPro, AndaimesPini_Project, base-corporativa, wrconsultoriaesolucoes, Plataforma-Cursos-WRConsultoria, FinanceControl, Bot_IqOption, MVP-linkedin-bot, exnova-api, devpro-e2e-sandbox, Digital-Signage-Platform, FlowTrack, YardMaster, SaaS (archive)

### CASE_STUDY_CREATE (2 candidates — do NOT create yet)
1. ProFlow (high priority)
2. DevPro (medium priority)

### README_REWRITE (3)
1. Oraculo — remove Palantir claim, clean root
2. LogiFlow — remove marketing claim, remove fake badges, clean root
3. Go-API-Gestao-de-Projetos-e-Tarefas — clean root, consider rename

### README_MINOR_UPDATE (3)
1. PayFlow-AI — verify test count badge
2. Pagae — add architecture diagram, demo URL
3. desafio-focon — clean root report files

### METADATA_UPDATE (6 — all Top 6)
1. PayFlow-AI — add description, topics, homepage
2. Pagae — add description, topics
3. Oraculo — add description, topics
4. desafio-focon — add description, topics, homepage
5. LogiFlow — add description, topics, homepage
6. Go-API-Gestao-de-Projetos-e-Tarefas — add description, topics

---

## Part 19 — Post-Execution Visibility Projection

If all proposed changes are executed:

| Metric | Current | Projected |
|---|---|---|
| PUBLIC | 15 | 9 (6 showcase + 3 supporting) |
| PRIVATE | 15 | 21 (15 current private + 5 made private + 1 archived) |
| TOTAL | 30 | 30 |

---

## Part 20 — Validators

| Validator | Result |
|---|---|
| validate_credential_matrix.py | PASS — Total items: 41, ALL VALIDATIONS PASSED |
| validate_history_sanitization_plan.py --live | PASS — COMPLETED=10, READY=0, BLOCKED=2, 15/15/30 visibility, live GitHub existence confirmed |

---

## Safety Confirmations

- No repository history rewritten: YES
- No force push: YES
- Former-employer repositories untouched: YES (Digital-Signage-Platform, FlowTrack, YardMaster)
- ProFlow production untouched: YES
- No credentials modified: YES
- No sessions modified: YES
- No secret values printed: YES
- No GitHub Support ticket submitted: YES
- No Phase 2B mutations executed: YES — this is an audit and action plan only
- No repository visibility changed: YES
- No repositories archived: YES
- No READMEs modified: YES
- No topics/descriptions changed: YES
- No profile README modified: YES

---

## Phase 2B.1 — Final Showcase Reconciliation & Execution Readiness

**Date:** 2026-08-18
**Phase:** 2B.1 (Evidence-Based Reconciliation)
**Status:** READ-ONLY — No mutations executed
**Baseline:** Merged main `04b5cd9241328bde31051882d8dba57d12d877b3` (PR #16)

> This section reconciles the Phase 2B audit with execution-ready evidence. All test suites were run locally in isolated environments. No repository mutations were performed.

---

### 1. Top 6 Slot #6 — Mandatory Re-Evaluation

#### Head-to-Head: Go-API vs Legal-AI-Copilot vs vigil-ai

| Dimension | Go-API | Legal-AI-Copilot | vigil-ai |
|---|---|---|---|
| Architecture | Clean layered (handler→service→repository→models), 10 modules | FastAPI + RAG + agent router + state machine + RBAC + automation | FastAPI + multi-agent system (LeadHunter, Enrichment, Engagement, Sales, Orchestrator) |
| Implementation completeness | PHASE_1_* files in root reveal incomplete status | Complete MVP with explicit limitations documented in README | Single-day project (2 commits), hackathon-level |
| Source depth | 10 handlers, 10 services, 10 repositories, 11 models | 24 Python modules (agent_router, agent_executor, legal_agent, rag_service, embedding_service, chunker, ai_validator, risk_analysis, analysis_record_service, automation_service, webhook_service, auth, validators, etc.) | 7 models, 7 API routes, agents directory |
| Test evidence | **ZERO test files** | **176 tests passed, 0 failed, 0 skipped** (18.13s) | 29 tests passed, 0 failed (7.10s) |
| Ability to execute tests | **CANNOT COMPILE** — go.mod requires Go 1.26, only Go 1.22.2 available | All tests pass with argon2-cffi installed | All tests pass |
| CI health | NO CI | FAILING — DEPENDENCY_VERSION_FAILURE (pyjwt==2.8.1 yanked) | NO CI |
| Build health | Frontend builds (4.61s); **backend cannot build** | Frontend builds (2.42s); backend tests pass | Frontend builds (1.85s); backend tests pass |
| README honesty | Claims "real-time notifications" (FALSE — no WebSocket/SSE), "scalable/robust" (unverified) | Lists MVP limitations explicitly; claims "166 tests" (actual: 176 — understated) | Honest about being a Pareto case study |
| Business relevance | Project management SaaS (common domain) | Legal contract analysis with AI (unique domain) | B2B event management (niche) |
| Recruiter clarity | Generic project management app | Clear AI + legal domain with RBAC and guardrails | Clear case study context |
| Uniqueness vs Top 5 | Go language breadth (only differentiator) | AI + legal + RBAC + state machine — unique combination | Multi-agent autonomous system — unique |
| AI relevance | NONE | RAG, embeddings, agent router, guardrails, confidence validation — meaningful AI | Agno + Claude multi-agent orchestration — meaningful AI |
| Full-stack breadth | Go backend + Vue 3 frontend | FastAPI backend + React/TypeScript frontend | FastAPI backend + Vue 3 frontend |
| Portfolio credibility | Weakened by zero tests, can't compile, false claims | Strengthened by 176 tests, verified implementation, honest README | Moderate — single-day project looks like hackathon |

#### Decision: Legal-AI-Copilot WINS Slot #6

**Rationale:** QUALITY > LANGUAGE BREADTH. Legal-AI-Copilot has 176 passing tests, verified RBAC/agent-router/state-machine/RAG implementation, meaningful AI beyond API wrapping, and an honest README. Go-API has zero tests, cannot compile with available toolchain, and makes false "real-time notifications" claims. Go's language breadth is not worth sacrificing quality for.

**vigil-ai eliminated:** 29 tests is decent but the project is a single-day hackathon-level effort (2 commits). Not strong enough for Top 6.

---

### 2. Go-API Verification Results

| Field | Value |
|---|---|
| GO_TEST_RESULT | **CANNOT EXECUTE** — go.mod requires go >= 1.26, only Go 1.22.2 available. ZERO test files found (`find . -name "*_test.go"` returns 0 results). |
| GO_FRONTEND_BUILD_RESULT | **SUCCESS** — Vue 3 frontend builds in 4.61s with Vite. All assets generated. |
| GO_IMPLEMENTATION_COMPLETENESS | **INCOMPLETE** — PHASE_1_CLOSURE.md and PHASE_1_SUMMARY.md in root reveal the project is in "Phase 1" state. escopo.txt in root. No demo URL. No CI. |
| GO_README_OVERCLAIMS | 1. "Notificações em tempo real" (Real-time notifications) — **FALSE**: no WebSocket, SSE, or EventSource found in backend code. Notifications are DB-stored models with no push mechanism. 2. "Solução robusta, escalável" — **UNVERIFIED**: no load testing, no scaling architecture, no evidence of robustness beyond standard GORM+Gin stack. |
| GO_FINAL_PORTFOLIO_SCORE | **45/100** (downgraded from 58 due to: zero tests, cannot compile, false real-time claim, incomplete status) |

---

### 3. Legal-AI-Copilot Verification Results

| Field | Value |
|---|---|
| LEGAL_TEST_RESULT | **176 passed, 0 failed, 0 skipped** in 18.13s. README claims "166 tests passed, 0 failed" — actual count is HIGHER (176 > 166). All tests pass after installing argon2-cffi (missing from requirements.txt). |
| LEGAL_FRONTEND_BUILD_RESULT | **SUCCESS** — React + TypeScript + Vite frontend builds in 2.42s. 1512 modules transformed. |
| LEGAL_CI_CLASSIFICATION | **DEPENDENCY_VERSION_FAILURE** — `pyjwt==2.8.1` was yanked/never existed on PyPI (available: 2.8.0, 2.9.0). CI "Install dependencies" step fails. Trivial fix: change to `pyjwt>=2.8.0` or `pyjwt==2.9.0`. NOT a product failure. |
| LEGAL_IMPLEMENTATION_COMPLETENESS | **COMPLETE MVP** — Verified: RBAC (5 roles: ADMIN, LAWYER, ASSISTANT, CLIENT, VIEWER with role checks), agent router (intent classification: SUMMARIZE, EXTRACT, IDENTIFY_RISKS, COMPARE, UNKNOWN), human review state machine (validate_transition with APPROVED as terminal state), automation/webhook (webhook_service.py + automation_service.py with status tracking), risk analysis (severity, category, confidence_score), AI beyond API wrapping (RAG via rag_service.py, embeddings via embedding_service.py, chunking via chunker.py, guardrails via ai_validator.py with confidence validation). |
| LEGAL_README_OVERCLAIMS | **NONE** — README is honest. Lists MVP limitations explicitly. Test count claim (166) is actually understated (actual: 176). Only issue: 40+ report MD files clutter the root directory. |
| LEGAL_FINAL_PORTFOLIO_SCORE | **75/100** (upgraded from 63 due to: 176 verified passing tests, complete implementation, honest README, meaningful AI) |

---

### 4. Final Slot #6 Decision

**WINNER: Legal-AI-Copilot**

**Exact reason:** Legal-AI-Copilot has 176 passing tests (vs Go-API's 0), a verified complete implementation with RBAC/agent-router/state-machine/RAG/guardrails (vs Go-API's false "real-time" claims), a trivial CI fix (vs Go-API's inability to compile), and meaningful AI beyond API wrapping (vs Go-API's no AI). Go's language breadth does not compensate for its quality deficits. QUALITY > LANGUAGE BREADTH.

---

### 5. PayFlow-AI — 629 Test Claim Verification

| Field | Value |
|---|---|
| COLLECTED_TESTS | **629** |
| PASSED | **629** |
| FAILED | **0** |
| SKIPPED | **0** |
| DURATION | **65.37s** |

**VERIFIED: YES** — The README badge claim "629 backend tests" is exactly correct. 629 tests collected, 629 passed, 0 failed, 0 skipped. The claim may remain unchanged.

#### PayFlow-AI CI Classification

| CI Job | Status | Classification |
|---|---|---|
| backend-tests | SUCCESS | All 629 tests pass in CI |
| docker-compose-check | FAILURE | **STALE_CI_CONFIG** — uses `docker-compose` (v1 hyphenated) but GitHub Actions runners only have `docker compose` (v2 plugin). Exit code 127 (command not found). |
| frontend-build | FAILURE | **TOOLCHAIN_VERSION_FAILURE** — CI uses Node.js 18 but Next.js 16 requires Node.js >=20.9.0. Frontend builds successfully locally with Node 24. |
| e2e-tests | SKIPPED | Only runs on workflow_dispatch |

**Summary:** Both CI failures are configuration issues, NOT product failures. The backend (actual product code) passes all 629 tests. Fixes: (1) change `docker-compose` to `docker compose` in CI, (2) change Node.js version from 18 to 20 in CI.

---

### 6. desafio-focon Provenance/Positioning Check

| Check | Result |
|---|---|
| Proprietary company material | **BRAND LOGOS PRESENT** — 3 Fócon Engenharia logo files in `public/brand/` (focon-logo-horizontal.png, focon-logo-white.png, focon-colorida.jpeg). These are publicly visible corporate logos, not proprietary data. |
| Confidential data | **NONE** — No PDFs, DOCX, or XLSX files found. No CNPJ, CPF, phone, or salary data. |
| Real company data | **NONE** — Seed data uses fictional project names ("Residencial Aurora", "Edifício Horizonte") with standard test UUIDs. Migration comments explicitly say "Seed demo data", "demo users", "demo projects". |
| Employment/affiliation claims | **NONE** — No claims of employment, affiliation, or endorsement by Fócon found in README or source. |
| README positioning | Named "FoconFlow" — references Fócon Engenharia brand assets but does not claim to be Fócon's official product. |

**Classification:** TECHNICAL_CHALLENGE_CASE_STUDY

**Top-6 Eligibility:** **RETAIN** — No provenance problem exists. The repository is a technical challenge case study with demo data only. Brand logos are publicly visible corporate logos used in the context of a hiring challenge.

**Required README update:** Add explicit positioning statement clarifying this is a technical challenge/hiring case study, not Fócon's official product, and that Leonardo is not affiliated with Fócon. Example: "> **Contexto:** Projeto desenvolvido como desafio técnico. Não é um produto oficial da Fócon Engenharia e não há vínculo empregatício ou comercial."

---

### 7. Professional Experience Claim

**Classification:** OWNER_VERIFIABLE_CAREER_FACT

The "3+ years of experience" claim in the profile README is a career-experience fact that cannot be verified from Git repositories alone. This is normal — career experience is verified through LinkedIn, resumes, and professional references, not through code commits.

**Decision:** Do NOT remove "3+ years" from the profile README. Mark as PENDING_OWNER_PROFILE_CONFIRMATION. Leonardo should confirm this is accurate based on his actual professional history.

**Do not fabricate experience.** If Leonardo confirms the claim is accurate, it may remain. If it is inaccurate, it should be corrected to the actual figure.

---

### 8. Visibility Plan Reconfirmation

#### 5 PUBLIC_TO_PRIVATE Reconfirmations

| Repository | One-sentence reason for making private |
|---|---|
| API_Analyze | Tutorial-level Streamlit app with no tests, no CI, and no Docker — its presence as a public repo dilutes the portfolio's perceived engineering quality. |
| FragTech-Fintech | Claims "AI-powered" but has no AI implementation visible in code — the unsupported claim creates a credibility risk for reviewers who inspect the source. |
| PyScriptTech | A company marketing website with minimal code value — it does not demonstrate engineering depth and is better represented by the ProFlow case study in the profile README. |
| Portfolio-LeonardoFragoso-React | Duplicates the profile README's portfolio function — maintaining two portfolio surfaces (profile README + portfolio site) creates inconsistency and the React portfolio adds no unique engineering signal. |
| MedFlow_Finance | A PHP/Laravel project outside Leonardo's primary Python stack with 20+ SPRINT report files cluttering the root — it dilutes the Python/backend positioning and does not demonstrate Leonardo's strongest skills. |

#### Portfolio Website Impact Assessment

**Question:** If Portfolio-LeonardoFragoso-React is made private, can its deployed website remain available?

**Answer:** YES. Vercel deployments are independent of repository visibility. Making a GitHub repository private does NOT affect already-deployed Vercel sites. The Vercel project remains connected to the GitHub account and can still access private repos through its GitHub integration. The portfolio site at `https://portfolio-leonardo-fragoso-react.vercel.app/` will remain live (confirmed: HTTP 200).

**Question:** Does the profile README fully replace the portfolio website function?

**Answer:** PARTIALLY. The profile README provides the GitHub-facing portfolio function (name, title, positioning, ProFlow case study, project table, stack, contact links). The portfolio website provides a visual experience (animations, project cards, contact form) that the text-based README cannot replicate. However, for GitHub-first discovery (recruiters browsing GitHub profiles), the profile README is the primary surface. The portfolio website can remain live at its Vercel URL even with the repo private.

**Recommendation:** Making Portfolio-LeonardoFragoso-React private is SAFE. The Vercel deployment remains live. The profile README handles GitHub-facing discovery. If Leonardo wants to fully retire the portfolio site, that requires a separate Vercel project deletion (not part of this plan).

---

### 9. Case Study Strategy

#### ProFlow — HIGH_PRIORITY_PUBLIC_CASE_STUDY

**Proposed case-study outline:**

1. **Business Problem** — Freelancers manage proposals, deliveries, communication, and payments in separate tools, increasing manual work and reducing project visibility.
2. **Solution Overview** — SaaS platform centralizing the commercial and operational freelance workflow with AI assistance for proposals and pricing.
3. **High-Level Architecture** — Vue.js frontend + Django REST Framework backend + PostgreSQL + Redis + Celery + Django Channels (WebSockets).
4. **Backend Architecture** — Django REST Framework with JWT auth (access + refresh with rotation), OAuth (Google, GitHub), Celery async workers, Django Channels for real-time, payment webhooks with idempotency and validation.
5. **Frontend Architecture** — Vue.js 3 with reactive state management, real-time updates via WebSocket subscription.
6. **Data Layer** — PostgreSQL for relational data, Redis for caching and Celery queue.
7. **Integrations** — OpenAI (AI proposals/pricing), Mercado Pago (payments), OAuth providers (Google, GitHub).
8. **Testing Strategy** — pytest backend tests (9 test files covering AI engine, payments, security, state machine, signals, consent mode, hero render, resilient throttles, score history).
9. **Deployment Architecture** — Railway (backend, worker, beat, Postgres, Redis) + Vercel (frontend). Separate deploy pipelines.
10. **Engineering Decisions** — JWT rotation, OAuth, async processing, real-time updates, webhook idempotency, rate limiting, OpenAPI/Swagger documentation.
11. **Safe Screenshots** — UI screenshots with demo/fictional data only.
12. **Lessons Learned** — Production scaling insights, security hardening (Phase 2A), monitoring.

**Do NOT disclose:** Source code, production secrets, real customer data, private operational data, environment variables, deployment URLs with sensitive paths.

#### DevPro — MEDIUM_PRIORITY_PUBLIC_CASE_STUDY

**Proposed case-study outline:**

1. **Problem** — Coordinating autonomous software development cycles across multiple AI agents and tools requires orchestration, state management, and validation.
2. **Solution** — Autonomous Software Development Orchestrator coordinating OpenAI (Tech Lead/reviewer), Devin (executor), GitHub (source of truth), and local OS (Git, tests, build, lint).
3. **Orchestrator Architecture** — Modular, persistent, testable core running autonomous loop: OpenAI → DevPro → Devin → GitHub → Validation → OpenAI review → FIX/APPROVE.
4. **CodingExecutor Abstraction** — Abstraction layer for code execution agents (Devin integration via v3 API, polling for completion).
5. **Multi-Executor Design** — Architecture supports multiple executor backends (Devin, OpenAI-local fallback).
6. **Devin/OpenAI-local Provider Architecture** — OpenAI as structured reviewer (Tech Lead/Code/Architecture/Security/QA) with APPROVED/FIX_REQUIRED/REPLAN_REQUIRED/BLOCKED decisions. Devin as executor via v3 API.
7. **Resilience/Reconciliation** — Crash recovery via persistent state transitions, idempotent prompt sending (deduplication), resume interrupted workflows.
8. **Testing** — 16 test files covering actions, API, autonomous loop, CI validation, Devin client, Devin polling, Git client, GitHub client, idempotency, max iterations, OpenAI client, restart recovery, SHA validation, state machine, validation, workspace.
9. **Guardrails** — No GPT-generated shell, allowlisted semantic actions, path-traversal protection, secret sanitization, destructive actions disabled by default.

**Do NOT disclose:** Source code, API keys, Devin API details beyond public documentation, local project paths, production environment details.

**Do NOT create either case study yet — requires Leonardo's approval.**

---

### 10. Final Top 6 (Evidence-Backed)

| Pin | Repository | Revised Score | Primary Signal |
|---|---|---|---|
| #1 | PayFlow-AI | **84/100** (unchanged — 629 tests verified, CI failures are config-only) | FastAPI + AI + payments + 629 verified tests + Docker + Railway |
| #2 | Pagae | **79/100** (unchanged — CI passing, architecture verified) | Django 5 + 10 domain apps + repository pattern + CI passing |
| #3 | Oraculo | **72/100** (unchanged — deepest AI engineering) | NL2SQL + RAG + knowledge graph — deepest AI engineering |
| #4 | desafio-focon | **69/100** (unchanged — provenance clear, E2E verified) | React 19 + Supabase RLS + E2E tests + live on Vercel |
| #5 | LogiFlow | **63/100** (unchanged — domain complexity verified) | Logistics SaaS + multi-tenant + fiscal + GPS — domain complexity |
| #6 | **Legal-AI-Copilot** | **75/100** (upgraded from 63 — 176 tests verified, implementation verified, honest README) | AI + legal + RBAC + agent router + state machine + RAG + 176 tests |

**Go-API-Gestao-de-Projetos-e-Tarefas REMOVED from Top 6** — Score revised to 45/100 (zero tests, cannot compile, false real-time claim). Moved to KEEP_PUBLIC_SUPPORTING.

---

### 11. Final Action Plan

#### A. FINAL_TOP_6
1. PayFlow-AI (84)
2. Pagae (79)
3. Oraculo (72)
4. desafio-focon (69)
5. LogiFlow (63)
6. Legal-AI-Copilot (75)

#### B. FINAL_PIN_ORDER
1. PayFlow-AI
2. Pagae
3. Legal-AI-Copilot
4. Oraculo
5. desafio-focon
6. LogiFlow

> Pin order adjusted: Legal-AI-Copilot (75) moves to #3 pin position (higher score than Oraculo at 72 and desafio-focon at 69). Pin order follows score ranking.

#### C. PUBLIC_TO_PRIVATE (5)
1. API_Analyze
2. FragTech-Fintech
3. PyScriptTech
4. Portfolio-LeonardoFragoso-React
5. MedFlow_Finance

#### D. ARCHIVE (1)
1. SaaS

#### E. KEEP_PUBLIC_SUPPORTING (4)
1. Plataforma-de-Monitoramento-de-Sistemas-e-APIs (Java 21 + Spring Boot — language breadth)
2. LeonardoRFragoso (profile README infrastructure)
3. Go-API-Gestao-de-Projetos-e-Tarefas (Go — language breadth, but downgraded to supporting due to quality deficits)
4. vigil-ai (multi-agent AI case study — supporting signal)

#### F. PRIVATE_STRATEGIC (2)
1. ProFlow (HIGH_PRIORITY_PUBLIC_CASE_STUDY)
2. DevPro (MEDIUM_PRIORITY_PUBLIC_CASE_STUDY)

#### G. CASE_STUDY_CREATE (2 — do NOT create yet)
1. ProFlow case study (high priority)
2. DevPro case study (medium priority)

#### H. README_REWRITE (3)
1. Oraculo — remove "Palantir competitor" claim, clean root (5 status report files)
2. LogiFlow — remove "60-70%" marketing claim, remove fake CI/CD badges, clean root
3. Go-API-Gestao-de-Projetos-e-Tarefas — remove false "real-time notifications" claim, remove "scalable/robust" claims, clean root (PHASE_1_*, escopo.txt)

#### I. README_MINOR_UPDATE (4)
1. PayFlow-AI — 629 test claim VERIFIED, no change needed to badge; fix CI config (docker-compose→docker compose, Node 18→20)
2. Pagae — add architecture diagram, demo/staging URL
3. desafio-focon — add technical challenge positioning statement, clean root report files
4. Legal-AI-Copilot — clean root (40+ report MD files), fix pyjwt version in requirements.txt, update test count from 166 to 176

#### J. METADATA_UPDATE (6 — all Top 6)
1. PayFlow-AI — add description, topics, homepage
2. Pagae — add description, topics
3. Legal-AI-Copilot — add description, topics
4. Oraculo — add description, topics
5. desafio-focon — add description, topics, homepage
6. LogiFlow — add description, topics, homepage

#### K. PROFILE_README_CHANGES
1. Remove Digital-Signage-Platform from "Outros projetos em destaque" (private, 404)
2. Add PayFlow-AI, Pagae, Legal-AI-Copilot to projects table
3. Replace Go-API with Legal-AI-Copilot in Top 6 references
4. Keep "3+ anos de experiência" (PENDING_OWNER_PROFILE_CONFIRMATION — do not remove)
5. Keep "6 sistemas corporativos" claim (refers to former-employer work — PENDING_OWNER_PROFILE_CONFIRMATION)
6. Keep ProFlow case study section (strongest signal)
7. Add DevPro as brief mention (case study candidate)
8. Ensure all linked repos are PUBLIC

#### Projected Counts

| Metric | Current | Projected |
|---|---|---|
| PUBLIC_AFTER | 15 | 10 (6 showcase + 4 supporting) |
| PRIVATE_AFTER | 15 | 20 (15 current private + 5 made private) |
| ARCHIVED_AFTER | 0 | 1 (SaaS) |
| TOTAL | 30 | 30 |

---

### 12. Security Invariants

| Validator | Result |
|---|---|
| validate_credential_matrix.py | **PASS** — Total items: 41, ALL VALIDATIONS PASSED |
| validate_history_sanitization_plan.py --live | **PASS** — COMPLETED=10, READY=0, BLOCKED=2, PUBLIC=15, PRIVATE=15, TOTAL=30 |

No Phase 2A state regressed.

---

### Phase 2B.1 Safety Confirmations

- No repository history rewritten: YES
- No force push: YES
- Former-employer repositories untouched: YES
- ProFlow production untouched: YES
- No credentials modified: YES
- No sessions modified: YES
- No secret values printed: YES
- No GitHub Support ticket submitted: YES
- No Phase 2B mutations executed: YES — audit and reconciliation only
- No repository visibility changed: YES
- No repositories archived: YES
- No READMEs modified: YES
- No topics/descriptions changed: YES
- No profile README modified: YES
- No case studies created: YES
- No pins modified: YES
- Local test environments created in /tmp and cleaned up: YES

---

## Phase 2B.2 — Portfolio Curation Execution (2026-08-18)

**Date:** 2026-08-18
**Phase:** 2B.2 (Approved Portfolio Curation Execution)
**Status:** EXECUTED — All approved mutations completed
**Owner Approval:** Explicit owner approval received
**Baseline:** Merged main `29e9593d2154fceedacd556d66226601f601059a` (PR #17)

> This section records the execution of the approved Phase 2B portfolio curation plan. All mutations were explicitly authorized by the owner.

### Execution Summary

| Action | Count | Status |
|---|---|---|
| PUBLIC → PRIVATE visibility changes | 5 | EXECUTED |
| Archives | 1 (SaaS) | EXECUTED |
| README PRs (Top 6 + Go-API) | 7 | MERGED |
| Profile README PR | 1 | MERGED |
| Metadata updates (descriptions) | 6 | EXECUTED |
| Topic updates | 6 | EXECUTED |
| Homepage URL updates | 2 (verified demos only) | EXECUTED |
| Pin changes | 0 | MANUAL_ACTION_REQUIRED (GitHub API limitation) |
| Case studies created | 0 | DEFERRED |

### Post-Execution Visibility Totals

| Metric | Before | After |
|---|---|---|
| TOTAL | 30 | 30 |
| PUBLIC | 15 | 10 |
| PRIVATE | 15 | 20 |
| ARCHIVED | 0 | 1 |

### All PR Merge SHAs

| Repository | PR # | Merge SHA |
|---|---|---|
| PayFlow-AI | #2 | `0d9bdf1875c9ddf2a2c3bee8aa530aab6c0fcc75` |
| Pagae | #1 | `f89f6745019d34412b92856254e0e57c41d0f164` |
| Legal-AI-Copilot | #1 | `76bc3631d57cc861da723dd30a499aa9f5a714e5` |
| Oraculo | #1 | `5077e8e66677d605db569553f8ee2b5b2bb4c926` |
| desafio-focon | #33 | `cde0fd86f1ae87b3628111090854334b33695649` |
| LogiFlow | #2 | `128aa2cdaaafee72e88d81a8a8be79b83ca43983` |
| Go-API-Gestao-de-Projetos-e-Tarefas | #1 | `fc008ba8416b14c37ebf608b47ba0de59bf80176` |
| LeonardoRFragoso (profile) | #18 | `5eb4b655d70650b8f587daf986eb1b20a46df729` |

### Validator Results (Post-Execution)

| Validator | Result |
|---|---|
| validate_credential_matrix.py | PASS (41 IDs) |
| validate_history_sanitization_plan.py --live | PASS (Phase 2A: 15/15 historical, Phase 2B: 10/20/1 live) |

### Security Invariants (Post-Execution)

- No repository deleted: YES
- No history rewritten: YES
- No force push: YES
- Former-employer repositories untouched: YES (Digital-Signage-Platform, FlowTrack remain PRIVATE)
- ProFlow production untouched: YES
- No credentials modified: YES
- No sessions modified: YES
- No secret values printed: YES
- No GitHub Support ticket submitted: YES
- No private strategic repos made public: YES (ProFlow, DevPro remain PRIVATE)
- No client/former-employer code exposed: YES
- No production behavior altered: YES
- No case studies created: YES (deferred)
- No pins modified via API: YES (manual action required — GitHub API limitation)
