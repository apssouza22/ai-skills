# auto_reviewer.md - Substitui 3 seniors em code review

OBJECTIVE: Review completo de PR com sugestões

PHASE 1 - Análise de mudanças:
RUN:
git diff main...HEAD --name-only
git diff main...HEAD --stat

    IDENTIFY:
        - Arquivos modificados
        - Linhas adicionadas/removidas
        - Impacto no sistema

PHASE 2 - Quality checks:
FOR EACH arquivo modificado:
ANALYZE:
- Code smells
- Violações de SOLID
- Complexidade ciclomática
- Duplicação de código
- Falta de testes
- Security issues

PHASE 3 - Gerar feedback:
CREATE PR_REVIEW.md:
# 🔍 Code Review Automático

        ## Summary
        ✅ **Aprovado** | ⚠️ **Precisa ajustes** | ❌ **Bloqueado**

        ## Positivos
        - [O que está bom]

        ## Issues Encontradas

        ### 🔴 Críticas (bloqueia merge)
        - [Issues que precisam ser resolvidas]

        ### 🟡 Importantes (considere mudar)
        - [Melhorias recomendadas]

        ### 🔵 Sugestões (nice to have)
        - [Optimizações opcionais]

        ## Code Quality Metrics
        - Complexidade: X/10
        - Manutenibilidade: X/10
        - Testabilidade: X/10
        - Performance: X/10

        ## Suggested Changes
        ```diff
        [Código com sugestões de mudança]
        ``` {data-source-line=”1575”}

PHASE 4 - Auto-fix simples:
FOR EACH issue simples:
CREATE {file}_suggested.py com correções

    RUN:
        git add -A
        git commit -m “🤖 auto-fix: Correções sugeridas pelo reviewer automático”

REPORT:
Review completo!
Tempo economizado: 45 minutos
Custo economizado: $112.50
