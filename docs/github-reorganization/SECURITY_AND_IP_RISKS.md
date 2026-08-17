# Security & IP Risks — Phase 1 Audit

**Account:** LeonardoRFragoso
**Audit date:** 2026-08-17

> **CRITICAL RULE:** No secret values are printed in this document. Only secret TYPE, location, presence in current tree vs. history, and remediation priority are reported.

## Executive Summary

- **Repositories with CRITICAL findings:** 6 — ProFlow, base-corporativa, MVP-linkedin-bot, Bot_IqOption, FinanceControl, Digital-Signage-Platform
- **Repositories with HIGH findings:** 8 — PayFlow-AI, Portfolio-LeonardoFragoso-React, MVP-linkedin-bot, Bot_IqOption, FlowTrack, Bet-IA-BOT, YardMaster, Digital-Signage-Platform
- **Repositories with versioned build artifacts / dependencies:** 11
- **Repositories with versioned databases / dumps:** 12

## CRITICAL Security Findings (Immediate Rotation Required)

These repositories contain real credentials in the current tree or git history. All credentials must be treated as **COMPROMISED** and rotated immediately.

### ProFlow (PUBLIC)

- **Path:** `RAILWAY_ENV_FINAL.txt`
  - **Secret type:** generic-token
  - **In current tree:** False
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** Full production env file committed to history with real credentials: Django SECRET_KEY (prod-...), OpenAI API key (sk-proj-...), Google OAuth client secret (GOCSPX-...), GitHub OAuth client secret, Mercado Pago access token (APP_USR-...), MP client secret, MP webhook secret. Removed from current tree but recoverable from git history.

- **Path:** `DEPLOY_CHECKLIST.md`
  - **Secret type:** generic-token
  - **In current tree:** False
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** Deploy checklist committed to history duplicating the same real production credentials (Django secret, OpenAI key, Google/GitHub OAuth secrets, Mercado Pago token/secret). Removed from current tree.

### base-corporativa (PUBLIC)

- **Path:** `RAILWAY_ENV_ATUALIZADO.txt`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** CRITICAL
  - **Note:** Tracked plaintext env file with real production credentials: AWS R2 access keys, MercadoPago access token and public key, MelhorEnvio client ID/secret/API token, database public URL. All values appear to be real production secrets.

- **Path:** `backend/.env.railway`
  - **Secret type:** .env
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** CRITICAL
  - **Note:** Tracked .env file with real production credentials: AWS R2 keys, database URL with credentials, Django superuser email/password, SendGrid API key, MercadoPago tokens, MelhorEnvio tokens. .gitignore covers .env but NOT .env.railway.

- **Path:** `backend/fix_product_images_r2.py`
  - **Secret type:** aws-key
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** CRITICAL
  - **Note:** Hardcoded Cloudflare R2 access key and secret key directly in Python source code (R2_ACCESS_KEY, R2_SECRET_KEY variables).

- **Path:** `backend/list_r2_images.py`
  - **Secret type:** aws-key
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** CRITICAL
  - **Note:** Hardcoded Cloudflare R2 access key and secret key directly in Python source code.

- **Path:** `backend/upload_pdfs_to_r2.py`
  - **Secret type:** aws-key
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** CRITICAL
  - **Note:** Hardcoded Cloudflare R2 access key and secret key directly in Python source code.

- **Path:** `backend/upload_product_images_to_r2.py`
  - **Secret type:** aws-key
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** CRITICAL
  - **Note:** Hardcoded Cloudflare R2 access key and secret key directly in Python source code.

### MVP-linkedin-bot (PRIVATE)

- **Path:** `Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot/Default/Preferences`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** Chrome browser profile committed to git — contains policy_recovery_token and receiver_id_hash_token (session authentication tokens for Chrome sync/sign-in)

- **Path:** `Auto_job_applier_linkedIn/V2-Completa/chrome_profile_linkedin_bot/Default/Preferences`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** Chrome browser profile committed to git — contains policy_recovery_token and receiver_id_hash_token (session authentication tokens)

### Bot_IqOption (PRIVATE)

- **Path:** `bot_iqoption_v2/backend/.env`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** Production .env file committed to git — contains MercadoPago production credentials (MERCADOPAGO_PUBLIC_KEY, MERCADOPAGO_ACCESS_TOKEN, MERCADOPAGO_CLIENT_ID, MERCADOPAGO_CLIENT_SECRET) marked as 'PRODUÇÃO' in comments

- **Path:** `bot_iqoption_v2/backend/RAILWAY_ENV_COMPLETE.txt`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** Complete Railway environment file committed to git — contains SECRET_KEY, MERCADOPAGO_ACCESS_TOKEN, MERCADOPAGO_CLIENT_SECRET and all production environment variables

- **Path:** `bot_iqoption_v2/backend/bot_iqoption.log`
  - **Secret type:** jwt
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** 197 JWT tokens found in committed log file — trading session WebSocket authentication tokens from IQ Option API, exposing live trading session data

- **Path:** `bot_iqoption_v2/backend/keys/user_2_key.key`
  - **Secret type:** private-key
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** User API key file (44 bytes) committed to git — per-user encryption/authentication key

- **Path:** `bot_iqoption_v2/backend/keys/user_3_key.key`
  - **Secret type:** private-key
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** User API key file (44 bytes) committed to git — per-user encryption/authentication key

- **Path:** `bot_iqoption_v2/backend/keys/user_4_key.key`
  - **Secret type:** private-key
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** User API key file (44 bytes) committed to git — per-user encryption/authentication key

### FinanceControl (PUBLIC)

- **Path:** `chave-EC2/Finance2.pem`
  - **Secret type:** private-key
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** RSA private key (EC2 key pair) committed and present in current tree. Also appeared in history at backend/chave-EC2/Finance2.pem (commit 1bd26c7) before path moved. Must be revoked/rotated and removed from history.

### Digital-Signage-Platform (PUBLIC)

- **Path:** `secrets/db_credentials.txt`
  - **Secret type:** db-password
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** CRITICAL
  - **Note:** File added at commit 17f5403 with REAL DB credentials (DB name, User, Password, RootPassword - non-placeholder values). Later sanitized to a template at commit f73b8fe ('white label preparation'), but the original real credential values remain recoverable in git history. The current-tree version still contains non-placeholder Password/RootPassword values despite a 'TEMPLATE' header.

## HIGH Security Findings

### PayFlow-AI (PUBLIC)

- **Path:** `Docs/CORRIGIR_TOKEN.txt`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Real-looking Twilio auth token (32-hex) committed in a troubleshooting doc with explicit instructions to paste it into .env. Live credential exposed in current tree.

### Portfolio-LeonardoFragoso-React (PUBLIC)

- **Path:** `public/Docs/cartao cnpj.pdf`
  - **Secret type:** customer-data
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** CNPJ business card PDF (260KB) committed to public repo. Contains personal/business tax registration information.
- **Path:** `public/Docs/contrato-social-cnpj.pdf`
  - **Secret type:** customer-data
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** CNPJ articles of association PDF (1.4MB) committed to public repo. Contains sensitive business registration documents.

