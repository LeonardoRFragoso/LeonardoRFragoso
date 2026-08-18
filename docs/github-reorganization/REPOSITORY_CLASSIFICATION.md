# Repository Classification — Phase 1 Audit

**Account:** LeonardoRFragoso
**Audit date:** 2026-08-17

This file classifies every repository across three dimensions:
1. **IP / Provenance classification** (who owns the right to publish)
2. **Claims-vs-evidence maturity** (does the code support README claims?)
3. **Portfolio value scoring** (0-5 across 10 dimensions) + recommended destination

---
## 1. IP / Provenance Classification

| Category | Label | Count | Repositories |
|---|---|---|---|
| A | Personal product | 25 | API_Analyze, AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes, Bet-IA-BOT, DevPro, FinanceControl, FragTech-Fintech, Go-API-Gestao-de-Projetos-e-Tarefas, LeonardoRFragoso, LogiFlow, MVP-linkedin-bot, MedFlow_Finance, Oraculo, PRODERJ, Pagae, PayFlow-AI, Portfolio-LeonardoFragoso-React, ProFlow, PyScriptTech, SaaS, alzi-project, aviator-banca, base-corporativa, exnova-api, pimenta, sanduicherie |
| B | Open-source / educational | 3 | Bot_IqOption, Plataforma-de-Monitoramento-de-Sistemas-e-APIs, SGE-Django |
| C | Technical hiring challenge | 5 | -Backend-Pipefy-AWS-no-Mundo-Invest, IronForceAI-Teste, Legal-AI-Copilot, desafio-focon, vigil-ai |
| D | Client project | 5 | AndaimesPini_Project, FlowTrack, Plataforma-Cursos-WRConsultoria, Sistema-de-compras, wrconsultoriaesolucoes |
| E | Former employer / corporate | 4 | Digital-Signage-Platform, YardMaster, dash-monitor, nao-conformidade |
| F | Internal supporting infrastructure | 1 | devpro-e2e-sandbox |

### IP Classification Details

#### API_Analyze
- **Category:** A — Personal product
- **Branding evidence:** Personal financial analysis tool for Brazilian FIIs and stocks (B3); README references LeonardoRFragoso GitHub account; No third-party branding or client references
- **Ownership concerns:** Personal project using public financial APIs (NewsAPI, Alpha Vantage, yFinance). No third-party IP concerns. Safe for public distribution.
- **Recommend private:** False

#### AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes
- **Category:** A — Personal product
- **Branding evidence:** Branded 'AgentesIA' as personal SaaS MVP; README states 'fins educacionais e de portfólio'; Author block links to @LeonardoRFragoso personal GitHub
- **Ownership concerns:** Personal project with no third-party/client branding; uses Anthropic Claude API via user-supplied key. Safe to publish.
- **Recommend private:** False

#### AndaimesPini_Project
- **Category:** D — Client project
- **Branding evidence:** frontend/src/components/pages/LandingPage.js: 'Andaimes Pini' (title and footer '© {year} Andaimes Pini. Todos os direitos reservados.'); frontend/src/components/layouts/Navbar.js: 'Andaimes Pini'; frontend/.env.production: REACT_APP_API_URL=https://andaimespiniproject-production.up.railway.app; DEPLOY_GUIDE.md: 'Guia de Deploy - AndaimesPini Project' (Frontend: Vercel, Backend: Railway); backend/create_admin_railway.py and railway.json + nixpacks.toml + Procfile for Railway deployment
- **Ownership concerns:** Clearly a client project for 'Andaimes Pini' (a scaffolding rental company — 'andaimes' = scaffolding in PT-BR). System is a rental management system deployed live to Railway (andaimespiniproject-production.up.railway.app) and Vercel. Public redistribution of client-specific business code and data is risky.
- **Recommend private:** True

#### -Backend-Pipefy-AWS-no-Mundo-Invest
- **Category:** C — Technical hiring challenge
- **Branding evidence:** README.md title: 'Mundo Invest API'; README.md: 'Teste técnico para vaga de Desenvolvedor Backend (Pipefy & AWS) no Mundo Invest'; Próxima etapa Teste Técnico.txt: recruitment message from 'Henrique R Castiglione, CGO Grupo EWZ Capital' with Notion link to test instructions, deadline 29/05; app/infrastructure/pipefy_client.py: Pipefy GraphQL mutations (createCard, updateCardField) structured per official Pipefy docs
- **Ownership concerns:** Candidate-authored code for a Mundo Invest (Grupo EWZ Capital) technical test. The challenge instructions and company name are embedded, but the implementation is the candidate's own work; typical for hiring challenges to be public as portfolio evidence.
- **Recommend private:** False

#### Bet-IA-BOT
- **Category:** A — Personal product
- **Branding evidence:** Personal betting analysis system using public APIs (API-Football, The Odds API); No third-party branding or client references
- **Ownership concerns:** Personal project with no third-party IP concerns, but contains a hardcoded API key that should be rotated
- **Recommend private:** True

#### Bot_IqOption
- **Category:** B — Open-source / educational
- **Branding evidence:** README explicitly states 'projeto de estudo/experimental para fins educacionais'; Disclaimer: 'Não utilize em contas reais'
- **Ownership concerns:** Despite educational framing, the repo contains production MercadoPago credentials and real user API keys — the payment integration and user management are production-grade, not educational
- **Recommend private:** True

#### DevPro
- **Category:** A — Personal product
- **Branding evidence:** Personal project: 'DevPro — Autonomous Software Development Orchestrator' coordinating OpenAI/Devin/GitHub/local OS; No third-party client/employer branding; integrates public APIs (OpenAI, Devin, GitHub) as a personal tool
- **Ownership concerns:** No third-party IP concerns. Personal autonomous-development orchestrator using public APIs. Safe to publish.
- **Recommend private:** False

#### Digital-Signage-Platform
- **Category:** E — Former employer / corporate
- **Branding evidence:** Initial commit 0d0dba6 titled 'Initial commit - TVS Digital Signage Platform'; package.json name is 'tvs-digital-signage'; docs/PLTI-012a_Documento_de_Escopo_As_is_To_be.md identifies the system as 'TVS iTracker' serving 'iTracker, Rio Brasil Terminal (RBT), CLIA'; docs/PLTI-012b/c/d are corporate governance documents (Arquitetura, As Built, Plano de Manutencao) authored by Leonardo Fragoso dated 05/12/2024; History references database 'tvs_itracker'; LEGAL_COMPLIANCE_REPORT.md (commit f73b8fe) self-describes a 'white label preparation' that 'Removed real credentials containing proprietary information'; proxy-server.py, final_rbac_fix.py, backend/routes/settings.py, backend/migrations/add_system_configs.py still reference tvs/iTracker
- **Ownership concerns:** This is a corporate system built for iTracker / Rio Brasil Terminal / CLIA. Despite a self-authored 'LEGAL_COMPLIANCE_REPORT' claiming it is cleared for white-label commercialization, residual corporate identifiers (PLTI project docs, TVS iTracker naming, tvs_itracker DB references) and real database credentials remain in git history. Public redistribution carries clear employer/client IP risk.
- **Recommend private:** True

#### FinanceControl
- **Category:** A — Personal product
- **Branding evidence:** README.md: 'FinanceControl - Gerenciador Financeiro Pessoal'; MIT License (LICENSE file); README.md: 'Sistema completo de gestão financeira pessoal com modelo Freemium'
- **Ownership concerns:** Personal finance product with MIT license — no third-party IP concerns. However a live EC2 private key is exposed, which is a security (not IP) issue requiring immediate remediation before any public showcase.
- **Recommend private:** False

#### FlowTrack
- **Category:** D — Client project
- **Branding evidence:** README states the system is 'em producao no maior terminal portuario privado do Brasil (operacao ICTSI no Porto do Rio de Janeiro)'; Initial commit 83a021b titled 'Commit inicial - Sistema Atendimento GR completo com tema escuro e visualizacao em tempo real' (GR = corporate operations system); Docs/LEGAL_REVIEW_SUMMARY.md references removal of brand references 'ICTSI, iTracker, CLIA' - confirming corporate/client provenance; Docs/BRANDING.md and Docs/LOGO_SETUP.md describe white-label rebranding workflow
- **Ownership concerns:** This is a production operations-management system deployed at an ICTSI port terminal. Although a 'White Label transformation' (commit 377713b) attempted to strip brand references and an accompanying LEGAL_REVIEW_SUMMARY claims 'Zero Legal Blockers' and 'No data exposure', the README still explicitly names ICTSI and the initial commit exposes the GR corporate system origin. The committed nohup.out log in history contradicts the 'No data exposure' claim. Public redistribution carries client IP and operational-data risk.
- **Recommend private:** True

#### FragTech-Fintech
- **Category:** A — Personal product
- **Branding evidence:** 'FragTech' is Leonardo's own software-house brand (per audit special instruction); README references a FragTech logo (frontend/public/logo.svg); MIT License; Project scaffolded with bolt.new (.bolt/config.json template 'bolt-vite-react-ts')
- **Ownership concerns:** Personal FragTech software-house brand project. Commits are authored by leonardo.fragoso@itracker.com.br (employer email) but the project is branded FragTech (personal brand), not iTracker employer IP. Safe to publish.
- **Recommend private:** False

#### Go-API-Gestao-de-Projetos-e-Tarefas
- **Category:** A — Personal product
- **Branding evidence:** Branded 'TaskFlow' as personal SaaS; escopo.txt explicitly frames it as a portfolio piece: 'O que ESSE projeto prova no seu portfólio' and 'passa em entrevista fácil'; MIT License, author block links to personal GitHub/LinkedIn
- **Ownership concerns:** Personal showcase project with no client/employer branding. Safe to publish.
- **Recommend private:** False

#### IronForceAI-Teste
- **Category:** C — Technical hiring challenge
- **Branding evidence:** README title: 'IronFence AI - Spike de Descoberta CEAP'; README references 'curriculo_nome_completo.pdf # Currículo do candidato'; CHECKLIST.md references 'decisão do candidato'; Project name 'IronForceAI-Teste' suggests a test/evaluation submission
- **Ownership concerns:** Hiring challenge submission using public CEAP (Cota para Exercício da Atividade Parlamentar) data from Câmara dos Deputados. The code is the candidate's own work but was created for a selection process. Public visibility is likely intentional for evaluation.
- **Recommend private:** False

#### Legal-AI-Copilot
- **Category:** C — Technical hiring challenge
- **Branding evidence:** Committed PDF 'Case Técnico – AI & Legal Operations Specialist.pdf' opens with 'Parabéns por avançar para esta etapa do processo seletivo' (congratulations for advancing to this stage of the selection process); INTERVIEW_QUICK_REFERENCE.md, VIDEO_PRESENTATION_SCRIPT.md, DEMO_SCRIPT*.md, RECORDING_CHECKLIST.md — all hiring-deliverable artifacts; Case requires PDF document (max 5 pages) + demo video (5-10 min) as delivery format; deliverables/ directory with Legal_AI_Copilot_Case.pdf
- **Ownership concerns:** The hiring case PDF and deliverables are from a prospective employer's selection process. Committing these publicly redistributes third-party hiring materials. The committed venv and contract PDFs add noise but the case materials are the IP concern.
- **Recommend private:** True

#### LeonardoRFragoso
- **Category:** A — Personal product
- **Branding evidence:** README.md: 'Leonardo Fragoso — Backend Software Engineer | Python · Django · FastAPI | SaaS · Applied AI'; README.md homepage: https://leonardo-r-fragoso.vercel.app (and portfolio-leonardo-fragoso-react.vercel.app); GitHub profile README repo (special repo matching username, rendered on profile)
- **Ownership concerns:** Personal profile README — fully owned, no third-party IP. Safe to publish (it is the public profile by design).
- **Recommend private:** False

