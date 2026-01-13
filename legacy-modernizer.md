# legacy_modernizer.md - Moderniza código jurássico

OBJECTIVE: Migrar código legacy para padrões modernos

PHASE 1 - Archaeology:
GLOB **/*.{js,py,java}
GREP “var |==|!=|function\(” --legacy-patterns

    IDENTIFY:
        - Padrões obsoletos
        - Anti-patterns
        - Código duplicado
        - Dead code

PHASE 2 - Migration planning:
CREATE MIGRATION_PLAN.md:
# 📋 Plano de Migração

        ## Prioridade 1 (Fácil & Alto impacto)
        - [ ] Converter var → const/let
        - [ ] Converter == → ===
        - [ ] Converter callbacks → async/await

        ## Prioridade 2 (Médio esforço)
        - [ ] Extrair funções grandes
        - [ ] Adicionar types/interfaces
        - [ ] Modernizar imports

        ## Prioridade 3 (Requer refatoração)
        - [ ] Quebrar god objects
        - [ ] Implementar patterns
        - [ ] Adicionar testes

PHASE 3 - Auto-migration:
FOR EACH pattern simples:
UPDATE arquivos com versão moderna

    CREATE migration_report.json:
        {
            “files_updated”: [],
            “patterns_fixed”: [],
            “manual_review_needed”: [],
            “estimated_time_saved”: “hours”
        }

PHASE 4 - Testing:
RUN:
npm test || pytest || mvn test

    VERIFY:
        Todos os testes passam após migração

REPORT:
Migração automática completa!
Arquivos modernizados: X
Tempo economizado: Y horas
Dívida técnica reduzida: Z%
