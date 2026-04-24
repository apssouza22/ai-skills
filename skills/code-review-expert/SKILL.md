---
name: code-review-expert
description: "Expert code review of current git changes with a senior engineer lens. Detects SOLID violations, security risks, and proposes actionable improvements."
---

# Code Review Expert

## Overview

Perform a structured review with focus on SOLID, architecture, removal candidates, and security risks. Default to review-only output unless the user asks to implement changes.

**Supported inputs:**
- **Local changes**: Reviews current `git diff` (default behavior).
- **GitHub PR URL**: When the user provides a GitHub PR URL (e.g., `https://github.com/owner/repo/pull/123`), fetch the PR diff using `gh` CLI and review it.

## Severity Levels

| Level | Name | Description | Action |
|-------|------|-------------|--------|
| **P0** | Critical | Security vulnerability, data loss risk, correctness bug | Must block merge |
| **P1** | High | Logic error, significant SOLID violation, performance regression | Should fix before merge |
| **P2** | Medium | Code smell, maintainability concern, minor SOLID violation | Fix in this PR or create follow-up |
| **P3** | Low | Style, naming, minor suggestion | Optional improvement |

## Workflow

### 1) Preflight context

Detect the input source and gather context accordingly.

#### a) GitHub PR URL provided

When the user provides a GitHub PR URL or `owner/repo#number`:

1. Extract PR metadata:
   ```bash
   gh pr view <URL> --json title,body,number,state,baseRefName,headRefName,additions,deletions,changedFiles,reviews,labels
   ```
2. Get the full diff:
   ```bash
   gh pr diff <URL>
   ```
3. List changed files:
   ```bash
   gh pr diff <URL> --stat
   ```
4. Check CI status (optional context):
   ```bash
   gh pr checks <URL>
   ```

Use the PR description and linked issues for additional context about intent.

#### b) Local git changes (default)

- Use `git status -sb`, `git diff --stat`, and `git diff` to scope changes.
- If needed, use `rg` or `grep` to find related modules, usages, and contracts.

#### Common for both sources

- Identify entry points, ownership boundaries, and critical paths (auth, payments, data writes, network).

**Edge cases:**
- **No changes**: If `git diff` is empty, inform user and ask if they want to review staged changes or a specific commit range.
- **Large diff (>500 lines)**: Summarize by file first, then review in batches by module/feature area.
- **Mixed concerns**: Group findings by logical feature, not just file order.

### 2) SOLID + architecture smells

- Load `references/solid-checklist.md` for specific prompts.
- Look for:
  - **SRP**: Overloaded modules with unrelated responsibilities.
  - **OCP**: Frequent edits to add behavior instead of extension points.
  - **LSP**: Subclasses that break expectations or require type checks.
  - **ISP**: Wide interfaces with unused methods.
  - **DIP**: High-level logic tied to low-level implementations.
- When you propose a refactor, explain *why* it improves cohesion/coupling and outline a minimal, safe split.
- If refactor is non-trivial, propose an incremental plan instead of a large rewrite.

### 3) Removal candidates + iteration plan

- Load `references/removal-plan.md` for template.
- Identify code that is unused, redundant, or feature-flagged off.
- Distinguish **safe delete now** vs **defer with plan**.
- Provide a follow-up plan with concrete steps and checkpoints (tests/metrics).

### 4) Security and reliability scan

- Load `references/security-checklist.md` for coverage.
- Check for:
  - XSS, injection (SQL/NoSQL/command), SSRF, path traversal
  - AuthZ/AuthN gaps, missing tenancy checks
  - Secret leakage or API keys in logs/env/files
  - Rate limits, unbounded loops, CPU/memory hotspots
  - Unsafe deserialization, weak crypto, insecure defaults
  - **Race conditions**: concurrent access, check-then-act, TOCTOU, missing locks
- Call out both **exploitability** and **impact**.

### 5) Code structure review