#### LogiFlow
- **Category:** A — Personal product
- **Branding evidence:** LogiFlow CRM branding throughout — README, docs, docker configs, helm charts; MIT license (Copyright 2026 Leonardo Fragoso); Live deployment referenced: logi-flow-wuhp.vercel.app; Email: vendas@logiflow.com.br, noreply@logiflow.com.br; References multiple third-party integrations: Focus NFe, Evolution API, Mercado Pago, Google Maps, Sascar, Autotrac, OnixSat, SuiteCRM, Omie, Bling, Tiny, Melhor Envio, Frenet, SendGrid
- **Ownership concerns:** Personal SaaS product with MIT license. Third-party API integrations are documented but no proprietary third-party code is included. The extensive documentation (70+ docs files) contains integration guides with example credentials that should be sanitized. Safe for public distribution after credential cleanup.
- **Recommend private:** True

#### MVP-linkedin-bot
- **Category:** A — Personal product
- **Branding evidence:** Personal CV/CPF/resume PDFs in repo root; LinkedIn job application data with real company names and phone numbers
- **Ownership concerns:** Contains Leonardo Fragoso's personal identification documents (CPF, CVs) and Chrome browser session data — extremely risky if made public
- **Recommend private:** True

#### MedFlow_Finance
- **Category:** A — Personal product
- **Branding evidence:** Branded 'MedFlow Finance' as a personal SaaS B2B product; MIT License (Copyright 2026 Leonardo Fragoso); composer.json license field is 'proprietary' but root LICENSE is MIT; No client/employer branding; admin@medflow.local demo credentials
- **Ownership concerns:** Personal medical-billing SaaS product with no client data or employer branding. Safe to publish, though the '100% ready' claim is misleading (see contradiction).
- **Recommend private:** False

#### Oraculo
- **Category:** A — Personal product
- **Branding evidence:** Personal product: 'Oráculo — Plataforma Universal de Inteligência Corporativa' (enterprise data intelligence platform); No third-party client/employer branding; uses public APIs (OpenAI, Z.AI, OpenCode) and open-source libs (FAISS, DuckDB, NetworkX)
- **Ownership concerns:** No third-party IP concerns. Personal product. dados/chat_history contains sample conversation data (not real customer data).
- **Recommend private:** False

#### PRODERJ
- **Category:** A — Personal product
- **Branding evidence:** README: 'Este projeto foi desenvolvido como ferramenta de estudo pessoal para concursos públicos'; README: 'NÃO possui vínculo oficial com o PRODERJ, Dataprev, as bancas IBDO/FGV ou qualquer órgão público'; README: 'As questões são elaboradas e não são reproduções de provas anteriores'; License: 'Projeto de uso pessoal - Não destinado à distribuição comercial'; deploy-vm.sh targets a personal VM (192.168.0.45, user lfragoso)
- **Ownership concerns:** Investigated for employer/government IP per special instruction. Despite the PRODERJ name (Rio de Janeiro state IT center public exam), the README explicitly disclaims any official affiliation, questions are AI-generated originals (not reproductions of real exams), and deploy targets a personal VM. No government/employer proprietary code, datasets, or internal systems found. The name refers to a public exam, not proprietary code. Classified A (Personal product), NOT E (former employer/corporate).
- **Recommend private:** False

#### Pagae
- **Category:** A — Personal product
- **Branding evidence:** Branded 'Pagaê' as an original Brazilian fintech prototype; README: 'Marcas, textos e fluxos são originais e não copiam concorrentes'; README: 'Este projeto é um protótipo/MVP de software financeiro brasileiro. Não é uma instituição financeira.'; No client/employer branding; personal GitHub author
- **Ownership concerns:** Personal original-brand fintech prototype with no third-party IP. Safe to publish.
- **Recommend private:** False

#### PayFlow-AI
- **Category:** A — Personal product
- **Branding evidence:** Personal SaaS product: 'PayFlow AI — Assistente Financeiro Conversacional via WhatsApp' for autônomos/MEIs; No third-party client/employer branding; integrates Twilio, OpenAI, Mercado Pago, Asaas as a personal product
- **Ownership concerns:** No third-party IP concerns. Personal product. Main risk is the exposed Twilio credential in Docs/CORRIGIR_TOKEN.txt.
- **Recommend private:** False

#### Plataforma-Cursos-WRConsultoria
- **Category:** D — Client project
- **Branding evidence:** README: 'Plataforma web de gestao e comercializacao de cursos (LMS + backoffice administrativo) para a WR Consultoria e Solucoes em QSMS'; Seed data and tests reference WR/wrcursos.com.br branding (api/app/seeds/courses_seed.py, classes_seed.py, students_seed.py; tests/conftest.py); web/src/views/ValidateCertificate.vue and alembic migrations reference WR/wrcursos domain; MULTI_TENANT_ARCHITECTURE.md and PROJECT_SUMMARY.md describe a white-label SaaS for WR Consultoria
- **Ownership concerns:** Built for WR Consultoria e Solucoes em QSMS as a white-label multi-tenant LMS/SaaS. While no third-party commercial plugins are present (unlike the WordPress repo), the domain logic, course catalog seeds, and branding are client-specific. Public redistribution is moderately risky because it exposes a client's business model and seed data, though the code itself is largely original.
- **Recommend private:** True

#### Plataforma-de-Monitoramento-de-Sistemas-e-APIs
- **Category:** B — Open-source / educational
- **Branding evidence:** README.md: 'Desenvolvido como projeto de portfólio profissional'; MIT License (LICENSE file); README.md: 'inspirada em ferramentas corporativas como New Relic, Datadog e Dynatrace' (inspiration, not proprietary code)
- **Ownership concerns:** Personal portfolio project under MIT license with no third-party proprietary code. Safe to publish; only hygiene issue is versioned node_modules.
- **Recommend private:** False

#### Portfolio-LeonardoFragoso-React
- **Category:** A — Personal product
- **Branding evidence:** Personal portfolio of Leonardo Fragoso — 'Desenvolvedor Python Backend | Django · FastAPI · IA'; Deployed at portfolio-leonardo-fragoso-react.vercel.app and leonardofragosodev.netlify.app; readme-github.md references former employer iTracker (ICTSI — Porto do Rio de Janeiro) with 6 enterprise systems; Case studies for ProFlow, LogiFlow, Oráculo in docs/; Featured projects: ProFlow, Base Corporativa, LogiFlow CRM
- **Ownership concerns:** Personal portfolio — safe for public distribution. However, sensitive PDFs (CNPJ card, contrato social) in public/ expose personal/business tax documents. The readme-github.md references former employer iTracker/ICTSI systems by name (GPTracker, GateLog, FlowTrack, Digital Signage, RPA Bots, Sistema GR) — this is work history on a GitHub profile README, not proprietary code.
- **Recommend private:** False

#### ProFlow
- **Category:** A — Personal product
- **Branding evidence:** Personal product: 'ProFlow — The Operating System for Professional Freelancers' (Brazilian freelancer platform); Proprietary license (LICENSE file). No third-party client/employer branding; integrates Mercado Pago, OpenAI, Asaas, Telegram
- **Ownership concerns:** No third-party IP concerns. Personal product. Critical concern is real production credentials leaked in git history (RAILWAY_ENV_FINAL.txt, DEPLOY_CHECKLIST.md).
- **Recommend private:** True

#### PyScriptTech
- **Category:** A — Personal product
- **Branding evidence:** PyScript.tech branding pervasive across 30+ source files (components, services, contexts, pages); Social links: github.com/pyscripttech, instagram.com/pyscripttech, linkedin.com/company/pyscripttech; Contact: contato@pyscript.tech, phone (21) 98029-2791; localStorage keys use @pyscript:* prefix (theme, user, token); SEO component hardcodes 'PyScript.tech' in title and meta descriptions; Footer: '© PyScript.tech. Todos os direitos reservados.'; 50+ docs files reference PyScript/PyScript.tech in filenames and content; ProFlow integration: PyScript.tech described as owner/operator of ProFlow portal; Testimonials mention 'PyScript.tech entregou em 3 semanas...'; Timeline: 'Fundação da PyScript.tech com foco em soluções Python e automação'
- **Ownership concerns:** Personal software house website. MIT licensed. No third-party IP concerns. Branding is deeply embedded and would require comprehensive rebranding effort. Safe for public distribution under current brand.
- **Recommend private:** False

#### SGE-Django
- **Category:** B — Open-source / educational
- **Branding evidence:** README.md: 'Sistema de Gestão de Estoque (SGE)' — SGE = Estoque (Stock), NOT Escolar (School); README.md: 'projeto desenvolvido em Django e Bootstrap 5'; Generic Django app structure (authentication, brands, categories, inflows, outflows, products, suppliers) — standard inventory management tutorial pattern
- **Ownership concerns:** Generic Django stock-management learning project with no third-party branding. Safe to publish; only a low-risk dev SECRET_KEY.
- **Recommend private:** False

#### SaaS
- **Category:** A — Personal product
- **Branding evidence:** README.md: 'Ecossistema SaaS - Plataformas de Serviços com IA'; MIT License (LICENSE file); README.md: 'BI-as-a-Service Ativo v1.1.0'
- **Ownership concerns:** Personal SaaS ecosystem project under MIT license. No third-party IP. Private repo; safe to keep or selectively publish.
- **Recommend private:** True

#### Sistema-de-compras
- **Category:** D — Client project
- **Branding evidence:** README.md: 'Sistema de Gestão de Compras - Ziran v2.0' - Ziran is a specific company brand; assets/img/logo_ziran.jpg and ziran fundo.jpg - company branding; Fluxo utilizado hoje pela empresa.docx - internal company process documentation; Compras_SLA .xlsx - corporate purchasing SLA data; README describes corporate purchasing workflow with 7-step approval process
- **Ownership concerns:** Client/company-specific purchasing system for 'Ziran'. Contains internal business process documents, corporate SLA data, and company branding. Public redistribution exposes client internal processes and data.
- **Recommend private:** True

#### YardMaster
- **Category:** E — Former employer / corporate
- **Branding evidence:** WHITE_LABEL_TRANSFORMATION.md documents renaming itracker_logo.png to logo.png and CSS variables --itracker-* to --brand-*; LEGAL_REVIEW_REPORT.md confirms original project had ICTSI/iTracker/CLIA references; utils/sharepoint_client.py: SharePoint URL replaced with generic placeholder (was corporate); Operational data files: armadores_brasil.txt (shipping companies), posicao_floriano.txt, posicao_suzano.txt (yard positions for specific Brazilian ports); Database schema has 'unidade TEXT DEFAULT Rio de Janeiro' hardcoded
- **Ownership concerns:** Originally an iTracker/ICTSI corporate yard management system. While branding was superficially rebranded to 'white label', the codebase contains operational data (yard positions, shipping company lists), a tracked SQLite database, and hardcoded defaults referencing specific corporate locations. Public redistribution is risky.
- **Recommend private:** True

#### alzi-project
- **Category:** A — Personal product
- **Branding evidence:** README.md: 'Alzi Project — Processador de Planilha de Contêineres'; README.md: 'Ferramenta desenvolvida para automatizar o processamento de planilhas de rastreamento de contêineres portuários'
- **Ownership concerns:** Utility tool with no obvious third-party branding, but the committed TC.xls/TC.xlsx spreadsheets may contain real port operational/container tracking data from an actual operation or client. Repo is private, mitigating exposure.
- **Recommend private:** True

