## Project Knowledge

Here is a list of important project knowledge that you should know before executing any task.

### Tech Stack

**Backend:**
- Java 21
- Spring Boot
- Gradle 8.x with Kotlin DSL
- JUnit 5 with Testcontainers (PostgreSQL)

**Frontend:**
- React 18 with TypeScript
- Vite 7 for development and builds

**Code Quality:**
- Checkstyle  (Google Java Style)
- Spotless (Eclipse Java formatter)
- ESLint  Prettier


## Tools You Can Use

### Backend Commands

| Command | Description |
|---------|-------------|
| `./gradlew build` | Compile, test, and package the application |
| `./gradlew clean build` | Clean build from scratch |
| `./gradlew test` | Run all JUnit tests |
| `./gradlew clean test --no-build-cache --info` | Run tests without cache (verbose) |
| `./gradlew dev` | Run with hot reload (continuous compilation + bootRun) |
| `./gradlew check` | Run all verification tasks (tests, checkstyle, version checks) |
| `./gradlew checkstyleMain` | Run Checkstyle on main sources |

### Frontend Commands

Webapps live under **npm workspaces** in the root `package.json` (`global-portal-shared/webapp`, `partner-portal-application/webapp`, `admin-portal-application/webapp`). Prefer running install and multi-app commands from the **repository root**.

**From repository root**

| Command | Description |
|---------|-------------|
| `npm install` | Install dependencies for the root and all workspaces |
| `npm run build` | Equivalent to `npm run build --workspaces --if-present`: run each workspace’s `build` script where it exists |
| `npm run build --workspaces --if-present` | Explicit form: build all webapps that define `build` (workspaces without `build` are skipped) |
| `npm run build -w partner-portal-application/webapp` | Partner portal webapp only (same as `npm run partner-build`) |
| `npm run build -w admin-portal-application/webapp` | Admin portal webapp only (same as `npm run admin-build`) |

**From a single webapp directory** (for example `partner-portal-application/webapp/`)

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server (port 5173) |
| `npm run build` | TypeScript compile + production build for this app |
| `npm run lint` | Run ESLint |
| `npm run format` | Auto-format with Prettier |
| `npm run format:check` | Check formatting without changes |


## Line Length Limits
- **Java:** 120 characters max
- **TypeScript/JavaScript:** 120 chars max


## Code structure
**/webapp # Frontend code
/buildSrc # Gradle Build scripts
/it # docker compose files and data required for local development

@.agents/rules/security-guidelines.md

## Boundaries

### ✅ Always
- Organize code by domain package, not by technical layer
- Write to `**/webapp/src/` for frontend code
- Add new Liquibase SQL migrations to `global-portal-shared/src/main/resources/db/sql/`
- Write unit tests in domain packages mirroring main source structure
- Write integration tests in `inttest` package using `@WebIntegrationTest` and extending `TestIntBase` when webserver is required
- Use @IntegrationTest (+ TestIntBase) — for integration tests living in global-portal-shared
- Run `npm run format` before committing frontend changes
- Use version catalog (`gradle/libs.versions.toml`) for all dependencies
- Add Javadoc to all public **and protected** classes, interfaces, enums, records, and annotations — and to all public methods with 2+ lines (except `@Override`/`@Test`)
- Use `final` keyword for method parameters in Java
- Use `final var` for local variables in Java when type is obvious from context
- Use TypeScript strict mode with proper typing (no `any`)
- Use Java records for DTOs, value objects, and immutable data classes
- Use environment variables or secrets manager for all sensitive configuration
- Return generic error messages to API clients (no internal details)
- Log exceptions server-side with correlation IDs for debugging
- Use @Slf4j for logging. This will automatically create a logger instance named `log` that you can use for logging throughout your class.
- Validate all user input at controller/API boundaries
- Sanitize data before rendering in frontend
- Create new pages in `**/webapp/src/features/{page-name}/{page-name}Page.tsx`
- Add @Transactional to all services and repository methods
- Add new domain packages to `global-portal-shared/src/main/java/com/workday/globalpartnerportal/domain/`

### ⚠️ Ask First
- Database schema changes or migrations
- Adding new dependencies to `build.gradle.kts` or `package.json`
- Modifying CI/CD configuration
- Changes to `buildSrc/` custom Gradle tasks
- Modifications to `config/checkstyle/` rules
- Changes to authentication or security configurations
- API endpoint changes that affect external consumers
- Adding new environment variables for secrets

### 🚫 Never
- Create layer-based packages (`controller/`, `service/`, `repository/`, `entity/`)
- Commit secrets, API keys, or credentials
- Hardcode versions in `build.gradle.kts` files (use `libs.versions.toml`)
- Edit generated files in `build/` or `dist/` directories
- Edit `node_modules/` or `gradle/wrapper/`
- Use star imports in Java (`import java.util.*`)
- Use `Optional.get()` without checking presence first
- Skip writing Javadoc for public or protected types (classes, interfaces, enums, records) or public methods with 2+ lines
- Use `@SuppressWarnings` without justification comment
- Remove or skip failing tests to make builds pass
- Hardcode secrets, passwords, or API keys in `application.yml` or `application.properties`
- Expose exception messages, stack traces, or internal system details in API responses
- Log sensitive data (passwords, tokens, credit cards, PII)
- Concatenate user input into SQL queries (use parameterized queries)
- Store sensitive tokens in localStorage (use httpOnly cookies)
- Use `dangerouslySetInnerHTML` with unsanitized user input
- Disable CSRF protection without explicit security review
- Return different error messages for authentication failures (prevents user enumeration)
- Call repositories directly from other domains (use services for cross-domain interactions)
- Use @Nested tests in integration tests. Keep integration tests flat for better organization and to avoid issues with Spring context loading.

### PR Title Requirements

PR titles **must** start with a valid JIRA ID:

```
✅ LSDPS-1234: Add partner management feature
✅ GPP-567: Fix authentication bug
❌ Add new feature (missing JIRA ID)
❌ fix: Update styles (missing JIRA ID)
```

## Local Development URLs

- **Backend API:** http://localhost:8081
- **Frontend Dev Server:** http://localhost:5173


# Task execution plan
Important: Always plan the task step by step before writing code. Ask for permission to proceed with the plan.
Important: Before proceed with the plan, create a new file named `.agents/plans/name-of-the-task.md`.
Based on the approved plan, list all necessary implementation steps as GitHub-style checkboxes (`- [ ] Step Description`). Use sub-bullets for granular details within each main step.


- Plans should be detailed enough to execute without ambiguity
- Each task in the plan must include at least one validation test to verify it works. Preferably an integration test.
- Assess complexity and single-pass feasibility - can an agent realistically complete this in one go?
- Include a complexity indicator at the top of each plan:
  ✅ Simple - Single-pass executable, low risk
  ⚠️ Medium - May need iteration, some complexity
  🔴 Complex - Break into sub-plans before executing

**CRITICAL: After you successfully complete each step, you MUST update the `.agents/plans/name-of-the-task.md` file by changing the corresponding checkbox from `- [ ]` to `- [x]`.**
Only proceed to the *next* unchecked item after confirming the previous one is checked off in the file. Announce which step you are starting.
