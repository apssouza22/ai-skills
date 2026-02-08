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

### Java Code Style

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

**❌ Bad practices:**
- Missing Javadoc on public APIs
- Star imports (`import java.util.*`)
- No `final` on method parameters
- Poor naming (single letters, abbreviations)
- Layer-based package organization
- Using `Optional.get()` without checking presence
- Null pointer risks from unchecked operations

### Local Variable Type Inference (`var`)

Use `final var` for local variables when the type is obvious from the right-hand side. This reduces verbosity while maintaining immutability.

**✅ Good - Use `final var` when type is obvious:**
- Method return values where type is clear from method name
- Constructor calls: `final var list = new ArrayList<String>()`
- Factory methods: `final var id = UUID.randomUUID()`
- Stream operations with clear terminal operations

**✅ Good - Use explicit type when it improves clarity:**
- Empty collections: `final List<Partner> emptyList = new ArrayList<>()`
- When the type isn't obvious from context
- Public API signatures (method parameters, return types, fields)

**❌ Bad - Explicit type when var would be clearer:**
- Redundant type declaration when right-hand side is obvious
- Example: `final String id = UUID.randomUUID().toString()` (use `final var` instead)

**❌ Bad - var without final (prefer immutability):**
- Always use `final var` instead of just `var`

### Java Records for Data Classes

Use Java records for DTOs, value objects, and immutable data carriers. Records provide concise syntax with automatic `equals()`, `hashCode()`, `toString()`, and accessor methods.

**✅ Good - Use records for:**
- Request/Response DTOs with Bean Validation annotations
- Value objects with immutable data
- Data carriers with factory methods (e.g., `from(Entity entity)`)
- Records with validation in compact constructor
- Records with helper methods (e.g., `isExpired()`)

**❌ Bad - Using regular classes for simple data carriers:**
- Do NOT create classes with getters/setters for simple DTOs
- Do NOT use mutable POJOs when records are appropriate

**When to use records:**
- Request/Response DTOs
- Value objects
- Immutable data carriers
- Configuration holders

**When NOT to use records:**
- JPA entities (require mutable state and no-arg constructor)
- Classes that need inheritance
- Classes with complex mutable state

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

**❌ Bad practices:**
- Using `any` type
- Untyped component props
- Single-letter or abbreviated variable names
- Missing dependency arrays in useEffect
- Inline complex logic in JSX
- Missing keys in mapped lists
- Not handling loading/error states

### Dependency Management

All versions MUST be defined in `gradle/libs.versions.toml`:

**✅ Good practices:**
- Define all versions in `[versions]` section of `libs.versions.toml`
- Define libraries in `[libraries]` section referencing versions
- Define plugins in `[plugins]` section referencing versions
- Reference catalog entries in `build.gradle.kts` using `libs.` prefix
- Keep all version management centralized

**❌ Bad practices:**
- Hardcoding versions directly in `build.gradle.kts` files
- Duplicating version numbers across multiple files
- Using string literals for dependency coordinates with versions

### Line Length Limits

- **Java:** 120 characters max
- **TypeScript/JavaScript:** 120 chars max

## Security Guidelines

### Secrets Management

**Never hardcode secrets in configuration files.** All sensitive values must be injected via environment variables or a secrets manager.

**✅ CORRECT practices:**
- Use environment variable placeholders in `application.yml`: `${DB_PASSWORD}`, `${API_KEY}`, etc.
- Store secrets in environment variables or secrets management systems
- Use placeholder syntax for all sensitive configuration values
- Document required environment variables in README

**❌ WRONG practices:**
- Hardcoding passwords, API keys, or secrets directly in `application.yml` or `application.properties`
- Committing files containing actual secret values
- Using default/example secrets in production configurations


### Error Handling and API Responses

**Never expose internal exception messages, stack traces, or system details to API consumers.** This prevents information disclosure that attackers could exploit.

### Input Validation

**Always validate and sanitize user input at system boundaries.**

**✅ CORRECT practices:**
- Use Bean Validation annotations on DTOs (`@NotBlank`, `@Email`, `@Size`, `@Pattern`)
- Validate path variables and query parameters with annotations (`@Min`, `@Max`, `@Pattern`)
- Add custom validation messages for better user feedback
- Validate at controller/API boundaries before processing
- Use records with validation annotations for request DTOs

**❌ WRONG practices:**
- Accepting unvalidated user input
- Skipping validation on path variables or query parameters
- Processing input without checking constraints
- Missing validation annotations on request DTOs

### SQL Injection Prevention

**Always use parameterized queries. Never concatenate user input into SQL.**

### Logging Security

**Never log sensitive data.**

**✅ CORRECT practices:**
- Log only safe identifiers (user IDs, correlation IDs, email addresses)
- Mask sensitive data if logging is absolutely required (e.g., first 4 characters of token)
- Use correlation IDs for request tracking instead of tokens
- Log business events without exposing sensitive details

**❌ WRONG practices:**
- Logging passwords, tokens, API keys, or authentication credentials
- Logging credit card numbers or payment details
- Logging personally identifiable information (PII) without masking
- Including full tokens or secrets in log messages

### Frontend Security (TypeScript/React)

**✅ CORRECT practices:**
- Use httpOnly cookies for authentication tokens (set by backend)
- Let React handle escaping automatically (avoid `dangerouslySetInnerHTML`)
- Store only public configuration in frontend code
- Use environment variables for API endpoints (`import.meta.env.VITE_*`)
- Validate and sanitize user input before rendering

**❌ WRONG practices:**
- Storing sensitive tokens or API keys in localStorage or sessionStorage
- Using `dangerouslySetInnerHTML` with unsanitized user input
- Hardcoding secrets or API keys in frontend code (they're visible in bundles)
- Exposing backend secrets or credentials in frontend configuration
- Trusting client-side validation alone (always validate on backend)

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

## Testing Guidelines

### Test Organization

Tests are organized into two categories:

| Type | Location                                          | Naming | Purpose |
|------|---------------------------------------------------|--------|---------|
| **Unit Tests** | `src/test/java/com/mycompany/myproject/{domain}/` | `*Test.java` | Test individual classes in isolation |
| **Integration Tests** | `src/test/java/inttest/`                          | `*IntTest.java` | Test full application with database |

### Integration Tests (inttest package)

**All integration tests MUST:**
1. Be placed in the `inttest` package
2. Use the `@WebIntegrationTest` annotation
3. Extend `TestIntBase` for database access
4. Follow the naming convention `*IntTest.java`

**For database tests**, add `@Transactional` to ensure rollback after each test method.

### Unit Tests (domain packages)

Unit tests remain in their domain packages alongside the code they test.


## Local Development URLs

- **Backend API:** http://localhost:8081
- **Frontend Dev Server:** http://localhost:5173

# Task execution plan
Important: Always plan the task step by step before writing code. Ask for permission to proceed with the plan.
Important: Before proceed with the plan, create a new file named `tasks/name-of-the-task.md`. Based on the approved plan, list all necessary implementation steps as GitHub-style checkboxes (`- [ ] Step Description`). Use sub-bullets for granular details within each main step.

**CRITICAL: After you successfully complete each step, you MUST update the `tasks/name-of-the-task.md` file by changing the corresponding checkbox from `- [ ]` to `- [x]`.**
Only proceed to the *next* unchecked item after confirming the previous one is checked off in the file. Announce which step you are starting.