#### aviator-banca
- **Category:** A — Personal product
- **Branding evidence:** Personal bankroll tracking app for Aviator game; No third-party branding or client references
- **Ownership concerns:** Personal project with no third-party IP concerns. No secrets or sensitive data committed.
- **Recommend private:** True

#### base-corporativa
- **Category:** A — Personal product
- **Branding evidence:** README.md: 'Base Corporativa' brand with live demo at basecorporativa.store; E-commerce for corporate uniforms/workwear - appears to be own business venture; Railway deployment configuration (nixpacks.toml, railway.toml, Procfile); MercadoPago and MelhorEnvio integrations for Brazilian e-commerce
- **Ownership concerns:** Appears to be a personal e-commerce business. No third-party employer branding detected. However, tracked production credentials (AWS, MercadoPago, SendGrid, database) pose a severe security risk if the repo is public. The business data and customer info in the database URL are sensitive.
- **Recommend private:** True

#### dash-monitor
- **Category:** E — Former employer / corporate
- **Branding evidence:** README.md: 'utilizado internamente na iTracker (ICTSI, Porto do Rio de Janeiro)'; V1-Dash/dashboard_monitor.py: hardcoded iTracker logo references, 'itracker_logo.png', 'Desenvolvido pelo setor de Qualidade - iTracker'; V2-Dash/frontend/src/App.tsx: brandLogo itracker_logo.png, brandName 'iTracker'; V2-Dash/backend/app/domain/services_config.py: service id 'ictsi-tvs', name 'ICTSI TVs'; Internal IP 192.168.0.45 with corporate service ports
- **Ownership concerns:** Clearly an internal iTracker/ICTSI corporate tool. Public redistribution exposes internal infrastructure details, IP addresses, and dashboard screenshots of proprietary systems.
- **Recommend private:** True

#### desafio-focon
- **Category:** C — Technical hiring challenge
- **Branding evidence:** Repo named 'desafio-focon' (desafio = challenge); .gitignore references 'Desafio_Tecnico_*.pdf' (technical challenge PDF); Fócon Engenharia brand assets committed in /public/brand (logo-horizontal.png, logo-white.png, focon-colorida.jpeg); AGENTS.md references 'Production project ref: ldjkblrsicecyeithkgo (desafio-focon, São Paulo)'; VALIDATION_REPORT_2026-08-16.md titled 'DESAFIO-FOCÓN: COMPREHENSIVE VALIDATION REPORT'; No contract/proposal/payment/commercial engagement evidence found anywhere
- **Ownership concerns:** Fócon Engenharia is a real company whose brand assets are committed. This appears to be a technical hiring challenge (desafio técnico) based on or for Fócon. No evidence it became a commercial client engagement. Brand usage is low-risk in a challenge context but third-party logo redistribution should be noted.
- **Recommend private:** False

#### devpro-e2e-sandbox
- **Category:** F — Internal supporting infrastructure
- **Branding evidence:** README.md: 'A minimal Python project (calculator) used for DevPro end-to-end orchestration testing'; devpro.yml: DevPro project config with executor (primary: devin, fallback: openai_local), reviewer (openai/gpt-4o-mini), and policies (create_repository: false, create_pull_request: true, merge: false, deploy: false); Open PRs authored by 'devin-ai-integration[bot]' and 'LeonardoRFragoso' via DevPro orchestration branches (devpro/<sha>-<task>)
- **Ownership concerns:** Internal supporting infrastructure for the DevPro orchestrator's E2E test pipeline. No third-party IP. Private repo; should remain private as it is test scaffolding, not a portfolio piece.
- **Recommend private:** True

#### exnova-api
- **Category:** A — Personal product
- **Branding evidence:** Personal trading bot for Exnova platform; No third-party branding or client references
- **Ownership concerns:** Personal project with no third-party IP concerns. Uses environment variables for all credentials — no secrets committed.
- **Recommend private:** True

#### nao-conformidade
- **Category:** E — Former employer / corporate
- **Branding evidence:** README.md: system based on corporate quality form 'planilha ITK-RG-PR-QUA-03-A-13'; create_admin_user.py: hardcoded iTracker emails (leonardo.fragoso@itracker.com.br, glaucio.xavier@itracker.com.br); diagnose_auth_system.py: same iTracker emails; templates/accounts/: multiple templates with 'iTracker' in page titles and itracker_logo.png references; static/img/itracker_logo.png tracked in git
- **Ownership concerns:** Corporate quality management system for iTracker. Contains iTracker branding, employee emails, and references to corporate quality process documents (ITK-RG-PR-QUA-03-A-13). Public redistribution exposes internal corporate processes and personnel.
- **Recommend private:** True

#### pimenta
- **Category:** A — Personal product
- **Branding evidence:** Melt Pimenta brand — landing page for an adult-content visual/conceptual project; README: 'Projeto visual/conceitual. Conteúdo destinado a maiores de 18 anos.'; No company or client branding — appears to be a personal/brand project; Uses Unsplash CDN images (no local media assets)
- **Ownership concerns:** Personal/brand landing page with no third-party IP concerns. Content is adult-oriented but not illegal. No proprietary code or client data. Safe for public distribution from an IP standpoint, though the committed node_modules and lack of .gitignore are hygiene issues.
- **Recommend private:** True

#### sanduicherie
- **Category:** A — Personal product
- **Branding evidence:** README.md: 'Sanduicherie' brand - platform for product management and digital catalog; Appears to be a personal/client project for a sandwich shop or food business; No employer or corporate branding detected
- **Ownership concerns:** Appears to be a personal project or small client engagement. No third-party employer IP concerns. Safe for public showcase as a portfolio piece.
- **Recommend private:** False

#### vigil-ai
- **Category:** C — Technical hiring challenge
- **Branding evidence:** README.md: 'Processo Seletivo AI Engineer — Pareto'; README.md: 'Solução completa para o case: agente autônomo de gestão do funil de um evento B2B de IA'; Commit msg: 'Finalize Vigil.AI Summit AI agent case' and 'Prepare final delivery package for Pareto AI Engineer case'
- **Ownership concerns:** Candidate-authored solution for a Pareto AI Engineer hiring case. The 'Vigil.AI Summit' event is a fictional case scenario, not a real client. Safe to publish as portfolio evidence of multi-agent AI work.
- **Recommend private:** False

#### wrconsultoriaesolucoes
- **Category:** D — Client project
- **Branding evidence:** Repository is the full production WordPress site for 'WR Consultoria e Solucoes em QSMS'; Custom mu-plugin 'wr-site-improvements' (delivery/upload-to-public_html/wp-content/mu-plugins/wrsi) with WR-branded blog cover images; Committed business PDFs: WR_ordem_servico_site.pdf (service order), WR_kit_implementacao.pdf, WR_guia_ga4_pixel.pdf, WR_analise_site.pdf; audit/conversion-2026-08/evidence/pdf/ contains WR-branded audit artifacts; Commercial premium plugins committed: elementor-pro, wordpress-seo-premium (licensed paid plugins not redistributable); public_html/wp-content/uploads/complianz/snapshots/WR-Consultoria-e-Solucoes-br-proof-of-consent-*.pdf (client consent records)
- **Ownership concerns:** Public redistribution is unsafe on multiple fronts: (1) commercial premium WordPress plugins (Elementor Pro, Yoast SEO Premium) are licensed paid software that must not be publicly redistributed; (2) WR Consultoria business documents (service orders, implementation kits, GA4/pixel guides) and production consent records are client/company proprietary; (3) the full production WordPress deployment (core + uploads) exposes the live site's structure and content.
- **Recommend private:** True

---
## 2. Claims-vs-Evidence Maturity Classification