### MVP-linkedin-bot (PRIVATE)

- **Path:** `Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot/Default/BrowsingTopicsState`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Chrome profile file with hex_encoded_hmac_key — browser session cryptographic material committed to repo
- **Path:** `Auto_job_applier_linkedIn/V2-Completa/chrome_profile_linkedin_bot/Default/BrowsingTopicsState`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Chrome profile file with hex_encoded_hmac_key — browser session cryptographic material committed to repo
- **Path:** `Auto_job_applier_linkedIn/V1/chrome_profile_linkedin_bot/Snapshots/142.0.7444.176/Default/Preferences`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Chrome profile snapshot with policy_recovery_token — session token committed to repo
- **Path:** `Auto_job_applier_linkedIn/V1/logs/log.txt`
  - **Secret type:** other
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Large log file (53k+ lines) containing LinkedIn page content, session data, and application details captured during bot execution
- **Path:** `cpf.pdf`
  - **Secret type:** customer-data
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Brazilian national ID (CPF) document in PDF format committed to repo root — sensitive personal identification document

### Bot_IqOption (PRIVATE)

- **Path:** `bot_iqoption_v2/backend/.env.example`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Example env file contains real MERCADOPAGO_CLIENT_SECRET value instead of placeholder — credential leaked in example file
- **Path:** `bot_iqoption_v2/backend/RAILWAY_ENV_TEMPLATE.md`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Railway env template contains real MERCADOPAGO_CLIENT_SECRET value instead of placeholder

### FlowTrack (PUBLIC)

- **Path:** `nohup.out`
  - **Secret type:** customer-data
  - **In current tree:** False
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** A runtime server log (nohup.out) was committed in the initial commit 83a021b and removed in commit 377713b ('White Label transformation'). gitleaks found 179 findings in it - all CSRF/session tokens from SecureCookieSession objects (e.g. csrf_token hashes) captured from live application traffic. These are leaked session artifacts in git history, not static credentials, but they expose runtime session data from the production GR/operations system.

### Bet-IA-BOT (PRIVATE)

- **Path:** `backend/test_new_api.py`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Hardcoded API-Football API key in test script (line 11) — real API credential committed to source code instead of using environment variable

### YardMaster (PUBLIC)

- **Path:** `venv/`
  - **Secret type:** node_modules
  - **In current tree:** True
  - **In git history:** False
  - **Priority:** HIGH
  - **Note:** 8328 virtualenv files tracked in git including all site-packages. Massive repository bloat and potential supply-chain exposure.

### Digital-Signage-Platform (PUBLIC)

- **Path:** `.env.tv`
  - **Secret type:** generic-token
  - **In current tree:** True
  - **In git history:** True
  - **Priority:** HIGH
  - **Note:** Committed env file in current tree containing a weak hardcoded JWT_SECRET_KEY (tvs-jwt-secret-key-2024, 23 chars) and a SECRET_KEY. DATABASE_URL present but is a sqlite path (no user:pass@host). gitleaks flagged the JWT secret.

## MEDIUM & LOW Findings

### API_Analyze (PUBLIC)
- [MEDIUM] `V2/backend/.env.example` — generic-token — current_tree=True history=True — NEWS_API_KEY in .env.example contains a potentially real 32-char hex API key (not a placeholder pattern). Should be rotated if real.
- [MEDIUM] `V2/backend/.env.example` — generic-token — current_tree=True history=True — ALPHA_VANTAGE_API_KEY in .env.example contains a potentially real Alpha Vantage key (not a placeholder pattern). Should be rotated if real.
- [LOW] `V2/backend/db.sqlite3` — other — current_tree=True history=True — SQLite database file (253KB) committed to repo. May contain user data or cached financial data.

### AgentesIA-Consultoria-de-Negocios-com-IA-Multi-Agentes (PUBLIC)
- [LOW] `backend/test_auth.py` — generic-token — current_tree=True history=True — gitleaks flagged 'SEU_ACCESS_TOKEN' (Portuguese for 'YOUR_ACCESS_TOKEN') in a curl example string inside a manual test script. This is a placeholder label, not a real credential.
- [LOW] `backend/.env.development` — .env — current_tree=True history=True — Versioned dev-only .env containing a placeholder JWT_SECRET_KEY marked 'dev-only-secret-key-change-in-production'; ANTHROPIC_API_KEY left blank/commented. No real credentials, but committing a .env file is bad practice.

