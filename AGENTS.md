## Project Knowledge


## Core Principles

These principles reduce common LLM coding mistakes. Apply them to every task.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

**The test:** Every changed line should trace directly to the user's request.

### Tech Stack

**Backend:**
- Java 21
- Spring Boot
- Gradle 8.x with Kotlin DSL
- JUnit 5 with Testcontainers (PostgreSQL)

**Frontend:**
- React with TypeScript
- Vite for development and builds
- React Router for routing
- Axios for HTTP requests

### Line Length Limits
- **Java:** 120 characters max
- **TypeScript/JavaScript:** 120 chars max

## Package Architecture

### Domain-Based Organization (Required)

Organize code by **business domain**, not by technical layer. Each domain package contains all related components (controllers, services, repositories, entities) together for high cohesion.

**✅ CORRECT - Domain-based organization (Package by Feature):**
- Group all classes by business domain (e.g., `partner/`, `organization/`)
- Each domain package contains: Entity, Repository, Service, Controller, DTOs, Mappers, and domain-specific exceptions
- Use `common/` package ONLY for cross-cutting concerns (exception handlers, security config, shared utilities)

**❌ WRONG - Layer-based organization (Anti-pattern):**
- Do NOT create technical layer packages (`controller/`, `service/`, `repository/`, `entity/`)
- Do NOT mix different business domains in the same package
- Do NOT organize by technical function instead of business capability

### Shared Package Guidelines

The `common/` package is ONLY for truly cross-cutting concerns:

**✅ Belongs in `common/`:**
- Global exception handling (`common/exception/`)
- Security configuration (`common/config/`)
- Common utilities used across all domains (`common/util/`)

**❌ Does NOT belong in `common/`:**
- Domain-specific DTOs (place in domain package instead)
- Domain-specific business logic
- Domain-specific exceptions

## Tools You Can Use

### Backend Commands

| Command | Description |
|---------|-------------|
| `./gradlew build` | Compile, test, and package the application |
| `./gradlew clean build` | Clean build from scratch |
| `./gradlew test` | Run all JUnit tests |
| `./gradlew bootRun` | Start the Spring Boot application (port 8081) |
| `./gradlew check` | Run all verification tasks (tests, checkstyle, version checks) |

### Frontend Commands

Run from `webapp/`:

| Command | Description |
|---------|-------------|
| `npm install` | Install dependencies |
| `npm run dev` | Start Vite dev server (port 5173) |
| `npm run build` | TypeScript compile + production build |
| `npm run lint` | Run ESLint |
| `npm run format` | Auto-format with Prettier |
| `npm run format:check` | Check formatting without changes |


## Standards

Follow these rules for all code you write:

### Java Naming Conventions

- **Packages:** lowercase, dot-separated (`com.mycompany.myproject.partner`)
- **Classes/Interfaces:** PascalCase (`GlobalPartnerPortalApplication`, `PartnerService`)
- **Methods:** camelCase starting with lowercase, minimum 2 chars (`hello`, `getUserData`)
- **Variables:** camelCase, minimum 2 chars (`userName`, `partnerList`)
- **Constants:** UPPER_SNAKE_CASE (`MAX_RETRIES`, `API_BASE_URL`)
- **Type Parameters:** Single uppercase or PascalCase ending in T (`T`, `ResponseT`)

**✅ Good practices:**
- Follow Google Java Style Guide
- Add Javadoc to all public classes and methods
- Use `final` keyword for method parameters
- Use domain-based package organization
- Use explicit imports (no star imports)
- Use descriptive variable and method names (minimum 2 characters)
- Validate input parameters before use
- Use `Optional.orElseThrow()` instead of `Optional.get()`
- Inject dependencies via constructor


### TypeScript/React Naming Conventions

- **Components:** PascalCase (`PartnerList`, `DashboardPage`)
- **Functions/Hooks:** camelCase (`usePartnerData`, `handleSubmit`)
- **Constants:** UPPER_SNAKE_CASE for true constants, camelCase for config objects
- **Types/Interfaces:** PascalCase (`Partner`, `ApiResponse`)
- **Files:** Match export name (`PartnerList.tsx`, `usePartnerData.ts`)

### TypeScript/React Code Style

**✅ Good practices:**
- Use proper TypeScript types (no `any`)
- Define interfaces for component props with `readonly` for immutable props
- Use descriptive variable and function names
- Properly type useState hooks with generic types
- Use named functions inside useEffect for clarity
- Include proper dependency arrays in useEffect
- Use `type` imports for type-only imports
- Handle loading and error states explicitly
- Use proper key props in lists