- Load `references/code-structure.md` for guidelines.
- Verify code follows **domain-based package organization**, not layer-based.
- Check for:
  - **No layer-based packages**: `controller/`, `service/`, `repository/`, `entity/` packages should not exist.
  - **Domain packages**: Code is organized by business domain (e.g., `partner/`, `organization/`).
  - **Complete domains**: Each domain package contains all related components (entity, repository, service, controller, DTOs).
  - **Proper common/ usage**: Only cross-cutting concerns (global exception handling, security config, shared utilities) are in `common/`.
  - **No domain-specific code in common/**: DTOs, exceptions, validators, and mappers belong in their domain package.
- Layer-based organization is a **P1** finding; domain-specific code in `common/` is **P2**.

### 6) Code quality scan

- Load `references/code-quality-checklist.md` for coverage.
- Check for:
  - **Error handling**: swallowed exceptions, overly broad catch, missing error handling, async errors
  - **Performance**: N+1 queries, CPU-intensive ops in hot paths, missing cache, unbounded memory
  - **Boundary conditions**: null/undefined handling, empty collections, numeric boundaries, off-by-one
- Flag issues that may cause silent failures or production incidents.

### 7) Output format

Structure your review as follows:

```markdown
## Code Review Summary

**Files reviewed**: X files, Y lines changed
**Overall assessment**: [APPROVE / REQUEST_CHANGES / COMMENT]

---

## Findings

### P0 - Critical
(none or list)

### P1 - High
- **[file:line]** Brief title
  - Description of issue
  - Suggested fix

### P2 - Medium
...

### P3 - Low
...

---

## Removal/Iteration Plan
(if applicable)

## Additional Suggestions
(optional improvements, not blocking)
```

**Inline comments**: Use this format for file-specific findings:
```
::code-comment{file="path/to/file.ts" line="42" severity="P1"}
Description of the issue and suggested fix.
::
```

**Clean review**: If no issues found, explicitly state:
- What was checked
- Any areas not covered (e.g., "Did not verify database migrations")
- Residual risks or recommended follow-up tests

### 8) Next steps confirmation

After presenting findings, ask user how to proceed.

**Important**: Do NOT implement any changes until user explicitly confirms. This is a review-first workflow.

#### For local changes:

```markdown
---

## Next Steps

I found X issues (P0: _, P1: _, P2: _, P3: _).

**How would you like to proceed?**

1. **Fix all** - I'll implement all suggested fixes
2. **Fix P0/P1 only** - Address critical and high priority issues
3. **Fix specific items** - Tell me which issues to fix
4. **No changes** - Review complete, no implementation needed
```

#### For GitHub PR reviews:

```markdown
---

## Next Steps

I found X issues (P0: _, P1: _, P2: _, P3: _).

**How would you like to proceed?**

1. **Post as PR review** - Submit findings as a GitHub review with inline comments
2. **Post summary comment** - Add a summary comment to the PR
3. **No action** - Review complete, no comments posted
```

When the user chooses to post a review, use `gh` to submit:

```bash
# Submit a review with a body
gh pr review <URL> --comment --body "review summary here"

# Or request changes
gh pr review <URL> --request-changes --body "review summary here"

# Post individual inline comments via the API
gh api repos/{owner}/{repo}/pulls/{number}/comments \
  --field body="comment text" \
  --field path="file/path.java" \
  --field line=42 \
  --field side="RIGHT" \
  --field commit_id="$(gh pr view <URL> --json headRefOid --jq .headRefOid)"
```

## Resources

### references/

| File | Purpose |
|------|---------|
| `solid-checklist.md` | SOLID smell prompts and refactor heuristics |
| `security-checklist.md` | Web/app security and runtime risk checklist |
| `code-quality-checklist.md` | Error handling, performance, boundary conditions |
| `code-structure.md` | Domain-based package organization guidelines and review checklist |
| `removal-plan.md` | Template for deletion candidates and follow-up plan |