### AndaimesPini_Project (PUBLIC)
- [MEDIUM] `database/db.sqlite3` — customer-data — current_tree=True history=True — Versioned SQLite database (40KB) possibly containing client rental/business data for Andaimes Pini.
- [LOW] `backend/*.sqlite_backup` — customer-data — current_tree=True history=True — 18 .sqlite_backup files versioned alongside migration scripts (create_admin.py.sqlite_backup, models/*.sqlite_backup, routes/*.sqlite_backup) — leftover backup artifacts.

### Bot_IqOption (PRIVATE)
- [MEDIUM] `bot_iqoption_v2/backend/db.sqlite3` — sql-dump — current_tree=True history=True — SQLite database committed to git — may contain user accounts, trading data, and session information
- [LOW] `bot_iqoption_v2/backend/venv/` — binary-artifact — current_tree=True history=True — Python venv directory (13,661 tracked files) committed to git — should be in .gitignore

### Digital-Signage-Platform (PUBLIC)
- [MEDIUM] `.env.production` — .env — current_tree=True history=True — Committed production env file in current tree (contains REACT_APP_API_URL / REACT_APP_SOCKET_URL). No direct secrets detected by gitleaks but a committed .env.production is a hygiene risk.
- [MEDIUM] `multiple (.env.example, backend/.env.production.example, backend/app.py, backend/tools/migrate_sqlite_to_mysql.py)` — db-password — current_tree=True history=True — History (commits 035ca7c, 222fbad, b3f287a, df23a1a) contained DATABASE_URL examples referencing the corporate database name 'tvs_itracker' (mysql+pymysql://root:password@localhost:3306/tvs_itracker). The 'root:password' is a default dev credential but the DB name ties the code to the iTracker corporate environment. References were partially scrubbed in the white-label commit f73b8fe but persist in history.

### FinanceControl (PUBLIC)
- [LOW] `backend/README.md` — jwt — current_tree=False history=True — Truncated example JWT (eyJ0eXAi... with '...' suffix) shown in API documentation example at line 223 (commit 211f864). Demo/doc token, not a real credential; file no longer in current tree.
- [MEDIUM] `backend/db.sqlite3` — customer-data — current_tree=True history=True — Versioned SQLite database (364KB) potentially containing user financial/transaction data.
- [LOW] `ReciboDePagamento_3_01122025173256_408_b479a41d.pdf` — customer-data — current_tree=True history=True — Versioned payment receipt PDF (8KB) — personal/financial document, should not be in repo.

### FlowTrack (PUBLIC)
- [MEDIUM] `Backend/config.py` — generic-token — current_tree=True history=True — Hardcoded weak fallback SECRET_KEY: os.getenv('SECRET_KEY', 'segredo-super-seguro') with a comment 'MUST be changed in production'. A weak default secret shipped in source is a risk if the env var is unset in deployment.

### FragTech-Fintech (PUBLIC)
- [LOW] `src/pages/Pix.tsx` — generic-api-key — current_tree=True history=True — gitleaks flagged the obviously fake example UUID 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' used as a demo Pix key in mock data. This is a placeholder, not a real credential.

### Legal-AI-Copilot (PUBLIC)
- [LOW] `AUTHENTICATION.md` — jwt — current_tree=True history=True — Truncated example JWTs ('eyJhbGciOiJIUzI1NiIs...') in authentication API documentation showing login response shape. Not real tokens.
- [LOW] `AUTHENTICATION.md` — oauth — current_tree=True history=True — Placeholder bearer tokens in curl examples in authentication documentation. Documentation examples only.
- [LOW] `IMPLEMENTATION_SUMMARY.md` — oauth — current_tree=True history=True — Placeholder 'YOUR_TOKEN' bearer token in curl example in implementation summary. Documentation example only.

### LogiFlow (PUBLIC)
- [MEDIUM] `LogiFlow CRM/backend/docs/MODULO_WHATSAPP.md` — generic-token — current_tree=True history=True — Evolution API key 'logiflow-evolution-key-2025' in documentation. Appears to be a real API key pattern, not a placeholder. Also found in 3 other docs files and evolution-api/README.md (8 total occurrences). Should be rotated.
- [LOW] `LogiFlow CRM/docs/MELHOR_ENVIO_SETUP.md` — jwt — current_tree=True history=True — JWT-style tokens in documentation (Melhor Envio setup guide). Appear to be truncated/example JWTs. Also found in SUITECRM_INSTALL.md, api/getting-started.md, and several guides/ files.
- [LOW] `LogiFlow CRM/docs/IMPLEMENTACAO_COMPLETA.md` — generic-token — current_tree=True history=True — MercadoPago test token (TEST- prefix) in documentation. Test environment token, not production.
- [LOW] `LogiFlow CRM/docs/guides/SETUP_COTACOES_AUTOMATICAS.md` — generic-token — current_tree=True history=True — Google Maps API key placeholder (AIzaSyC1234...) and Frenet/Melhor Envio example tokens in documentation. All appear to be example/placeholder values.
- [LOW] `LogiFlow CRM/backend/.env.docker` — db-password — current_tree=True history=True — Default Docker Compose passwords (DB_ROOT_PASSWORD=rootpass123, DB_PASSWORD=logiflow123, REDIS_PASSWORD=redis123). Clearly marked as docker compose defaults but should use secrets in production.
- [LOW] `LogiFlow CRM/docs/guides/SETUP_FOCUSNFE.md` — generic-token — current_tree=True history=True — FocusNFe example tokens (homologacao_abcdef..., producao_abcdef...) in documentation. Placeholder values.
- [LOW] `LogiFlow CRM/docs/guides/SETUP_EVOLUTION_API.md` — generic-token — current_tree=True history=True — Evolution API example key (evo_123abc456...) and placeholder curl auth headers in documentation.
- [LOW] `LogiFlow CRM/docs/guides/CONFIGURAR_OAUTH2_SUITECRM.md` — oauth — current_tree=True history=True — OAuth2 client secret examples and access token placeholders in SuiteCRM integration guide.
- [LOW] `LogiFlow CRM/app-motorista/.env.production` — other — current_tree=True history=True — Production .env file committed with Railway API URL (https://logiflow-api-production-3447.up.railway.app). Not a secret per se but exposes production infrastructure URL. Also in portal-cliente/.env.production and frontend/.env.production.

### MVP-linkedin-bot (PRIVATE)
- [MEDIUM] `perguntas.csv` — customer-data — current_tree=True history=True — CSV with personal phone number and company names from LinkedIn job applications — PII data committed to repo
- [LOW] `Auto_job_applier_linkedIn/V1/venv/` — binary-artifact — current_tree=True history=True — Python venv directory (26,655 tracked files) committed to git — should be in .gitignore
- [LOW] `Auto_job_applier_linkedIn/V2-Completa/venv/` — binary-artifact — current_tree=True history=True — Python venv directory committed to git — should be in .gitignore

### Oraculo (PUBLIC)
- [MEDIUM] `users.json` — generic-token — current_tree=False history=True — SHA256-hashed user passwords (admin, comercial, etc.) committed in legacy users.json in git history. Hashes are crackable; contains role/permission metadata. Removed from current tree.
- [LOW] `gptracker_simple.py` — generic-token — current_tree=False history=True — Example/placeholder OpenAI API key string ('sk-proj-abc123...') in legacy GPTRACKER instructions. Not a real credential.
- [LOW] `MELHORIAS_IMPLEMENTADAS.md` — jwt — current_tree=False history=True — Truncated example JWT ('eyJ0eXAiOiJKV1QiLCJhbGc...') in a markdown improvement report. Documentation example, not a real token.

### PayFlow-AI (PUBLIC)
- [LOW] `README.md` — generic-token — current_tree=True history=True — SECRET_KEY placeholder example ('sua-secret-key-gerada-com-64-ou-mais-caracteres') in README security section. Not a real secret.

### Plataforma-Cursos-WRConsultoria (PUBLIC)
- [LOW] `.github/workflows/ci.yml` — generic-token — current_tree=True history=True — 5 gitleaks findings, all test/dummy fixtures in the CI workflow: SECRET_KEY='test-secret-key-at-least-32-characters-long', 'dummy-secret-key-at-least-32-characters-long-xxx', and a base64 test TENANT_SECRET_ENCRYPTION_KEY. Clearly labeled test values used by the test job, not real credentials.
- [LOW] `USUARIOS_TESTE.md` — customer-data — current_tree=True history=True — Test-users doc lists default demo credentials (e.g. admin password 'admin123') and demo emails (admin@wrcursos.com.br, student@wrcursos.com.br). These are seeded demo accounts, not real customer data, but committing default credentials is a hygiene issue.

### Portfolio-LeonardoFragoso-React (PUBLIC)
- [MEDIUM] `public/Leonardo Fragoso _ Python Backend Developer.pdf` — other — current_tree=True history=True — CV/resume PDF (898KB) committed to public repo. Contains personal contact information and work history.

### ProFlow (PUBLIC)
- [LOW] `Docs/API_DOCUMENTATION.txt` — jwt — current_tree=True history=True — Truncated example JWTs ('eyJ0eXAiOiJKV1QiLCJhbGc...') and example password 'password123' in API documentation. Not real credentials.
- [LOW] `ASAAS_TEST_INSTRUCTIONS.md` — generic-token — current_tree=False history=True — Placeholder JWT tokens ('seu-token-jwt-aqui', truncated 'eyJhbGci...') in Asaas testing instructions. Not real credentials.
- [LOW] `ASAAS_SANDBOX_SETUP.md` — oauth — current_tree=False history=True — Placeholder bearer tokens in curl examples for Asaas sandbox setup. Documentation examples only.
- [LOW] `ASAAS_TESTING_GUIDE.md` — oauth — current_tree=False history=True — Placeholder bearer tokens in curl examples in Asaas testing guide. Documentation examples only.
- [LOW] `CRITICAL_FEATURES_IMPLEMENTATION.md` — oauth — current_tree=False history=True — Placeholder bearer tokens in curl examples in critical features implementation doc. Documentation examples only.
- [LOW] `AÇÕES_IMEDIATAS.md` — oauth — current_tree=False history=True — Placeholder bearer tokens in curl examples in immediate-actions doc. Documentation examples only.
- [LOW] `PROCESSO_REDEFINICAO_SENHA.md` — generic-token — current_tree=False history=True — Example password-reset tokens ('abc123def456...', 'MQ==') and example passwords in password-reset process documentation. Not real credentials.
- [LOW] `SECURITY_RETEST.md` — oauth — current_tree=False history=True — Placeholder bearer token ('token_user_a') in security retest curl examples. Documentation example only.

### SGE-Django (PRIVATE)
- [LOW] `app/settings.py` — generic-token — current_tree=True history=True — Django-generated 'django-insecure-...' SECRET_KEY hardcoded in settings.py with DEBUG=True. This is the default dev key (not a real production secret), but should be env-loaded. Single commit, no rotation in history.

### SaaS (PRIVATE)
- [LOW] `1. SaaS de Business Intelligence Automático (BI-as-a-Service)/backend/db.sqlite3` — customer-data — current_tree=True history=True — Versioned SQLite database in the BI-as-a-Service backend; may contain demo/tenant data. Private repo.

### Sistema-de-compras (PUBLIC)
- [MEDIUM] `compras_sla.db` — sql-dump — current_tree=True history=False — SQLite database tracked in git despite .gitignore listing 'compras_sla.db'. Contains business purchasing data and potentially user information.
- [MEDIUM] `Compras_SLA .xlsx` — customer-data — current_tree=True history=False — Excel spreadsheet with business purchasing/SLA data tracked in git. Contains corporate business process data.
- [MEDIUM] `Fluxo utilizado hoje pela empresa.docx` — customer-data — current_tree=True history=False — Word document describing current company purchasing workflow/process tracked in git. Exposes internal business processes.
- [LOW] `descrição.opus` — binary-artifact — current_tree=True history=False — Audio file (.opus) tracked in git. Binary artifact that should not be version controlled.
- [LOW] `docs/Guia_de_Testes.pdf` — binary-artifact — current_tree=True history=False — PDF test guide tracked in git. Binary artifact.
- [LOW] `assets/img/logo_ziran.jpg, assets/img/ziran fundo.jpg, img2.jpg` — binary-artifact — current_tree=True history=False — Image files (Ziran brand logo and background) tracked in git.

### YardMaster (PUBLIC)
- [MEDIUM] `database.db` — sql-dump — current_tree=True history=False — SQLite database tracked in git containing operational data (users, containers, operations, logs). May contain user hashes and operational records.
- [MEDIUM] `bkp/database.db.bak.20250617124206` — sql-dump — current_tree=True history=False — Multiple SQLite database backup files in bkp/ directory tracked in git (3 .bak files). Contains operational data snapshots.
- [MEDIUM] `__pycache__/ (recursive)` — binary-artifact — current_tree=True history=False — 3158 .pyc compiled Python files tracked in git across the project.
- [LOW] `app.py.backup_20250803_131833` — binary-artifact — current_tree=True history=False — Backup copy of main application file tracked in git.
- [LOW] `app.log` — other — current_tree=True history=False — Application log file tracked in git.

### alzi-project (PRIVATE)
- [MEDIUM] `TC.xls` — customer-data — current_tree=True history=True — Versioned port container tracking spreadsheet (.xls, 476KB) with real operational data; possible customer/employer operational data. Paired with TC.xlsx and TC_output.xlsx.
- [MEDIUM] `TC_output.xlsx` — customer-data — current_tree=True history=True — Generated output spreadsheet (239KB) derived from TC.xls containing processed container operational data.

### dash-monitor (PUBLIC)
- [LOW] `V2-Dash/backend/.env` — .env — current_tree=True history=False — Tracked .env file but contains only non-sensitive dev config (FLASK_ENV=development, FLASK_DEBUG=1, CORS_ORIGINS=localhost). No real credentials.
- [MEDIUM] `V2-Dash/backend/app/domain/services_config.py` — customer-data — current_tree=True history=False — Contains internal corporate IP addresses (192.168.0.45) and internal service names/ports for iTracker/ICTSI infrastructure.
- [MEDIUM] `V2-Dash/storage/screenshots/` — customer-data — current_tree=True history=False — 7 PNG screenshots of internal corporate dashboards tracked in git (sistema-patio, painel-multas, inventario-ti, etc.). Exposes internal system layouts.
- [LOW] `V2-Dash/backend/app/**/__pycache__/` — binary-artifact — current_tree=True history=False — 11 .pyc compiled Python files tracked in git.
- [LOW] `V1-Dash/monitor_dashboard.log` — other — current_tree=True history=False — Log file tracked in git; may contain runtime information.

### desafio-focon (PUBLIC)
- [LOW] `scripts/provision-remote-demo.mjs` — jwt — current_tree=True history=True — Hardcoded Supabase demo anon key (well-known public sb-supabase-demo JWT, iss=supabase-demo, exp=2033). Used as fallback default for local/demo provisioning. Not a real credential.
- [LOW] `playwright.config.ts` — jwt — current_tree=True history=True — Same Supabase demo anon key hardcoded in E2E test config for local Supabase instance. Public demo key, not a real secret.

### nao-conformidade (PRIVATE)
- [LOW] `projeto_glaucio/settings.py` — generic-token — current_tree=True history=False — Django SECRET_KEY has insecure default 'django-insecure-change-me-in-production' used when env var not set. DEBUG=True by default. ALLOWED_HOSTS includes '*' in debug mode.
- [LOW] `README.md` — other — current_tree=True history=False — README documents default user credentials in plaintext (admin/admin123, qualidade/123456, operador1/123456, supervisor/123456).

### sanduicherie (PUBLIC)
- [LOW] `.github/workflows/ci.yml` — jwt — current_tree=True history=False — Test JWT secret placeholder 'ci-test-secret-key-min-32-chars-long' and 'ci-e2e-test-secret-key-min-32-chars-long' used in CI env config. Not a real secret - clearly labeled test values.
- [LOW] `frontend/e2e/global-setup.ts` — jwt — current_tree=True history=False — Test JWT secret placeholder 'e2e-test-secret-key-min-32-chars-long' used in Playwright E2E setup. Not a real secret.
- [LOW] `frontend/playwright.config.ts` — jwt — current_tree=True history=False — Test JWT secret placeholder 'e2e-test-secret-key-min-32-chars-long' used in Playwright config. Not a real secret.

### wrconsultoriaesolucoes (PUBLIC)
- [LOW] `FOOTER_PYSCRIPT_MIGRATION.md` — generic-token — current_tree=True history=True — Documentation contains placeholder 'YOUR_JWT_TOKEN' in curl examples (gitleaks curl-auth-header rule). Not a real credential.
- [LOW] `public_html/wp-content/plugins/* (elementor, google-site-kit, jet-elements, official-facebook-pixel, wordpress-seo, image-optimization)` — other — current_tree=True history=True — 25 gitleaks findings are all inside third-party WordPress plugin vendor code (phpseclib key format strings, Flickr demo key in juxtapose.js, Elementor dashboard widget token, Facebook Pixel test JWTs, Yoast OIDC issuer config). These are upstream public plugin artifacts, not WR Consultoria secrets.

---
## Versioned Artifacts (Build Dependencies, Binaries, Databases)

These should be removed from version control and added to `.gitignore`.

| Repository | node_modules | venv | build/dist | binaries | sql_dumps | zip_backups | media_large | Details |
|---|---|---|---|---|---|---|---|---|
| AndaimesPini_Project | No | No | No | No | Yes | No | No | Versioned database/db.sqlite3 (40KB) and 18 *.sqlite_backup files in backend/ and backend/models/ and backend/routes/. No node_modules (gitignored). |
| Bot_IqOption | No | Yes | No | No | Yes | No | No | venv directory committed (13,661 tracked files), db.sqlite3 database committed, __pycache__ directories committed, large log file (117k+ lines) with 197 JWT tokens, 3 user key files, .env and RAILWAY_ENV_COMPLETE.txt with production credentials |
| Digital-Signage-Platform | No | No | No | No | No | No | Yes | No node_modules/venv. backend/scripts/seed_companies.py provides seed/demo data. deploy/ contains nginx + systemd configs. Large media is referenced via uploads but no committed media dumps found. |
| FinanceControl | No | No | No | Yes | Yes | No | No | Versioned backend/db.sqlite3 (364KB SQLite DB) and a payment-receipt PDF. .env.production contains only CHANGE_ME placeholders (template, not real secrets). .pem key is a versioned binary artifact. |
| Legal-AI-Copilot | No | Yes | Yes | Yes | No | No | Yes | CRITICAL: backend/venv/ committed (11836 files including 5324 .pyc). 35 PDFs committed including the hiring case PDF, sample contracts (contrato.pdf, Contrato_Prestacao_Servicos_*.pdf, test_contract.pdf) and ~28 uploaded test contracts in backend/uploads/. venv and uploads should be gitignored. |
| LogiFlow | No | No | No | No | No | Yes | No | render.yaml.bak (4.5KB backup deploy config) committed. Multiple .env.production files with API URLs committed. No node_modules or venv. CSV templates in templates/ directory. No large media files. |
| MVP-linkedin-bot | No | Yes | No | Yes | No | No | Yes | Two venv directories committed (26,655 tracked files), 5 PDF files (CV/resumes/CPF), Chrome profile data (36,969 tracked files), __pycache__ directories, large log file (53k+ lines) |
| Plataforma-de-Monitoramento-de-Sistemas-e-APIs | Yes | No | No | No | No | No | No | node_modules/ is versioned (100 tracked files incl. cookie, react-dom packages). No .gitignore excludes it. Should be removed and gitignored. |
| Portfolio-LeonardoFragoso-React | No | No | No | No | No | No | Yes | 3 PDF files in public/ (CNPJ card 260KB, contrato social 1.4MB, CV 898KB). Lighthouse report HTML/JSON in docs/. Project images in public/images/ for 8 projects. package-lock.json (221KB) committed. |
| SaaS | No | No | No | No | Yes | No | No | Versioned db.sqlite3 in the BI-as-a-Service backend. Six numbered product directories, but only product 1 has code; products 2-6 contain only escopo.txt scope documents. |
| Sistema-de-compras | No | No | No | Yes | Yes | No | No | SQLite database (compras_sla.db), Excel spreadsheet, Word document, audio file (.opus), PDF, and 3 JPG images tracked in git. .gitignore lists compras_sla.db but it is tracked anyway. |
| YardMaster | No | Yes | No | Yes | Yes | No | No | venv/ with 8328 files tracked, 3158 .pyc files, database.db + 3 .bak files in bkp/, app.py.backup file, app.log. Extremely bloated repository. |
| base-corporativa | No | No | Yes | No | No | No | No | frontend/dist/ with 10 built files tracked in git. No node_modules or venv tracked. No binary or SQL dump files. |
| dash-monitor | No | No | No | Yes | No | No | Yes | 7 PNG screenshots of internal dashboards in V2-Dash/storage/screenshots/, 11 .pyc files, 1 log file. No node_modules or venv tracked. |
| pimenta | Yes | No | No | No | No | No | No | node_modules directory (102 packages) committed to git. No .gitignore file exists in the repo. package-lock.json (91KB) committed. No other artifacts. |
| wrconsultoriaesolucoes | No | No | No | Yes | No | Yes | Yes | release/wrsi-v2.6.1-hostinger.zip (391KB release package) committed. Multiple WR business PDFs committed (WR_kit_implementacao.pdf, WR_ordem_servico_site.pdf, WR_guia_ga4_pixel.pdf, WR_analise_site.pdf). public_html/wp-content/uploads/ contains production media incl. complianz consent-proof PDFs. Full WordPress core + plugins + themes versioned (28305 files). No node_modules/venv. |

---
## IP / Provenance Risks

Repositories where public redistribution may violate client/employer/third-party IP rights:

### AndaimesPini_Project (PUBLIC) — Category D
- **Branding evidence:** frontend/src/components/pages/LandingPage.js: 'Andaimes Pini' (title and footer '© {year} Andaimes Pini. Todos os direitos reservados.'); frontend/src/components/layouts/Navbar.js: 'Andaimes Pini'; frontend/.env.production: REACT_APP_API_URL=https://andaimespiniproject-production.up.railway.app; DEPLOY_GUIDE.md: 'Guia de Deploy - AndaimesPini Project' (Frontend: Vercel, Backend: Railway); backend/create_admin_railway.py and railway.json + nixpacks.toml + Procfile for Railway deployment
- **Ownership concerns:** Clearly a client project for 'Andaimes Pini' (a scaffolding rental company — 'andaimes' = scaffolding in PT-BR). System is a rental management system deployed live to Railway (andaimespiniproject-production.up.railway.app) and Vercel. Public redistribution of client-specific business code and data is risky.
- **Currently public:** True
- **Recommendation:** Make private pending review

### Bet-IA-BOT (PRIVATE) — Category A
- **Branding evidence:** Personal betting analysis system using public APIs (API-Football, The Odds API); No third-party branding or client references
- **Ownership concerns:** Personal project with no third-party IP concerns, but contains a hardcoded API key that should be rotated
- **Currently public:** False
- **Recommendation:** Make private pending review

### Bot_IqOption (PRIVATE) — Category B
- **Branding evidence:** README explicitly states 'projeto de estudo/experimental para fins educacionais'; Disclaimer: 'Não utilize em contas reais'
- **Ownership concerns:** Despite educational framing, the repo contains production MercadoPago credentials and real user API keys — the payment integration and user management are production-grade, not educational
- **Currently public:** False
- **Recommendation:** Make private pending review

### Digital-Signage-Platform (PUBLIC) — Category E
- **Branding evidence:** Initial commit 0d0dba6 titled 'Initial commit - TVS Digital Signage Platform'; package.json name is 'tvs-digital-signage'; docs/PLTI-012a_Documento_de_Escopo_As_is_To_be.md identifies the system as 'TVS iTracker' serving 'iTracker, Rio Brasil Terminal (RBT), CLIA'; docs/PLTI-012b/c/d are corporate governance documents (Arquitetura, As Built, Plano de Manutencao) authored by Leonardo Fragoso dated 05/12/2024; History references database 'tvs_itracker'; LEGAL_COMPLIANCE_REPORT.md (commit f73b8fe) self-describes a 'white label preparation' that 'Removed real credentials containing proprietary information'; proxy-server.py, final_rbac_fix.py, backend/routes/settings.py, backend/migrations/add_system_configs.py still reference tvs/iTracker
- **Ownership concerns:** This is a corporate system built for iTracker / Rio Brasil Terminal / CLIA. Despite a self-authored 'LEGAL_COMPLIANCE_REPORT' claiming it is cleared for white-label commercialization, residual corporate identifiers (PLTI project docs, TVS iTracker naming, tvs_itracker DB references) and real database credentials remain in git history. Public redistribution carries clear employer/client IP risk.
- **Currently public:** True
- **Recommendation:** Make private pending review

### FlowTrack (PUBLIC) — Category D
- **Branding evidence:** README states the system is 'em producao no maior terminal portuario privado do Brasil (operacao ICTSI no Porto do Rio de Janeiro)'; Initial commit 83a021b titled 'Commit inicial - Sistema Atendimento GR completo com tema escuro e visualizacao em tempo real' (GR = corporate operations system); Docs/LEGAL_REVIEW_SUMMARY.md references removal of brand references 'ICTSI, iTracker, CLIA' - confirming corporate/client provenance; Docs/BRANDING.md and Docs/LOGO_SETUP.md describe white-label rebranding workflow
- **Ownership concerns:** This is a production operations-management system deployed at an ICTSI port terminal. Although a 'White Label transformation' (commit 377713b) attempted to strip brand references and an accompanying LEGAL_REVIEW_SUMMARY claims 'Zero Legal Blockers' and 'No data exposure', the README still explicitly names ICTSI and the initial commit exposes the GR corporate system origin. The committed nohup.out log in history contradicts the 'No data exposure' claim. Public redistribution carries client IP and operational-data risk.
- **Currently public:** True
- **Recommendation:** Make private pending review

### Legal-AI-Copilot (PUBLIC) — Category C
- **Branding evidence:** Committed PDF 'Case Técnico – AI & Legal Operations Specialist.pdf' opens with 'Parabéns por avançar para esta etapa do processo seletivo' (congratulations for advancing to this stage of the selection process); INTERVIEW_QUICK_REFERENCE.md, VIDEO_PRESENTATION_SCRIPT.md, DEMO_SCRIPT*.md, RECORDING_CHECKLIST.md — all hiring-deliverable artifacts; Case requires PDF document (max 5 pages) + demo video (5-10 min) as delivery format; deliverables/ directory with Legal_AI_Copilot_Case.pdf
- **Ownership concerns:** The hiring case PDF and deliverables are from a prospective employer's selection process. Committing these publicly redistributes third-party hiring materials. The committed venv and contract PDFs add noise but the case materials are the IP concern.
- **Currently public:** True
- **Recommendation:** Make private pending review

### LogiFlow (PUBLIC) — Category A
- **Branding evidence:** LogiFlow CRM branding throughout — README, docs, docker configs, helm charts; MIT license (Copyright 2026 Leonardo Fragoso); Live deployment referenced: logi-flow-wuhp.vercel.app; Email: vendas@logiflow.com.br, noreply@logiflow.com.br; References multiple third-party integrations: Focus NFe, Evolution API, Mercado Pago, Google Maps, Sascar, Autotrac, OnixSat, SuiteCRM, Omie, Bling, Tiny, Melhor Envio, Frenet, SendGrid
- **Ownership concerns:** Personal SaaS product with MIT license. Third-party API integrations are documented but no proprietary third-party code is included. The extensive documentation (70+ docs files) contains integration guides with example credentials that should be sanitized. Safe for public distribution after credential cleanup.
- **Currently public:** True
- **Recommendation:** Make private pending review

### MVP-linkedin-bot (PRIVATE) — Category A
- **Branding evidence:** Personal CV/CPF/resume PDFs in repo root; LinkedIn job application data with real company names and phone numbers
- **Ownership concerns:** Contains Leonardo Fragoso's personal identification documents (CPF, CVs) and Chrome browser session data — extremely risky if made public
- **Currently public:** False
- **Recommendation:** Make private pending review

### Plataforma-Cursos-WRConsultoria (PUBLIC) — Category D
- **Branding evidence:** README: 'Plataforma web de gestao e comercializacao de cursos (LMS + backoffice administrativo) para a WR Consultoria e Solucoes em QSMS'; Seed data and tests reference WR/wrcursos.com.br branding (api/app/seeds/courses_seed.py, classes_seed.py, students_seed.py; tests/conftest.py); web/src/views/ValidateCertificate.vue and alembic migrations reference WR/wrcursos domain; MULTI_TENANT_ARCHITECTURE.md and PROJECT_SUMMARY.md describe a white-label SaaS for WR Consultoria
- **Ownership concerns:** Built for WR Consultoria e Solucoes em QSMS as a white-label multi-tenant LMS/SaaS. While no third-party commercial plugins are present (unlike the WordPress repo), the domain logic, course catalog seeds, and branding are client-specific. Public redistribution is moderately risky because it exposes a client's business model and seed data, though the code itself is largely original.
- **Currently public:** True
- **Recommendation:** Make private pending review

### ProFlow (PUBLIC) — Category A
- **Branding evidence:** Personal product: 'ProFlow — The Operating System for Professional Freelancers' (Brazilian freelancer platform); Proprietary license (LICENSE file). No third-party client/employer branding; integrates Mercado Pago, OpenAI, Asaas, Telegram
- **Ownership concerns:** No third-party IP concerns. Personal product. Critical concern is real production credentials leaked in git history (RAILWAY_ENV_FINAL.txt, DEPLOY_CHECKLIST.md).
- **Currently public:** True
- **Recommendation:** Make private pending review

### SaaS (PRIVATE) — Category A
- **Branding evidence:** README.md: 'Ecossistema SaaS - Plataformas de Serviços com IA'; MIT License (LICENSE file); README.md: 'BI-as-a-Service Ativo v1.1.0'
- **Ownership concerns:** Personal SaaS ecosystem project under MIT license. No third-party IP. Private repo; safe to keep or selectively publish.
- **Currently public:** False
- **Recommendation:** Make private pending review

### Sistema-de-compras (PUBLIC) — Category D
- **Branding evidence:** README.md: 'Sistema de Gestão de Compras - Ziran v2.0' - Ziran is a specific company brand; assets/img/logo_ziran.jpg and ziran fundo.jpg - company branding; Fluxo utilizado hoje pela empresa.docx - internal company process documentation; Compras_SLA .xlsx - corporate purchasing SLA data; README describes corporate purchasing workflow with 7-step approval process
- **Ownership concerns:** Client/company-specific purchasing system for 'Ziran'. Contains internal business process documents, corporate SLA data, and company branding. Public redistribution exposes client internal processes and data.
- **Currently public:** True
- **Recommendation:** Make private pending review

### YardMaster (PUBLIC) — Category E
- **Branding evidence:** WHITE_LABEL_TRANSFORMATION.md documents renaming itracker_logo.png to logo.png and CSS variables --itracker-* to --brand-*; LEGAL_REVIEW_REPORT.md confirms original project had ICTSI/iTracker/CLIA references; utils/sharepoint_client.py: SharePoint URL replaced with generic placeholder (was corporate); Operational data files: armadores_brasil.txt (shipping companies), posicao_floriano.txt, posicao_suzano.txt (yard positions for specific Brazilian ports); Database schema has 'unidade TEXT DEFAULT Rio de Janeiro' hardcoded
- **Ownership concerns:** Originally an iTracker/ICTSI corporate yard management system. While branding was superficially rebranded to 'white label', the codebase contains operational data (yard positions, shipping company lists), a tracked SQLite database, and hardcoded defaults referencing specific corporate locations. Public redistribution is risky.
- **Currently public:** True
- **Recommendation:** Make private pending review

### alzi-project (PRIVATE) — Category A
- **Branding evidence:** README.md: 'Alzi Project — Processador de Planilha de Contêineres'; README.md: 'Ferramenta desenvolvida para automatizar o processamento de planilhas de rastreamento de contêineres portuários'
- **Ownership concerns:** Utility tool with no obvious third-party branding, but the committed TC.xls/TC.xlsx spreadsheets may contain real port operational/container tracking data from an actual operation or client. Repo is private, mitigating exposure.
- **Currently public:** False
- **Recommendation:** Make private pending review

### aviator-banca (PRIVATE) — Category A
- **Branding evidence:** Personal bankroll tracking app for Aviator game; No third-party branding or client references
- **Ownership concerns:** Personal project with no third-party IP concerns. No secrets or sensitive data committed.
- **Currently public:** False
- **Recommendation:** Make private pending review

### base-corporativa (PUBLIC) — Category A
- **Branding evidence:** README.md: 'Base Corporativa' brand with live demo at basecorporativa.store; E-commerce for corporate uniforms/workwear - appears to be own business venture; Railway deployment configuration (nixpacks.toml, railway.toml, Procfile); MercadoPago and MelhorEnvio integrations for Brazilian e-commerce
- **Ownership concerns:** Appears to be a personal e-commerce business. No third-party employer branding detected. However, tracked production credentials (AWS, MercadoPago, SendGrid, database) pose a severe security risk if the repo is public. The business data and customer info in the database URL are sensitive.
- **Currently public:** True
- **Recommendation:** Make private pending review

### dash-monitor (PUBLIC) — Category E
- **Branding evidence:** README.md: 'utilizado internamente na iTracker (ICTSI, Porto do Rio de Janeiro)'; V1-Dash/dashboard_monitor.py: hardcoded iTracker logo references, 'itracker_logo.png', 'Desenvolvido pelo setor de Qualidade - iTracker'; V2-Dash/frontend/src/App.tsx: brandLogo itracker_logo.png, brandName 'iTracker'; V2-Dash/backend/app/domain/services_config.py: service id 'ictsi-tvs', name 'ICTSI TVs'; Internal IP 192.168.0.45 with corporate service ports
- **Ownership concerns:** Clearly an internal iTracker/ICTSI corporate tool. Public redistribution exposes internal infrastructure details, IP addresses, and dashboard screenshots of proprietary systems.
- **Currently public:** True
- **Recommendation:** Make private pending review

### devpro-e2e-sandbox (PRIVATE) — Category F
- **Branding evidence:** README.md: 'A minimal Python project (calculator) used for DevPro end-to-end orchestration testing'; devpro.yml: DevPro project config with executor (primary: devin, fallback: openai_local), reviewer (openai/gpt-4o-mini), and policies (create_repository: false, create_pull_request: true, merge: false, deploy: false); Open PRs authored by 'devin-ai-integration[bot]' and 'LeonardoRFragoso' via DevPro orchestration branches (devpro/<sha>-<task>)
- **Ownership concerns:** Internal supporting infrastructure for the DevPro orchestrator's E2E test pipeline. No third-party IP. Private repo; should remain private as it is test scaffolding, not a portfolio piece.
- **Currently public:** False
- **Recommendation:** Make private pending review

### exnova-api (PRIVATE) — Category A
- **Branding evidence:** Personal trading bot for Exnova platform; No third-party branding or client references
- **Ownership concerns:** Personal project with no third-party IP concerns. Uses environment variables for all credentials — no secrets committed.
- **Currently public:** False
- **Recommendation:** Make private pending review

### nao-conformidade (PRIVATE) — Category E
- **Branding evidence:** README.md: system based on corporate quality form 'planilha ITK-RG-PR-QUA-03-A-13'; create_admin_user.py: hardcoded iTracker emails (leonardo.fragoso@itracker.com.br, glaucio.xavier@itracker.com.br); diagnose_auth_system.py: same iTracker emails; templates/accounts/: multiple templates with 'iTracker' in page titles and itracker_logo.png references; static/img/itracker_logo.png tracked in git
- **Ownership concerns:** Corporate quality management system for iTracker. Contains iTracker branding, employee emails, and references to corporate quality process documents (ITK-RG-PR-QUA-03-A-13). Public redistribution exposes internal corporate processes and personnel.
- **Currently public:** False
- **Recommendation:** Make private pending review

### pimenta (PUBLIC) — Category A
- **Branding evidence:** Melt Pimenta brand — landing page for an adult-content visual/conceptual project; README: 'Projeto visual/conceitual. Conteúdo destinado a maiores de 18 anos.'; No company or client branding — appears to be a personal/brand project; Uses Unsplash CDN images (no local media assets)
- **Ownership concerns:** Personal/brand landing page with no third-party IP concerns. Content is adult-oriented but not illegal. No proprietary code or client data. Safe for public distribution from an IP standpoint, though the committed node_modules and lack of .gitignore are hygiene issues.
- **Currently public:** True
- **Recommendation:** Make private pending review

### wrconsultoriaesolucoes (PUBLIC) — Category D
- **Branding evidence:** Repository is the full production WordPress site for 'WR Consultoria e Solucoes em QSMS'; Custom mu-plugin 'wr-site-improvements' (delivery/upload-to-public_html/wp-content/mu-plugins/wrsi) with WR-branded blog cover images; Committed business PDFs: WR_ordem_servico_site.pdf (service order), WR_kit_implementacao.pdf, WR_guia_ga4_pixel.pdf, WR_analise_site.pdf; audit/conversion-2026-08/evidence/pdf/ contains WR-branded audit artifacts; Commercial premium plugins committed: elementor-pro, wordpress-seo-premium (licensed paid plugins not redistributable); public_html/wp-content/uploads/complianz/snapshots/WR-Consultoria-e-Solucoes-br-proof-of-consent-*.pdf (client consent records)
- **Ownership concerns:** Public redistribution is unsafe on multiple fronts: (1) commercial premium WordPress plugins (Elementor Pro, Yoast SEO Premium) are licensed paid software that must not be publicly redistributed; (2) WR Consultoria business documents (service orders, implementation kits, GA4/pixel guides) and production consent records are client/company proprietary; (3) the full production WordPress deployment (core + uploads) exposes the live site's structure and content.
- **Currently public:** True
- **Recommendation:** Make private pending review

### Third-Party Commercial Plugins / Licensed Software

- **wrconsultoriaesolucoes:** Contains commercial premium WordPress plugins (Elementor Pro, Yoast SEO Premium) — licensed paid software not redistributable under any open-source license. Must not remain public.

### Self-Authored 'Legal Compliance' Reports — Flagged for Human Review

Two repositories contain self-authored legal compliance reports that claim they are cleared for commercialization, but git history contradicts these claims:

- **Digital-Signage-Platform:** `LEGAL_COMPLIANCE_REPORT.md` claims 'CLEARED FOR COMMERCIALIZATION' / 'Sanitized Sensitive Data', but commit `17f5403` added real DB credentials to `secrets/db_credentials.txt`. Later sanitization at `f73b8fe` does NOT purge history. The `tvs_itracker` DB name ties code to iTracker corporate environment. **Category E (former employer/corporate).**
- **FlowTrack:** `LEGAL_REVIEW_SUMMARY` claims brand references were removed, but README still names ICTSI. `nohup.out` with 179 session/CSRF token findings remains in git history. **Category D (client project).**

Both require human legal review before any public showcase.

---
## Remediation Priority Summary

### Phase 2A — Urgent (Immediate Action Required)

| Priority | Repository | Issue | Action |
|---|---|---|---|
| CRITICAL | ProFlow | Real production credentials in git history (RAILWAY_ENV_FINAL.txt, DEPLOY_CHECKLIST.md): OpenAI API key, Google/GitHub OAuth secrets, Mercado Pago token, Django secret | Rotate all exposed credentials. Make repo private. Scrub git history with BFG or git-filter-repo. |
| CRITICAL | base-corporativa | 14 gitleaks findings: AWS/Cloudflare R2 keys, MercadoPago tokens, MelhorEnvio tokens, SendGrid API key, database URL, Django superuser password in tracked files (RAILWAY_ENV_ATUALIZADO.txt, backend/.env.railway, 4 Python scripts) | Rotate all credentials. Remove tracked secret files. Scrub git history. Update .gitignore to cover .env.railway. |
| CRITICAL | Bot_IqOption | 201 gitleaks findings: Production MercadoPago credentials in .env and RAILWAY_ENV_COMPLETE.txt, 197 JWT trading session tokens in bot_iqoption.log, 3 user API key files in keys/, SQLite database committed. venv (13,661 files) tracked. | Rotate MercadoPago credentials. Remove log/keys/venv. Scrub history. This repo is PRIVATE but credentials are still compromised. |
| CRITICAL | MVP-linkedin-bot | 9 gitleaks findings: Chrome browser profile with session tokens committed, CPF (national ID) PDF, personal CV/resume PDFs, perguntas.csv with phone numbers. venv (26,655 files) and Chrome profile (36,969 files) tracked. | Rotate LinkedIn session. Remove Chrome profile, personal docs, venv. Scrub history. Repo is PRIVATE but personal data is exposed in git. |
| CRITICAL | FinanceControl | RSA private key (chave-EC2/Finance2.pem) in current tree AND history. Versioned db.sqlite3 and payment-receipt PDF. Prior commit 'fix: remove exposed credentials' missed the .pem. | Revoke/rotate EC2 key pair. Remove .pem, db.sqlite3, PDFs. Scrub history. Repo is PUBLIC — key is compromised. |
| CRITICAL | Digital-Signage-Platform | Real DB credentials committed at 17f5403 (secrets/db_credentials.txt), later sanitized but values remain in history. .env.tv with weak JWT_SECRET_KEY in current tree. Tied to iTracker corporate environment. | Rotate DB credentials. Remove .env.tv. Scrub history. Make repo private (former employer IP). Repo is PUBLIC — credentials are compromised. |

### Phase 2A — High Priority

| Priority | Repository | Issue | Action |
|---|---|---|---|
| HIGH | PayFlow-AI | Security findings in history — review and rotate if real | Audit gitleaks findings, rotate any real credentials, scrub history |
| HIGH | Portfolio-LeonardoFragoso-React | 3 sensitive PDFs committed in public/ (CNPJ card, contrato social, CV) | Remove personal/business PDFs from public repo, scrub history |
| HIGH | FlowTrack | 179 session/CSRF token findings in nohup.out (history-only), weak fallback SECRET_KEY, README still names ICTSI | Remove nohup.out from history, rotate SECRET_KEY, make repo private (client project) |
| HIGH | Bet-IA-BOT | Hardcoded API-Football API key in backend/test_new_api.py | Rotate API-Football key, remove from code, use env vars |
| HIGH | YardMaster | 8328 venv files + 3158 .pyc files tracked in git, tracked SQLite database with operational data, iTracker branding | Remove venv/.pyc/SQLite from git, make repo private (former employer IP) |
| HIGH | Digital-Signage-Platform | (also listed CRITICAL above — .env.tv weak JWT secret in current tree) | Remove .env.tv, use env vars |