| Repository | Maturity | Key README Claims | Evidence Summary |
|---|---|---|---|
| API_Analyze | ADVANCED_MVP | Modular application with Streamlit, yFinance for B3 FII/stock analysis; Technical indicators: SMA, EMA, dividend history, financial reports (DRE, Balance Sheet, Cash Flow); NewsAPI integration for fin | tests=False, CI=False, docker=False, migrations=True, deploy=False, mock/fake=False, seed/demo=False, activity=stale 6-12mo |
| AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes | ADVANCED_MVP | Plataforma SaaS completa de análise estratégica de negócios; Multi-tenant com isolamento por organização; 5 agentes especializados trabalhando em conjunto | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=stale 6-12mo |
| AndaimesPini_Project | MVP | Sistema de Gestão de Locações; interface responsiva e moderna | tests=False, CI=False, docker=False, migrations=False, deploy=True, mock/fake=False, seed/demo=True, activity=stale 6-12mo |
| -Backend-Pipefy-AWS-no-Mundo-Invest | ADVANCED_MVP | API de Gerenciamento de Clientes e Integração com Pipefy; arquitetura em camadas (Clean Architecture simplificada); Visão de Produção (AWS) | tests=True, CI=False, docker=False, migrations=False, deploy=False, mock/fake=True, seed/demo=False, activity=active last 90d |
| Bet-IA-BOT | ADVANCED_MVP | Sistema automatizado de identificação de apostas de valor (value bets); Sistema completo que coleta dados de múltiplas APIs; Treina modelos de ML para prever resultados | tests=True, CI=False, docker=True, migrations=True, deploy=False, mock/fake=False, seed/demo=True, activity=stale 6-12mo |
| Bot_IqOption | ADVANCED_MVP | Projeto de estudo/experimental para fins educacionais; Conexão autenticada com a API da IQ Option; Suporte a conta PRACTICE (demo) e REAL | tests=False, CI=False, docker=True, migrations=True, deploy=True, mock/fake=False, seed/demo=True, activity=active last 90d |
| DevPro | ADVANCED_MVP | Autonomous Software Development Orchestrator; Phase 1 — the foundation: modular, persistent, testable core; Roadmap item unchecked: '[ ] Production autonomy' | tests=True, CI=True, docker=True, migrations=True, deploy=False, mock/fake=True, seed/demo=False, activity=active last 90d |
| Digital-Signage-Platform | PRODUCTION_LIKE | Plataforma completa de sinalizacao digital e TV corporativa para gestao centralizada de conteudo multimidia; Multi-empresa: Suporte a multiplas empresas e localizacoes em uma unica instalacao; Compila | tests=True, CI=False, docker=False, migrations=True, deploy=True, mock/fake=False, seed/demo=True, activity=stale 6-12mo |
| FinanceControl | ADVANCED_MVP | Sistema completo de gestão financeira pessoal com modelo Freemium, aplicativo multiplataforma e integração de pagamentos; Sistema de monetização Freemium com integração Mercado Pago; IA Assistente - I | tests=True, CI=False, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=False, activity=stale 6-12mo |
| FlowTrack | PRODUCTION_LIKE | Plataforma de gestao de operacoes com workflow de aprovacao multinivel, RBAC avancado e auditoria completa - em producao no maior terminal portuario privado do Brasil (operacao ICTSI no Porto do Rio d | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=False, activity=stale 6-12mo |
| FragTech-Fintech | PROTOTYPE | Modern AI-powered financial platform; Digital banking services, personal financial management, and personalized investment recommendations; Democratize access to advanced financial services | tests=False, CI=False, docker=False, migrations=True, deploy=False, mock/fake=True, seed/demo=False, activity=stale 6-12mo |
| Go-API-Gestao-de-Projetos-e-Tarefas | ADVANCED_MVP | Plataforma SaaS moderna para gestão de projetos, squads e tarefas; Perfeita para equipes que buscam uma solução robusta, escalável e fácil de usar; Pronto para produção | tests=False, CI=False, docker=True, migrations=True, deploy=False, mock/fake=False, seed/demo=False, activity=active last 90d |
| IronForceAI-Teste | PROTOTYPE | Análise investigativa da CEAP da Câmara dos Deputados; Mapeamento de relações parlamentar-fornecedor para hipóteses de compliance; Pipeline AUTOMATIZADO com agentes IA | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=True, activity=active last 90d |
| Legal-AI-Copilot | MVP | Legal AI Copilot — MVP; Sistema de IA para análise de contratos jurídicos com revisão humana, guardrails, e métricas de produtividade | tests=True, CI=True, docker=True, migrations=True, deploy=False, mock/fake=True, seed/demo=True, activity=active last 90d |
| LeonardoRFragoso | PRODUCTION_LIKE | 3+ anos de experiência; 6 sistemas corporativos; Produtos próprios em produção | tests=False, CI=True, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=False, activity=active last 90d |
| LogiFlow | PRODUCTION_LIKE | SaaS enterprise para transportadoras: CRM + TMS + fiscal + GPS — 60-70% mais acessível que concorrentes; Multi-tenant support with data isolation; CRM, TMS, Fiscal (CT-e/MDF-e via Focus NFe), ERP inte | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| MVP-linkedin-bot | MVP | Bot de automação completa do processo de candidatura a vagas no LinkedIn; Dashboard de acompanhamento em tempo real; Sistema de logs estruturado | tests=False, CI=False, docker=False, migrations=False, deploy=True, mock/fake=False, seed/demo=True, activity=active last 90d |
| MedFlow_Finance | ADVANCED_MVP | SaaS B2B de Automação e Faturamento Médico; PROJETO 100% PRONTO PARA EXECUÇÃO E DEMONSTRAÇÃO COMERCIAL; Status: MVP Ready | tests=True, CI=False, docker=True, migrations=True, deploy=False, mock/fake=True, seed/demo=True, activity=active last 90d |
| Oraculo | ADVANCED_MVP | plataforma enterprise de inteligência sobre dados; Posicionamento: concorrente de Palantir / Databricks / Snowflake. Não é um chatbot.; v4.0.0 — Hardening & Production-Ready | tests=True, CI=False, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| PRODERJ | ADVANCED_MVP | Sistema de simulados para preparação de Concursos Públicos; Multi-concurso com seleção visual; Geração assistida de questões difíceis com IA (Z.ai GLM-4.5-flash free tier) | tests=True, CI=False, docker=False, migrations=False, deploy=True, mock/fake=False, seed/demo=True, activity=active last 90d |
| Pagae | RELEASE_CANDIDATE | SaaS brasileiro de checkout Pix parcelado para pequenos e médios lojistas; Provider-agnostic payments (PaymentProvider interface, sandbox + Celcoin example); CI/CD: GitHub Actions (lint, testes, migra | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=False, activity=active last 90d |
| PayFlow-AI | ADVANCED_MVP | SaaS financeiro conversacional para gestão de cobranças via WhatsApp; Tests badge: 629 backend + 36 E2E (actual: 42 backend test files, 3 frontend); Multi-tenant com RBAC (owner/admin/finance/viewer) | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| Plataforma-Cursos-WRConsultoria | PRODUCTION_LIKE | Plataforma web de gestao e comercializacao de cursos (LMS + backoffice administrativo) para a WR Consultoria e Solucoes em QSMS; Fases do white-label SaaS concluidas: Fundacao multi-tenant (Tenant, te | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | ADVANCED_MVP | solução profissional de monitoramento de sistemas e APIs; Clean Architecture com separação rigorosa de responsabilidades; Backend Java moderno com Java 21 e Spring Boot 3.2 | tests=True, CI=False, docker=True, migrations=True, deploy=False, mock/fake=False, seed/demo=False, activity=stale 6-12mo |
| Portfolio-LeonardoFragoso-React | ADVANCED_MVP | React 18.3, TypeScript 5.5, TailwindCSS 3.4, Vite 5.4, Framer Motion 11; Deployed on Vercel and Netlify with CI/CD; Featured projects: ProFlow, Base Corporativa, LogiFlow CRM and more | tests=False, CI=False, docker=False, migrations=False, deploy=True, mock/fake=False, seed/demo=False, activity=active last 90d |
| ProFlow | ADVANCED_MVP | plataforma inteligente completa criada para proteger, organizar e profissionalizar freelancers no Brasil; ecossistema definitivo de trabalho freelance; Fase 3 - Escala (Em Progresso) | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| PyScriptTech | PRODUCTION_LIKE | Website institucional e portfólio da PyScript.tech — empresa especializada em desenvolvimento de software sob medida; Services: Software Sob Medida, Aplicações Web, Automação & Bots; React 18, CSS Mod | tests=True, CI=False, docker=False, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| SGE-Django | ARCHIVED_HISTORICAL | (none) | tests=False, CI=False, docker=False, migrations=True, deploy=False, mock/fake=False, seed/demo=False, activity=stale >12mo |
| SaaS | MVP | Ecossistema modular de aplicações SaaS com inteligência artificial integrada; BI-as-a-Service Ativo v1.1.0; Criação Automática de Dashboards com IA (GPT-4o-mini) | tests=True, CI=False, docker=False, migrations=True, deploy=False, mock/fake=False, seed/demo=False, activity=stale 6-12mo |
| Sistema-de-compras | MVP | Sistema completo de Gestão de Compras - Ziran v2.0; Vue.js 3.4 + FastAPI 0.109 + PostgreSQL 15 + Docker; Workflow Completo: Fluxo de aprovação em 7 etapas | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=True, activity=stale 6-12mo |
| YardMaster | ADVANCED_MVP | 100% White Label - Totalmente personalizável para qualquer cliente; Multi-tenant - Suporte a múltiplas empresas/operações; Sistema completo de gestão de pátios e estacionamentos | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=True, activity=stale 6-12mo |
| alzi-project | PROTOTYPE | Ferramenta de conversão e análise de planilhas de contêineres (.xls → .xlsx) com cálculo automatizado de tempos operacionais; Classificação por limites configuráveis (45 min / 1h) | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=False, activity=active last 90d |
| aviator-banca | MVP | Sistema web completo para acompanhamento de evolução de banca no jogo Aviator; Meta de atingir R$ 4.000,00 em lucro em 30 dias; Dashboard completo com métricas, gráficos e histórico detalhado | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=False, activity=stale 6-12mo |
| base-corporativa | PRODUCTION_LIKE | E-commerce completo de roupas corporativas com checkout integrado, PWA e sistema de gestão avançado; PWA (Progressive Web App) - Experiência mobile nativa com instalação; Checkout Seguro - Integração  | tests=True, CI=False, docker=False, migrations=True, deploy=True, mock/fake=False, seed/demo=True, activity=active last 90d |
| dash-monitor | PROTOTYPE | Status: Em Produção; utilizado internamente na iTracker (ICTSI, Porto do Rio de Janeiro); Dashboard de monitoramento de aplicações em tempo real | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=True, activity=active last 90d |
| desafio-focon | PRODUCTION_LIKE | MVP Completo (complete MVP); Production: https://desafio-focon.vercel.app; CI/CD: GitHub Actions com Supabase CLI v2 | tests=True, CI=True, docker=False, migrations=True, deploy=True, mock/fake=False, seed/demo=True, activity=active last 90d |
| devpro-e2e-sandbox | EXPERIMENT | minimal Python project (calculator) used for DevPro end-to-end orchestration testing | tests=True, CI=True, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=False, activity=active last 90d |
| exnova-api | MVP | Bot de trading automatizado para Exnova com estratégia MHI; Suporte a Martingale; Análise de médias móveis | tests=True, CI=False, docker=True, migrations=False, deploy=True, mock/fake=False, seed/demo=True, activity=active last 90d |
| nao-conformidade | ADVANCED_MVP | Sistema web desenvolvido em Django para gerenciar ocorrências e não-conformidades; Workflow automatizado com prazos e notificações; Dashboard completo com métricas e gráficos | tests=True, CI=False, docker=False, migrations=True, deploy=False, mock/fake=False, seed/demo=True, activity=active last 90d |
| pimenta | PROTOTYPE | Landing page visual e conceitual da Melt Pimenta; React 18 + Vite 5 + Tailwind CSS 3 + Framer Motion 11; Age Gate with sessionStorage persistence | tests=False, CI=False, docker=False, migrations=False, deploy=False, mock/fake=False, seed/demo=False, activity=active last 90d |
| sanduicherie | PRODUCTION_LIKE | Plataforma de gestão de produtos, site público e catálogo digital da Sanduicherie; Stack: Vue 3, TypeScript, Vite, Pinia, FastAPI, SQLAlchemy 2, Alembic, PostgreSQL, Docker, GitHub Actions | tests=True, CI=True, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=True, activity=active last 90d |
| vigil-ai | RELEASE_CANDIDATE | sistema multi-agente autônomo que automatiza o funil completo; LeadHunter, Enrichment, Engagement, Sales, Orchestrator agents; cada agente roda assincronamente e deixa log auditável | tests=True, CI=False, docker=True, migrations=True, deploy=True, mock/fake=True, seed/demo=False, activity=active last 90d |
| wrconsultoriaesolucoes | PRODUCTION_VERIFIED | No traditional README; repository is a WordPress site deployment tracked in git with extensive markdown audit/hardening reports (FINAL_HARDENING_REPORT_v2.3.1, HARDENING_COMPLETION_SUMMARY, INTEGRATIO | tests=True, CI=False, docker=False, migrations=True, deploy=True, mock/fake=False, seed/demo=False, activity=active last 90d |

### Maturity Distribution

- **ADVANCED_MVP:** 17
- **PRODUCTION_LIKE:** 9
- **MVP:** 7
- **PROTOTYPE:** 5
- **RELEASE_CANDIDATE:** 2
- **EXPERIMENT:** 1
- **PRODUCTION_VERIFIED:** 1
- **ARCHIVED_HISTORICAL:** 1

### Maturity Justifications

#### API_Analyze — ADVANCED_MVP
V2 is a Django REST + Vue.js rewrite with 6 Django apps, JWT auth, caching config, and 12 improvement phases implemented. However, there are zero tests, no CI, no Docker, and only a single commit with no iteration. The original Streamlit app (V1) is not present in the tree.

#### AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes — ADVANCED_MVP
Has migrations, Docker, deploy config and a claimed live demo, but CI is failing, test coverage is near-zero (1 pytest function + a manual script), and the repo has been stale ~6 months. Core SaaS flows (multi-agent orchestration, billing, async queue) are implemented but not verified by green CI or a real test suite.

#### AndaimesPini_Project — MVP
A deployed, working client rental-management system (live on Railway/Vercel) with manual DB migration scripts and seed data, but no automated tests, no CI, and no Docker. Functional MVP for a real client.

#### -Backend-Pipefy-AWS-no-Mundo-Invest — ADVANCED_MVP
Clean Architecture with 24 passing tests and idempotent webhook handling, but the Pipefy integration is simulated locally (mock) rather than live, and there is no CI, Docker, or deploy config. Fits a well-executed hiring challenge MVP.

#### Bet-IA-BOT — ADVANCED_MVP
Well-structured Django + Vue.js full-stack system with 7 Django apps, ML model training pipeline, Celery async tasks, Docker setup, and API integration tests. However, no CI, no deploy config, tests are integration-only (not unit tests), and project is stale since March 2026.

#### Bot_IqOption — ADVANCED_MVP
Full-stack trading platform with Django backend (accounts, trading, billing modules), React frontend, MercadoPago payment integration, Celery async tasks, and Docker deployment. However, no tests, no CI, and critical production secrets committed to git undermine production readiness.

#### DevPro — ADVANCED_MVP
Core autonomous loop (OpenAI→DevPro→Devin→GitHub→validation→review) is implemented with persistent state machine, 27 tests, CI green, Docker and Alembic migrations. However deployment providers are stubs, README marks 'Production autonomy' as unchecked, and it is still labelled Phase 1–3 foundation work.

#### Digital-Signage-Platform — PRODUCTION_LIKE
Has migrations, deploy configs (nginx/systemd), Prometheus monitoring, RBAC, and multi-company support indicating production-grade engineering, but lacks CI, has only 2 test files, and committed real credentials suggest ad-hoc ops rather than verified production governance.

#### FinanceControl — ADVANCED_MVP
Full-stack product with 29 tests, 11 migrated Django apps, Docker, systemd/nginx deploy config, and a Freemium monetization layer — but no CI and a CRITICAL leaked EC2 private key in the current tree, indicating production-hygiene gaps.

#### FlowTrack — PRODUCTION_LIKE
README asserts a live production deployment at an ICTSI port terminal with real operational impact, which is strong production evidence; however the repository itself has no tests, CI, Docker, or migration framework, so the codebase maturity is production-like at best and the production claim is unverifiable from the repo alone.

#### FragTech-Fintech — PROTOTYPE
A bolt.new-scaffolded fintech UI with only 3 commits, no tests, no CI, no Docker, and no real backend integrations. The README's 'modern AI-powered financial platform' framing overstates what is essentially an AI-generated prototype scaffold.

#### Go-API-Gestao-de-Projetos-e-Tarefas — ADVANCED_MVP
Feature-complete layered Go backend (handler→service→repository) with Vue 3 SPA, GORM migrations, Docker and a detailed README, but zero automated tests and no CI. The README's 'Pronto para produção' claim is contradicted by the roadmap listing tests as future Phase 2 work.

#### IronForceAI-Teste — PROTOTYPE
Exploratory data analysis spike for a hiring challenge — has a functional pipeline (download, process, analyze, visualize) with AI agents, but no tests, no CI, no deployment, and is explicitly a 'spike de descoberta' (discovery spike) rather than a production system.

#### Legal-AI-Copilot — MVP
Hiring-challenge MVP with core flows (PDF upload, text extraction, agent router, risk analysis, JWT auth, RBAC) and 16 tests, but CI is failing, a full venv is committed (11836 files), heuristic mode is a fake-AI fallback, and it was built for a 2-business-day selection process. Not production-ready.

#### LeonardoRFragoso — PRODUCTION_LIKE
This is the live GitHub profile README — always-on public-facing content with an active generation workflow, not a software product. It is currently being modified as part of this audit to become the future central professional README.

#### LogiFlow — PRODUCTION_LIKE
Has tests (16 files), CI/CD (4 workflows with service containers), Docker (6 compose files), Alembic migrations (9 versions), Helm charts, ADRs, clean architecture (DDD), multi-tenant support, and multiple frontend apps. Live deployment referenced (logi-flow-wuhp.vercel.app, Railway API). However, CI passing status unknown, and 53 gitleaks findings (mostly placeholder credentials in docs) need remediation.

#### MVP-linkedin-bot — MVP
Two functional versions of a LinkedIn auto-apply bot with Selenium, Streamlit dashboard, and Telegram integration, but no tests, no CI, and massive unmanaged artifacts (venv, Chrome profiles, PDFs) committed to git.

#### MedFlow_Finance — ADVANCED_MVP
Feature-rich Laravel 11 + Vue 3 SaaS with 17 migrations, 5 async jobs, multi-tenancy and 60 written test methods, but no CI, no phpunit.xml, no Dockerfile, and the tests have never been run. The README's '100% ready' claim is contradicted by its own next-steps section and by the internal audit report self-rating of 85% completeness.

#### Oraculo — ADVANCED_MVP
README claims 'v4.0.0 — Production-Ready' and 'enterprise' positioning vs Palantir/Databricks, but there is NO CI, only 8 test files, only 2 migrations, mock email fallback, TF-IDF fallback RAG, and committed sample/legacy data. The architecture is broad (NL2SQL, RAG, knowledge graph, semantic engine) but production-readiness is overstated.

#### PRODERJ — ADVANCED_MVP
Working SPA live on Vercel with multi-contest support, AI-assisted question generation (serverless, token-protected), and a 122-check validation suite over the question bank. Lacks formal unit tests, CI, and Docker, but is a functional personal study tool with a live deployment.

#### Pagae — RELEASE_CANDIDATE
CI green, 104 tests including an e2e MVP-flow test, Django migrations, Docker (dev+prod), Railway deploy config and staging docs. Missing only real Pix gateway credentials, CPF/CNPJ encryption-at-rest, and a live production deployment to be production-verified. The README honestly scopes itself as 'MVP (atual)' with a clear roadmap.

#### PayFlow-AI — ADVANCED_MVP
Feature-rich (multi-tenant, SaaS billing, 16 migrations, Docker, OpenAI/Twilio/Asaas integrations) but CI is failing, the default payment provider is fake, QR codes are simulated, and the test badge overstates actual coverage. Core happy path works in demo mode but production readiness is not verified.

#### Plataforma-Cursos-WRConsultoria — PRODUCTION_LIKE
Has tests (32), CI, Docker (dev+prod compose), Alembic migrations with row-level security, multi-tenant architecture, and Mercado Pago integration - looking production-grade. However PROJECT_STATUS still lists unimplemented items (student portal, production FRONTEND_URL) and there is no evidence of a live deployment, so it is production-like rather than production-verified.

#### Plataforma-de-Monitoramento-de-Sistemas-e-APIs — ADVANCED_MVP
Clean Architecture Java 21 project with 14 tests, 6 Flyway migrations, WebSocket, Docker, and a React frontend implementing the core APM features — but no CI and versioned node_modules indicate unfinished hygiene. The README roadmap is stale (unchecked items are actually implemented).

#### Portfolio-LeonardoFragoso-React — ADVANCED_MVP
Live portfolio deployed on Vercel/Netlify with TypeScript, i18n, Framer Motion animations, SEO optimization, and prerendering. However, no tests, no CI, and no Docker. The docs/ folder shows evidence of multiple audit and optimization phases. The portfolio is functional and deployed but lacks engineering rigor (tests, CI).

#### ProFlow — ADVANCED_MVP
Extensive feature set (123 migrations, escrow, contracts, AI engine, Telegram, Mercado Pago) with 30 tests and Docker, but CI is failing, the platform relies on a seed/engagement system with simulated payments and fake projects to appear active, and critical production secrets were leaked in git history. Not production-verified.

#### PyScriptTech — PRODUCTION_LIKE
Live website (pyscript.tech) with Supabase backend, CRM dashboard, authentication, ProFlow integration via Edge Functions, 13 SEO landing pages, ROI calculator, and blog page. However, only 2 test files, no CI, and no Docker. The CRM uses localStorage as a mock data layer rather than a real backend for some features.

#### SGE-Django — ARCHIVED_HISTORICAL
Single commit from May 2024 on a legacy 'master' branch with no tests, no CI, and no recent activity — a finished/abandoned learning project that has been superseded.

#### SaaS — MVP
One of six planned SaaS products implemented with Django + React, migrations, and 4 test files, but no CI/Docker and the ecosystem is overwhelmingly scope-doc-only. README claims an active ecosystem while only 1/6 products exist.

#### Sistema-de-compras — MVP
Core functionality works as a Streamlit app for purchasing request management with SLA tracking. However, the README massively overstates the tech stack (claims Vue.js/FastAPI/PostgreSQL/Docker but actual code is Streamlit/SQLite). No tests, no CI, no Docker, and business data files are committed to git.

#### YardMaster — ADVANCED_MVP
Substantial Flask application with multiple blueprints (auth, admin, operacoes, vistoria, posicoes), container management, PDF generation, and role-based access. However, no real test suite, no CI, no Docker, and the repository is severely bloated with 8328 venv files and 3158 .pyc files tracked. The multi-tenant claim is unsubstantiated by code.

#### alzi-project — PROTOTYPE
A focused Streamlit data-processing utility with no tests, no CI, and no containerization. Functional for its narrow purpose but lacks engineering rigor beyond the script itself.

#### aviator-banca — MVP
Simple full-stack CRUD app (FastAPI + React) for personal bankroll tracking. No tests, no CI, no Docker, no deploy config. Core happy path works (add/view daily results, charts) but it's a basic personal tool.

#### base-corporativa — PRODUCTION_LIKE
Has Railway deployment configuration, multiple Django app migrations, live demo URL (basecorporativa.store), and production integrations (MercadoPago, MelhorEnvio, SendGrid, Cloudflare R2). However, test files are empty stubs, no CI pipeline, and CRITICAL production secrets are committed to git. The application appears to be live but lacks engineering maturity in secret management and testing.

#### dash-monitor — PROTOTYPE
V1 is a single-file Streamlit dashboard; V2 is a partial React+FastAPI rewrite with no tests, no CI, and no Docker. No deployment configuration beyond local run instructions. Screenshots suggest it was used internally but the codebase itself is not production-hardened.

#### desafio-focon — PRODUCTION_LIKE
Live Vercel deployment with real Supabase backend, CI green across 4 jobs, 47 test files, 33 migrations and RLS tests. However it is a hiring-challenge MVP (desafio técnico), not a sustained production system with real users, so PRODUCTION_LIKE rather than PRODUCTION_VERIFIED.

#### devpro-e2e-sandbox — EXPERIMENT
Intentionally minimal test fixture (calculator) whose purpose is to be operated on by the DevPro orchestrator — not a product. Its value is as E2E infrastructure, not standalone software.

#### exnova-api — MVP
Functional trading bot with custom Exnova API integration, MHI strategy, Telegram control, and Railway deployment. However, only 1 test file, no CI, no migrations, and the codebase is a single-purpose bot without broader architecture.

#### nao-conformidade — ADVANCED_MVP
Django application with multiple quality management tools (brainstorming, Ishikawa, 5 Whys, GUT matrix, 5W2H), workflow automation, and dashboard. Has 1 test file and migrations but no CI or Docker. Active development with 3 open PRs and 26 branches (mostly codex auto-generated).

#### pimenta — PROTOTYPE
Simple landing page with 9 basic React components, no tests, no CI, no Docker, no .gitignore, and node_modules committed to git. Only a single commit with no iteration. The app is demoable but incomplete from an engineering perspective.

#### sanduicherie — PRODUCTION_LIKE
Well-architected full-stack application with Vue 3 + FastAPI, comprehensive test suite (unit + integration + E2E), CI pipeline with PostgreSQL service, Docker Compose, Alembic migrations, repository pattern, and proper environment variable management. Lacks only verified live deployment evidence to reach PRODUCTION_VERIFIED.

#### vigil-ai — RELEASE_CANDIDATE
A polished hiring-case solution with 29 tests, Alembic migrations, Docker Compose, a mock-mode fallback for AI agents, and a Render deploy config — feature-complete and demoable, lacking only CI to be production-like.

#### wrconsultoriaesolucoes — PRODUCTION_VERIFIED
This is the live production WordPress site for WR Consultoria (Hostinger-managed), with 70 regression tests, delivery/rollback tooling, hardening reports, and active commits in the last 90 days. Deployment is verified by the presence of production uploads, consent records, and Hostinger managed-plugin docs.

---
## 3. Portfolio Value Scoring (0-5)

### Scoring Dimensions

| Dimension | Description |
|---|---|
| TECHNICAL_DEPTH | Complexity, architecture quality, engineering rigor |
| BUSINESS_RELEVANCE | Market demand, business value, commercial applicability |
| PRODUCTION_EVIDENCE | Tests, CI, migrations, Docker, deploy configs, live deployment |
| DIFFERENTIATION | Uniqueness vs. common portfolio projects |
| DOCUMENTATION | README quality, inline docs, ADRs, architecture docs |
| TEST_QUALITY | Test coverage, test types (unit/integration/E2E), test design |
| CURRENT_RELEVANCE | Recent activity, modern stack, maintained status |
| RECRUITING_VALUE | How well it demonstrates hireable skills |
| SOFTWARE_HOUSE_VALUE | Value as a software-house case/portfolio piece |
| IP_PUBLICATION_SAFETY | Safety of public publication (5=safe, 0=definitely unsafe) |

### Score Summary Table

| Repository | TECH | BUSI | PROD | DIFF | DOCU | TEST | CURR | RECR | SOFT | IP P | Avg | Destination |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| API_Analyze | 3 | 2 | 1 | 2 | 3 | 0 | 2 | 2 | 1 | 4 | 2.00 | KEEP_PUBLIC_SECONDARY |
| AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes | 4 | 4 | 2 | 3 | 4 | 1 | 2 | 4 | 3 | 4 | 3.10 | SHOWCASE_PUBLIC |
| AndaimesPini_Project | 3 | 3 | 3 | 1 | 3 | 0 | 2 | 2 | 3 | 1 | 2.10 | MAKE_PRIVATE_PENDING_REVIEW |
| -Backend-Pipefy-AWS-no-Mundo-Invest | 4 | 2 | 1 | 2 | 4 | 3 | 2 | 4 | 1 | 3 | 2.60 | SHOWCASE_PUBLIC |
| Bet-IA-BOT | 4 | 3 | 2 | 3 | 3 | 1 | 2 | 3 | 2 | 3 | 2.60 | KEEP_PRIVATE_ACTIVE |
| Bot_IqOption | 4 | 3 | 3 | 2 | 3 | 0 | 4 | 3 | 2 | 0 | 2.40 | MAKE_PRIVATE_PENDING_REVIEW |
| DevPro | 5 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 2 | 5 | 4.00 | SHOWCASE_PUBLIC |
| Digital-Signage-Platform | 4 | 4 | 3 | 3 | 4 | 1 | 3 | 3 | 3 | 0 | 2.80 | MAKE_PRIVATE_PENDING_REVIEW |
| FinanceControl | 4 | 3 | 3 | 2 | 4 | 3 | 2 | 3 | 2 | 4 | 3.00 | SHOWCASE_PUBLIC |
| FlowTrack | 3 | 4 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 1 | 2.60 | MAKE_PRIVATE_PENDING_REVIEW |
| FragTech-Fintech | 2 | 3 | 0 | 2 | 2 | 0 | 1 | 1 | 2 | 4 | 1.70 | REBRAND_REBUILD |
| Go-API-Gestao-de-Projetos-e-Tarefas | 4 | 3 | 2 | 2 | 4 | 0 | 4 | 4 | 2 | 5 | 3.00 | SHOWCASE_PUBLIC |
| IronForceAI-Teste | 3 | 2 | 1 | 3 | 3 | 0 | 3 | 3 | 1 | 4 | 2.30 | ARCHIVE_PUBLIC |
| Legal-AI-Copilot | 3 | 3 | 1 | 2 | 3 | 2 | 4 | 3 | 1 | 2 | 2.40 | MAKE_PRIVATE_PENDING_REVIEW |
| LeonardoRFragoso | 1 | 5 | 4 | 2 | 4 | 0 | 5 | 5 | 1 | 5 | 3.20 | SHOWCASE_PUBLIC |
| LogiFlow | 5 | 5 | 4 | 4 | 5 | 3 | 4 | 5 | 5 | 3 | 4.30 | SHOWCASE_PRIVATE_WITH_PUBLIC_CASE |
| MVP-linkedin-bot | 3 | 2 | 2 | 2 | 3 | 0 | 4 | 2 | 1 | 1 | 2.00 | MAKE_PRIVATE_PENDING_REVIEW |
| MedFlow_Finance | 4 | 4 | 1 | 3 | 4 | 1 | 4 | 3 | 4 | 4 | 3.20 | SHOWCASE_PRIVATE_WITH_PUBLIC_CASE |
| Oraculo | 4 | 4 | 2 | 4 | 4 | 2 | 5 | 4 | 3 | 4 | 3.60 | SHOWCASE_PUBLIC |
| PRODERJ | 3 | 2 | 3 | 3 | 4 | 2 | 3 | 2 | 1 | 4 | 2.70 | SHOWCASE_PUBLIC |
| Pagae | 5 | 4 | 3 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 4.30 | SHOWCASE_PUBLIC |
| PayFlow-AI | 4 | 4 | 2 | 3 | 4 | 3 | 5 | 4 | 3 | 3 | 3.50 | SHOWCASE_PUBLIC |
| Plataforma-Cursos-WRConsultoria | 4 | 4 | 3 | 3 | 4 | 3 | 4 | 4 | 4 | 2 | 3.50 | KEEP_PRIVATE_ACTIVE |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | 5 | 3 | 2 | 4 | 4 | 3 | 2 | 4 | 2 | 5 | 3.40 | SHOWCASE_PUBLIC |
| Portfolio-LeonardoFragoso-React | 3 | 4 | 3 | 2 | 4 | 0 | 4 | 5 | 3 | 3 | 3.10 | SHOWCASE_PUBLIC |
| ProFlow | 4 | 4 | 2 | 3 | 3 | 3 | 5 | 4 | 3 | 1 | 3.20 | MAKE_PRIVATE_PENDING_REVIEW |
| PyScriptTech | 4 | 5 | 4 | 3 | 4 | 1 | 5 | 4 | 5 | 4 | 3.90 | REBRAND_REBUILD |
| SGE-Django | 2 | 1 | 0 | 1 | 2 | 0 | 1 | 1 | 1 | 5 | 1.40 | ARCHIVE_PUBLIC |
| SaaS | 4 | 3 | 1 | 3 | 3 | 2 | 2 | 3 | 3 | 4 | 2.80 | KEEP_PRIVATE_ACTIVE |
| Sistema-de-compras | 2 | 3 | 2 | 1 | 2 | 0 | 2 | 1 | 2 | 2 | 1.70 | MAKE_PRIVATE_PENDING_REVIEW |
| YardMaster | 3 | 3 | 2 | 2 | 4 | 0 | 2 | 2 | 2 | 1 | 2.10 | MAKE_PRIVATE_PENDING_REVIEW |
| alzi-project | 2 | 2 | 1 | 1 | 3 | 0 | 2 | 1 | 1 | 3 | 1.60 | KEEP_PRIVATE_ACTIVE |
| aviator-banca | 3 | 1 | 1 | 1 | 2 | 0 | 2 | 1 | 1 | 5 | 1.70 | ARCHIVE_PRIVATE |
| base-corporativa | 4 | 4 | 4 | 3 | 3 | 1 | 4 | 3 | 4 | 3 | 3.30 | KEEP_PRIVATE_ACTIVE |
| dash-monitor | 2 | 2 | 2 | 1 | 3 | 0 | 3 | 1 | 1 | 1 | 1.60 | MAKE_PRIVATE_PENDING_REVIEW |
| desafio-focon | 5 | 3 | 4 | 3 | 4 | 4 | 5 | 5 | 2 | 3 | 3.80 | SHOWCASE_PUBLIC |
| devpro-e2e-sandbox | 2 | 1 | 1 | 1 | 3 | 2 | 3 | 1 | 1 | 5 | 2.00 | SUPPORTING_INFRA_PRIVATE |
| exnova-api | 3 | 2 | 2 | 1 | 2 | 1 | 4 | 2 | 1 | 4 | 2.20 | KEEP_PRIVATE_ACTIVE |
| nao-conformidade | 3 | 3 | 2 | 2 | 3 | 1 | 3 | 2 | 2 | 1 | 2.20 | MAKE_PRIVATE_PENDING_REVIEW |
| pimenta | 1 | 1 | 1 | 1 | 2 | 0 | 2 | 0 | 1 | 3 | 1.20 | MAKE_PRIVATE_PENDING_REVIEW |
| sanduicherie | 5 | 3 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 4 | 3.90 | SHOWCASE_PUBLIC |
| vigil-ai | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 4 | 2 | 4 | 3.20 | SHOWCASE_PUBLIC |
| wrconsultoriaesolucoes | 3 | 5 | 5 | 2 | 4 | 3 | 5 | 2 | 4 | 0 | 3.30 | MAKE_PRIVATE_PENDING_REVIEW |

### Detailed Scores & Recommendations

#### API_Analyze

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 2 |
| Production Evidence | 1 |
| Differentiation | 2 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 2 |
| Software House Value | 1 |
| Ip Publication Safety | 4 |
| **Overall Average** | **2.00** |

- **Recommended destination:** `KEEP_PUBLIC_SECONDARY`
- **Rationale:** Personal financial analysis tool with no tests, CI, or Docker. Safe to keep public as a secondary project. Not showcase-worthy due to lack of testing and CI. The committed db.sqlite3 and potentially real API keys in .env.example should be remediated.

#### AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 2 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 1 |
| Current Relevance | 2 |
| Recruiting Value | 4 |
| Software House Value | 3 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.10** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Strong personal SaaS showcase (multi-agent AI, multi-tenant, async pipeline, billing) with good docs and deploy config. Keep public as a portfolio piece, but fix the failing CI and remove the versioned .env.development before highlighting it.

#### AndaimesPini_Project

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 3 |
| Production Evidence | 3 |
| Differentiation | 1 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 2 |
| Software House Value | 3 |
| Ip Publication Safety | 1 |
| **Overall Average** | **2.10** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Client (Andaimes Pini) proprietary code and database currently public — should be made private pending review and client consent. May be repurposed as a private case study with client approval.

#### -Backend-Pipefy-AWS-no-Mundo-Invest

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 2 |
| Production Evidence | 1 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 2 |
| Recruiting Value | 4 |
| Software House Value | 1 |
| Ip Publication Safety | 3 |
| **Overall Average** | **2.60** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Strong hiring-challenge artifact demonstrating Clean Architecture, testing, and GraphQL mutation design — valuable as public portfolio evidence. The Mundo Invest branding is contextual to a completed selection process and poses low redistribution risk.

#### Bet-IA-BOT

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 3 |
| Documentation | 3 |
| Test Quality | 1 |
| Current Relevance | 2 |
| Recruiting Value | 3 |
| Software House Value | 2 |
| Ip Publication Safety | 3 |
| **Overall Average** | **2.60** |

- **Recommended destination:** `KEEP_PRIVATE_ACTIVE`
- **Rationale:** Well-architected personal project with a hardcoded API key to remediate. Keep private while the API key is rotated and the test file is cleaned. Could be a strong portfolio piece if sanitized and made public.

#### Bot_IqOption

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 3 |
| Production Evidence | 3 |
| Differentiation | 2 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 4 |
| Recruiting Value | 3 |
| Software House Value | 2 |
| Ip Publication Safety | 0 |
| **Overall Average** | **2.40** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Contains production MercadoPago credentials, 197 JWT trading session tokens, user API key files, and SQLite database in git history. Extremely unsafe to publish. Must undergo aggressive secret remediation and history rewriting before any public visibility.

#### DevPro

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 5 |
| Business Relevance | 3 |
| Production Evidence | 3 |
| Differentiation | 4 |
| Documentation | 4 |
| Test Quality | 4 |
| Current Relevance | 5 |
| Recruiting Value | 5 |
| Software House Value | 2 |
| Ip Publication Safety | 5 |
| **Overall Average** | **4.00** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Technically deep personal product (autonomous dev orchestration) with tests, CI, Docker and migrations — strong portfolio showcase. No IP concerns. Currently private; recommend making public as a flagship showcase.

#### Digital-Signage-Platform

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 3 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 1 |
| Current Relevance | 3 |
| Recruiting Value | 3 |
| Software House Value | 3 |
| Ip Publication Safety | 0 |
| **Overall Average** | **2.80** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Corporate (former employer/client) IP with real database credentials still recoverable in git history and residual TVS iTracker / RBT / CLIA branding in PLTI governance docs. Must be made private immediately pending credential rotation and history scrubbing before any showcase consideration.

#### FinanceControl

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 3 |
| Production Evidence | 3 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 2 |
| Recruiting Value | 3 |
| Software House Value | 2 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.00** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Strong personal product demonstrating full-stack + monetization skills, suitable for public showcase. CRITICAL prerequisite: revoke/rotate the EC2 key in chave-EC2/Finance2.pem, purge it from git history, and remove db.sqlite3 + the receipt PDF before any promotion.

#### FlowTrack

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 4 |
| Production Evidence | 3 |
| Differentiation | 3 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 3 |
| Recruiting Value | 3 |
| Software House Value | 3 |
| Ip Publication Safety | 1 |
| **Overall Average** | **2.60** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** A client (ICTSI port terminal) production operations system with corporate branding still referenced in the README and a committed runtime log (nohup.out) leaking session tokens in git history. Should be made private pending removal of the ICTSI reference from the README and history scrubbing of nohup.out, with a sanitized case study as the only public-facing artifact if the client consents.

#### FragTech-Fintech

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 2 |
| Business Relevance | 3 |
| Production Evidence | 0 |
| Differentiation | 2 |
| Documentation | 2 |
| Test Quality | 0 |
| Current Relevance | 1 |
| Recruiting Value | 1 |
| Software House Value | 2 |
| Ip Publication Safety | 4 |
| **Overall Average** | **1.70** |

- **Recommended destination:** `REBRAND_REBUILD`
- **Rationale:** 'FragTech' is Leonardo's own software-house brand and deserves a real showcase, but the current repo is only a bolt.new prototype (3 commits, no tests/CI/Docker). Rebuild it into a genuine FragTech product before presenting it as a software-house credential, or archive it privately.

#### Go-API-Gestao-de-Projetos-e-Tarefas

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 0 |
| Current Relevance | 4 |
| Recruiting Value | 4 |
| Software House Value | 2 |
| Ip Publication Safety | 5 |
| **Overall Average** | **3.00** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Assessed as a backend engineering showcase piece per audit instruction: clean layered Go/Gin architecture, JWT+RBAC, GORM, Vue 3 frontend, Docker. Strong recruiting value. Keep public, but add tests and CI to back the 'production-ready' claim.

#### IronForceAI-Teste

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 2 |
| Production Evidence | 1 |
| Differentiation | 3 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 3 |
| Recruiting Value | 3 |
| Software House Value | 1 |
| Ip Publication Safety | 4 |
| **Overall Average** | **2.30** |

- **Recommended destination:** `ARCHIVE_PUBLIC`
- **Rationale:** Hiring challenge submission that is already public and uses only public government data (CEAP). No secrets or third-party IP concerns. Archive as a completed challenge submission — serves as a portfolio piece showing data analysis and AI agent orchestration skills.

#### Legal-AI-Copilot

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 3 |
| Production Evidence | 1 |
| Differentiation | 2 |
| Documentation | 3 |
| Test Quality | 2 |
| Current Relevance | 4 |
| Recruiting Value | 3 |
| Software House Value | 1 |
| Ip Publication Safety | 2 |
| **Overall Average** | **2.40** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Contains third-party hiring-case materials (Case Técnico PDF from a selection process) that should not be publicly redistributed, plus a committed venv (11836 files) and uploaded test PDFs. Make private, remove venv/uploads/case PDF from tree and history, then decide whether to keep as a private archived hiring artifact.

#### LeonardoRFragoso

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 1 |
| Business Relevance | 5 |
| Production Evidence | 4 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 0 |
| Current Relevance | 5 |
| Recruiting Value | 5 |
| Software House Value | 1 |
| Ip Publication Safety | 5 |
| **Overall Average** | **3.20** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** The central profile README repo — must remain public (it IS the GitHub profile). It will become the future central professional README per this audit's goals.

#### LogiFlow

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 5 |
| Business Relevance | 5 |
| Production Evidence | 4 |
| Differentiation | 4 |
| Documentation | 5 |
| Test Quality | 3 |
| Current Relevance | 4 |
| Recruiting Value | 5 |
| Software House Value | 5 |
| Ip Publication Safety | 3 |
| **Overall Average** | **4.30** |

- **Recommended destination:** `SHOWCASE_PRIVATE_WITH_PUBLIC_CASE`
- **Rationale:** Strong SaaS product with enterprise features (multi-tenant, clean architecture, CI/CD, Docker, Helm, tests, ADRs). Make the repo private to protect the 53 gitleaks findings and production infrastructure URLs, then create a public case study showcasing the architecture and features. The SECURITY_FIX_CREDENTIALS.md shows prior credential exposure incidents — the repo should be private until all credentials in docs are sanitized.

#### MVP-linkedin-bot

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 2 |
| Production Evidence | 2 |
| Differentiation | 2 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 4 |
| Recruiting Value | 2 |
| Software House Value | 1 |
| Ip Publication Safety | 1 |
| **Overall Average** | **2.00** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Contains personal identification documents (CPF, CVs), Chrome session tokens, and PII data in git history. Must remain private and undergo secret remediation (purge Chrome profiles, PDFs, logs, venv from history) before any public consideration.

#### MedFlow_Finance

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 1 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 1 |
| Current Relevance | 4 |
| Recruiting Value | 3 |
| Software House Value | 4 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.20** |

- **Recommended destination:** `SHOWCASE_PRIVATE_WITH_PUBLIC_CASE`
- **Rationale:** Strong software-house-style SaaS (medical billing, multi-tenant, async pipeline) with good architecture and docs, but the '100% ready' claim is contradicted by unvalidated tests, no CI, and its own next-steps. Keep private until tests are actually run and CI is green; then publish a public case study rather than the unverified 'production-ready' repo.

#### Oraculo

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 2 |
| Differentiation | 4 |
| Documentation | 4 |
| Test Quality | 2 |
| Current Relevance | 5 |
| Recruiting Value | 4 |
| Software House Value | 3 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.60** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Ambitious personal data-intelligence platform with broad architecture (NL2SQL, RAG, knowledge graph). Keep public as a showcase but tone down 'production-ready/enterprise' README claims — no CI and sparse tests contradict them. Consider adding CI and removing legacy/sample data.

#### PRODERJ

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 2 |
| Production Evidence | 3 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 2 |
| Current Relevance | 3 |
| Recruiting Value | 2 |
| Software House Value | 1 |
| Ip Publication Safety | 4 |
| **Overall Average** | **2.70** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Personal study tool with a live demo, original AI-generated content, and explicit disclaimers of government affiliation. Safe to keep public as a showcase of full-stack React/TS + serverless work, though the government-exam name in the title may cause confusion.

#### Pagae

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 5 |
| Business Relevance | 4 |
| Production Evidence | 3 |
| Differentiation | 4 |
| Documentation | 5 |
| Test Quality | 4 |
| Current Relevance | 4 |
| Recruiting Value | 5 |
| Software House Value | 4 |
| Ip Publication Safety | 5 |
| **Overall Average** | **4.30** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** The strongest showcase piece of the set: green CI, 104 tests incl. e2e, clean domain-driven Django architecture, provider-agnostic payments, Docker, deploy config and 16 docs. Original brand with explicit no-IP-copy disclaimer. Keep public as the primary portfolio anchor.

#### PayFlow-AI

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 2 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 5 |
| Recruiting Value | 4 |
| Software House Value | 3 |
| Ip Publication Safety | 3 |
| **Overall Average** | **3.50** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Strong personal SaaS product demonstrating multi-tenant architecture, payments integration and conversational AI. Keep public as a showcase but remediate the Twilio token in Docs/CORRIGIR_TOKEN.txt (HIGH) and fix failing CI before highlighting.

#### Plataforma-Cursos-WRConsultoria

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 3 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 4 |
| Recruiting Value | 4 |
| Software House Value | 4 |
| Ip Publication Safety | 2 |
| **Overall Average** | **3.50** |

- **Recommended destination:** `KEEP_PRIVATE_ACTIVE`
- **Rationale:** An active, well-engineered client (WR Consultoria) LMS/SaaS with tests, CI, Docker, and multi-tenant RLS. It has portfolio/recruiting value but contains client-specific branding and seed data; keep private and active, optionally surfacing a sanitized public case study if WR Consultoria consents.

#### Plataforma-de-Monitoramento-de-Sistemas-e-APIs

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 5 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 4 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 2 |
| Recruiting Value | 4 |
| Software House Value | 2 |
| Ip Publication Safety | 5 |
| **Overall Average** | **3.40** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** High technical-depth portfolio piece (Clean Architecture, Java 21, observability) that is safe to publish under MIT. Prerequisite: remove versioned node_modules and update the stale roadmap checkboxes to reflect the implemented MVP.

#### Portfolio-LeonardoFragoso-React

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 4 |
| Production Evidence | 3 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 0 |
| Current Relevance | 4 |
| Recruiting Value | 5 |
| Software House Value | 3 |
| Ip Publication Safety | 3 |
| **Overall Average** | **3.10** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** This is the current personal portfolio that will be rebuilt after classification. It is live, public, and serves as the primary professional showcase. Keep public as the showcase. The sensitive PDFs (CNPJ card, contrato social) in public/Docs/ should be removed before or during the rebuild.

#### ProFlow

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 2 |
| Differentiation | 3 |
| Documentation | 3 |
| Test Quality | 3 |
| Current Relevance | 5 |
| Recruiting Value | 4 |
| Software House Value | 3 |
| Ip Publication Safety | 1 |
| **Overall Average** | **3.20** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** CRITICAL: real production credentials (OpenAI, Google OAuth, GitHub OAuth, Mercado Pago, Django secret) are recoverable in git history. Must be made private and credentials rotated immediately. After history scrubbing and CI fix, could return as a public showcase.

#### PyScriptTech

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 5 |
| Production Evidence | 4 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 1 |
| Current Relevance | 5 |
| Recruiting Value | 4 |
| Software House Value | 5 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.90** |

- **Recommended destination:** `REBRAND_REBUILD`
- **Rationale:** This is the future software-house rebrand target. The codebase has a solid foundation (React 18, Supabase, CRM dashboard, auth, ProFlow integration, 13 SEO landing pages, ROI calculator) that justifies rebuilding under a new brand rather than archiving. Branding is deeply embedded and requires comprehensive rebranding across source, docs, and infrastructure.

#### SGE-Django

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 2 |
| Business Relevance | 1 |
| Production Evidence | 0 |
| Differentiation | 1 |
| Documentation | 2 |
| Test Quality | 0 |
| Current Relevance | 1 |
| Recruiting Value | 1 |
| Software House Value | 1 |
| Ip Publication Safety | 5 |
| **Overall Average** | **1.40** |

- **Recommended destination:** `ARCHIVE_PUBLIC`
- **Rationale:** Old, superseded Django learning project with no ongoing value. Safe to archive publicly as an early-career artifact; no IP concerns.

#### SaaS

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 3 |
| Production Evidence | 1 |
| Differentiation | 3 |
| Documentation | 3 |
| Test Quality | 2 |
| Current Relevance | 2 |
| Recruiting Value | 3 |
| Software House Value | 3 |
| Ip Publication Safety | 4 |
| **Overall Average** | **2.80** |

- **Recommended destination:** `KEEP_PRIVATE_ACTIVE`
- **Rationale:** Personal SaaS R&D with only 1 of 6 products built; keep private while the ecosystem matures. The implemented BI-as-a-Service module could later be extracted as a public showcase if hardened.

#### Sistema-de-compras

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 2 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 1 |
| Documentation | 2 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 1 |
| Software House Value | 2 |
| Ip Publication Safety | 2 |
| **Overall Average** | **1.70** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Client project for 'Ziran' with internal business process documents, corporate SLA data, and company branding committed to git. README misleadingly claims a modern tech stack. Should be made private to protect client data and business processes.

#### YardMaster

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 2 |
| Software House Value | 2 |
| Ip Publication Safety | 1 |
| **Overall Average** | **2.10** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Former iTracker/ICTSI corporate yard management system with operational data, tracked SQLite database, and internal references. The README's multi-tenant/white-label claims are misleading. Should be made private and cleaned of corporate data before any public showcase consideration.

#### alzi-project

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 2 |
| Business Relevance | 2 |
| Production Evidence | 1 |
| Differentiation | 1 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 1 |
| Software House Value | 1 |
| Ip Publication Safety | 3 |
| **Overall Average** | **1.60** |

- **Recommended destination:** `KEEP_PRIVATE_ACTIVE`
- **Rationale:** Private utility with possible real operational data in committed spreadsheets; should remain private. Low portfolio value as a standalone script but useful as supporting evidence of data-processing work.

#### aviator-banca

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 1 |
| Production Evidence | 1 |
| Differentiation | 1 |
| Documentation | 2 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 1 |
| Software House Value | 1 |
| Ip Publication Safety | 5 |
| **Overall Average** | **1.70** |

- **Recommended destination:** `ARCHIVE_PRIVATE`
- **Rationale:** Simple personal CRUD app with no secrets and no production deployment. Stale since January 2026. Safe to archive as a personal project — no security concerns but limited showcase value.

#### base-corporativa

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 4 |
| Production Evidence | 4 |
| Differentiation | 3 |
| Documentation | 3 |
| Test Quality | 1 |
| Current Relevance | 4 |
| Recruiting Value | 3 |
| Software House Value | 4 |
| Ip Publication Safety | 3 |
| **Overall Average** | **3.30** |

- **Recommended destination:** `KEEP_PRIVATE_ACTIVE`
- **Rationale:** Personal e-commerce business with a live deployment at basecorporativa.store. Must remain private due to CRITICAL secret exposure (production AWS keys, payment gateway tokens, database credentials hardcoded in tracked files). Immediate secret rotation and git history cleanup required.

#### dash-monitor

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 2 |
| Business Relevance | 2 |
| Production Evidence | 2 |
| Differentiation | 1 |
| Documentation | 3 |
| Test Quality | 0 |
| Current Relevance | 3 |
| Recruiting Value | 1 |
| Software House Value | 1 |
| Ip Publication Safety | 1 |
| **Overall Average** | **1.60** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** This is an internal iTracker/ICTSI corporate monitoring tool exposing internal IP addresses, service names, and dashboard screenshots. Public distribution risks exposing corporate infrastructure details. Should be made private pending review.

#### desafio-focon

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 5 |
| Business Relevance | 3 |
| Production Evidence | 4 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 4 |
| Current Relevance | 5 |
| Recruiting Value | 5 |
| Software House Value | 2 |
| Ip Publication Safety | 3 |
| **Overall Average** | **3.80** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Strong technical hiring-challenge showcase with live deployment, CI, tests and migrations demonstrating full-stack competence. Keep public as a portfolio piece; the Fócon brand is used in a challenge context with no commercial engagement evidence, so publication is acceptable with a note.

#### devpro-e2e-sandbox

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 2 |
| Business Relevance | 1 |
| Production Evidence | 1 |
| Differentiation | 1 |
| Documentation | 3 |
| Test Quality | 2 |
| Current Relevance | 3 |
| Recruiting Value | 1 |
| Software House Value | 1 |
| Ip Publication Safety | 5 |
| **Overall Average** | **2.00** |

- **Recommended destination:** `SUPPORTING_INFRA_PRIVATE`
- **Rationale:** Private E2E test sandbox for the DevPro orchestrator — should remain private as supporting infrastructure. The 15 open PRs and 17 branches are automated test artifacts, not pending human work.

#### exnova-api

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 2 |
| Production Evidence | 2 |
| Differentiation | 1 |
| Documentation | 2 |
| Test Quality | 1 |
| Current Relevance | 4 |
| Recruiting Value | 2 |
| Software House Value | 1 |
| Ip Publication Safety | 4 |
| **Overall Average** | **2.20** |

- **Recommended destination:** `KEEP_PRIVATE_ACTIVE`
- **Rationale:** Active personal trading bot with clean secret hygiene (all credentials via env vars, proper .gitignore). Keep private as it's a personal tool with no showcase value, but no urgent security concerns.

#### nao-conformidade

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 2 |
| Documentation | 3 |
| Test Quality | 1 |
| Current Relevance | 3 |
| Recruiting Value | 2 |
| Software House Value | 2 |
| Ip Publication Safety | 1 |
| **Overall Average** | **2.20** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Corporate iTracker quality management system with employee emails, corporate branding, and references to internal quality process documents. Should remain private as it contains employer proprietary workflows and personnel information.

#### pimenta

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 1 |
| Business Relevance | 1 |
| Production Evidence | 1 |
| Differentiation | 1 |
| Documentation | 2 |
| Test Quality | 0 |
| Current Relevance | 2 |
| Recruiting Value | 0 |
| Software House Value | 1 |
| Ip Publication Safety | 3 |
| **Overall Average** | **1.20** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** Simple adult-content landing page with node_modules committed and no .gitignore. No engineering rigor (tests, CI, Docker). Should be made private pending review and cleanup — remove node_modules, add .gitignore, and assess whether the content is appropriate for a public professional portfolio.

#### sanduicherie

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 5 |
| Business Relevance | 3 |
| Production Evidence | 3 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 4 |
| Current Relevance | 5 |
| Recruiting Value | 4 |
| Software House Value | 4 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.90** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Excellent portfolio piece demonstrating modern full-stack architecture, comprehensive testing, CI/CD, and Docker. No IP concerns. The test JWT placeholders are clearly labeled and pose no security risk. Should be showcased publicly as a primary technical demonstration.

#### vigil-ai

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 4 |
| Business Relevance | 3 |
| Production Evidence | 2 |
| Differentiation | 3 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 3 |
| Recruiting Value | 4 |
| Software House Value | 2 |
| Ip Publication Safety | 4 |
| **Overall Average** | **3.20** |

- **Recommended destination:** `SHOWCASE_PUBLIC`
- **Rationale:** Excellent multi-agent AI hiring-case artifact demonstrating async agents, testing, and deploy readiness — strong public portfolio piece with no IP risk (fictional case scenario).

#### wrconsultoriaesolucoes

| Dimension | Score (0-5) |
|---|---|
| Technical Depth | 3 |
| Business Relevance | 5 |
| Production Evidence | 5 |
| Differentiation | 2 |
| Documentation | 4 |
| Test Quality | 3 |
| Current Relevance | 5 |
| Recruiting Value | 2 |
| Software House Value | 4 |
| Ip Publication Safety | 0 |
| **Overall Average** | **3.30** |

- **Recommended destination:** `MAKE_PRIVATE_PENDING_REVIEW`
- **Rationale:** A live client/company production WordPress site containing commercial premium plugins (Elementor Pro, Yoast SEO Premium) that cannot be publicly redistributed, plus proprietary WR Consultoria business documents and production consent records. Must be made private; the premium plugins and business PDFs should be removed from the repo entirely (and history scrubbed) before any showcase use.

---
## 4. Destination Distribution

- **SHOWCASE_PUBLIC** (15): Showcase — keep public as flagship portfolio piece
- **MAKE_PRIVATE_PENDING_REVIEW** (13): Make private pending IP/security review
- **KEEP_PRIVATE_ACTIVE** (6): Keep private, actively maintained
- **SHOWCASE_PRIVATE_WITH_PUBLIC_CASE** (2): Keep code private, publish a sanitized case study
- **REBRAND_REBUILD** (2): Rebrand and rebuild for software-house launch
- **ARCHIVE_PUBLIC** (2): Archive (currently public)
- **SUPPORTING_INFRA_PRIVATE** (1): Private supporting infrastructure
- **KEEP_PUBLIC_SECONDARY** (1): Keep public as secondary portfolio piece
- **ARCHIVE_PRIVATE** (1): Archive (currently private)

---
## 5. Contradictory / Overstated README Claims

### Digital-Signage-Platform
- Self-authored LEGAL_COMPLIANCE_REPORT.md claims 'CLEARED FOR COMMERCIALIZATION' / 'Sanitized Sensitive Data', but git history still contains real DB credentials at commit 17f5403 (secrets/db_credentials.txt). Scrubbing a later commit does not purge secrets from history. Claim is misleading.

### FlowTrack
- LEGAL_REVIEW_SUMMARY claims brand references were removed, but README still names ICTSI. Git history contains nohup.out with session/CSRF tokens (179 gitleaks findings, history-only). Claim is contradicted by evidence.

### Go-API-Gestao-de-Projetos-e-Tarefas
- README claims 'Pronto para produção' but there are ZERO tests and NO CI. The roadmap lists tests as future 'Phase 2'. Production-ready claim is not supported.

### MedFlow_Finance
- README claims 'PROJETO 100% PRONTO PARA EXECUÇÃO E DEMONSTRAÇÃO COMERCIAL' while its own 'Próximas Etapas > Imediato' lists unchecked items: 'Executar projeto localmente', 'Testar fluxo completo', 'Validar integrações'. AUDIT_REPORT_COMPLETE.md self-rates 85% and lists 'Ausência Total de Testes Automatizados' as critical. The '100% ready' claim is NOT supported by test/CI/migration evidence.

### Oraculo
- README claims 'v4.0.0 — Hardening & Production-Ready' and positions vs Palantir/Databricks/Snowflake, but: NO CI (no .github/workflows), only 8 test files, only 2 migrations, mock email fallback, TF-IDF fallback RAG, committed sample chat history and legacy code. Real integrations exist (DuckDB NL2SQL, FAISS, PostgreSQL) but 'production-ready' is overstated.

### Plataforma-de-Monitoramento-de-Sistemas-e-APIs
- README 'Funcionalidades Principais' marks 6 features as ✅ complete while the Roadmap lists the same MVP items as unchecked `[ ]`. **Code inspection confirms the features ARE implemented** (128 Java files, 5 entities, WebSocket, 6 Flyway migrations, 14 test files). The roadmap is stale/outdated — the feature list is accurate, but the roadmap contradicts it. Also: node_modules is versioned (100 tracked files).

### ProFlow
- Contains real features (project management, payments) alongside seed/engagement/simulated behavior: fake_project_generator.py, is_simulated payment fields, seed_test_data command, and a commit titled 'seed engagement projects system - honest notifications, simulated payments'. Must distinguish real product capabilities from generated/demo data.

### Sistema-de-compras
- README claims Vue.js 3.4 + FastAPI + PostgreSQL + Docker, but the actual code is a Streamlit app with SQLite. The claimed 'migration from Streamlit MVP to scalable architecture' was never implemented.

### YardMaster
- README claims '100% White Label' and 'Multi-tenant — Suporte a múltiplas empresas/operações' but code shows: NO tenant model, NO org_id/empresa_id/tenant_id columns, NO tenant middleware. whitelabel_config.py has ENABLE_MULTI_TENANT = False (disabled), TENANT_ID = 'default' (single static tenant). TenantConfigLoader.load_from_database() is a stub with commented-out SQL. The 'white label' transformation was purely cosmetic (CSS class renaming + logo file rename). Multi-tenant/white-label claim DOES NOT HOLD.