## Security Guidelines
- Never hardcode secrets in configuration files. All sensitive values must be injected via environment variables or a secrets manager.
- Never expose internal exception messages, stack traces, or system details to API consumers.** This prevents information disclosure that attackers could exploit.
- Always validate and sanitize user input at system boundaries.
- Always use parameterized queries. Never concatenate user input into SQL.
- Never log sensitive data. This includes passwords, tokens, credit card numbers, personally identifiable information (PII), etc.


### Frontend Security (TypeScript/React)
- Use httpOnly cookies for authentication tokens (set by backend)
- Let React handle escaping automatically (avoid `dangerouslySetInnerHTML`)
- Store only public configuration in frontend code
- Use environment variables for API endpoints (`import.meta.env.VITE_*`)
- Validate and sanitize user input before rendering

## Boundaries

### ✅ Always
- Avoid comments describing functionality ensure self describing code
- Organize code by domain package, not by technical layer
- Write to `partner-portal-application/src/` for backend code
- Write to `partner-portal-application/webapp/src/` for frontend code
- Write unit tests in domain packages mirroring main source structure
- Write integration tests in `inttest` package using `@WebIntegrationTest` and extending `TestIntBase`
- Run `npm run format` before committing frontend changes
- Use version catalog (`gradle/libs.versions.toml`) for all dependencies
- Add Javadoc to all public classes and methods
- Use `final` keyword for method parameters in Java
- Use `final var` for local variables in Java when type is obvious from context
- Use TypeScript strict mode with proper typing (no `any`)
- Use Java records for DTOs, value objects, and immutable data classes
- Use environment variables or secrets manager for all sensitive configuration
- Return generic error messages to API clients (no internal details)
- Log exceptions server-side with correlation IDs for debugging
- Use parameterized queries for all database operations
- Validate all user input at controller/API boundaries
- Sanitize data before rendering in frontend
- Add integration tests for new features covering the full stack (API + database)
- Add Integration tests only for services or controllers 

### ⚠️ Ask First

- Database schema changes or migrations
- Adding new dependencies to `build.gradle.kts` or `package.json`
- Modifying CI/CD configuration
- Changes to authentication or security configurations
- API endpoint changes that affect external consumers
- Adding new environment variables for secrets

### 🚫 Never

- Create layer-based packages (`controller/`, `service/`, `repository/`, `entity/`)
- Commit secrets, API keys, or credentials
- Edit generated files in `build/` or `dist/` directories
- Edit `node_modules/` or `gradle/wrapper/`
- Use star imports in Java (`import java.util.*`)
- Use `Optional.get()` without checking presence first
- Skip writing Javadoc for public APIs
- Use `@SuppressWarnings` without justification comment
- Remove or skip failing tests to make builds pass
- Use regular classes for simple DTOs or value objects (use records instead)
- Hardcode secrets, passwords, or API keys in `application.yml` or `application.properties`
- Expose exception messages, stack traces, or internal system details in API responses
- Log sensitive data (passwords, tokens, credit cards, PII)
- Concatenate user input into SQL queries (use parameterized queries)
- Store sensitive tokens in localStorage (use httpOnly cookies)
- Use `dangerouslySetInnerHTML` with unsanitized user input
- Disable CSRF protection without explicit security review
- Return different error messages for authentication failures (prevents user enumeration)
- Add integration tests for repositories or utility classes that don't interact with the database

## Local Development URLs

- **Backend API:** http://localhost:8081
- **Frontend Dev Server:** http://localhost:5173

# Task execution plan
Important: Always plan the task step by step before writing code. Ask for permission to proceed with the plan.
Important: Before proceed with the plan, create a new file named `.agent/plans/name-of-the-task.md`. Based on the approved plan, list all necessary implementation steps as GitHub-style checkboxes (`- [ ] Step Description`). Use sub-bullets for granular details within each main step.

- Plans should be detailed enough to execute without ambiguity
- Each task in the plan must include at least one validation test to verify it works
- Assess complexity and single-pass feasibility - can an agent realistically complete this in one go?
- Include a complexity indicator at the top of each plan:
✅ Simple - Single-pass executable, low risk
⚠️ Medium - May need iteration, some complexity
🔴 Complex - Break into sub-plans before executing

**CRITICAL: After you successfully complete each step, you MUST update the `.agent/plans/name-of-the-task.md` file by changing the corresponding checkbox from `- [ ]` to `- [x]`.**
Only proceed to the *next* unchecked item after confirming the previous one is checked off in the file. Announce which step you are starting.

