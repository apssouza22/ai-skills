# security_scanner.md - Auditoria de segurança completa

OBJECTIVE: Identificar vulnerabilidades antes que virem problema

PHASE 1 - Secret scanning:
GREP “password|api[_-]key|secret|token|private[_-]key” --all-files
GREP “[A-Za-z0-9+/]{40,}” --potential-secrets

    IDENTIFY:
        - Hardcoded credentials
        - API keys expostas
        - Tokens em código

PHASE 2 - Dependency audit:
RUN:
npm audit || pip-audit || bundler-audit

    ANALYZE:
        - CVEs conhecidas
        - Dependências desatualizadas
        - Packages abandonados

PHASE 3 - Code vulnerabilities:
GREP “eval\(|exec\(|system\(|`;|SQL|SELECT.*FROM” --injection-risks
GREP “http://|disable.*ssl|verify.*false” --insecure-connections

    IDENTIFY:
        - SQL injection risks
        - XSS vulnerabilities
        - Command injection
        - Insecure connections

PHASE 4 - Generate report:
CREATE SECURITY_AUDIT.md:
# 🔒 Security Audit Report

        ## Risk Level: [LOW|MEDIUM|HIGH|CRITICAL]

        ## 🔴 Critical Issues (Fix NOW)
        [Lista de vulnerabilidades críticas]

        ## 🟡 High Priority
        [Issues importantes]

        ## 🔵 Medium Priority
        [Melhorias de segurança]

        ## Remediation Steps
        1. [Passo a passo para corrigir]

        ## Compliance Check
        - [ ] OWASP Top 10
        - [ ] PCI DSS (se aplicável)
        - [ ] GDPR (se aplicável)

PHASE 5 - Auto-fix:
CREATE .env.example com variáveis necessárias
UPDATE código removendo secrets hardcoded
CREATE security-fixes branch com correções

REPORT:
Auditoria completa!
Issues encontradas: X
Auto-corrigidas: Y
Requerem atenção manual: Z
