
## Testing Guidelines

### Test Organization

Tests are organized into two categories:

| Type | Location | Naming | Purpose |
|------|----------|--------|---------|
| **Unit Tests** | `src/test/java/com/workday/globalpartnerportal/{domain}/` | `*Test.java` | Test individual classes in isolation |
| **Integration Tests** | `src/test/java/inttest/` | `*IntTest.java` | Test full application with database |

### Integration Tests (inttest package)

**All integration tests MUST:**
1. Be placed in the `inttest/{domain}` package
2. Use the `@WebIntegrationTest` annotation
3. Extend `TestIntBase` for database access
4. Follow the naming convention `*IntTest.java`

**Key classes in inttest package:**

| Class | Purpose |
|-------|---------|
| `WebIntegrationTest` | Meta-annotation combining `@SpringBootTest`, `@ActiveProfiles("test")`, and security config |
| `TestIntBase` | Base class providing singleton PostgreSQL container via Testcontainers |
| `TestSecurityConfig` | Test security configuration (disables CSRF, mocks OAuth2) |

**For database tests**, add `@Transactional` to ensure rollback:

```java
@WebIntegrationTest
@Transactional
class PartnerRepositoryIntTest extends TestIntBase {
  // Tests with automatic rollback
}
```

### Unit Tests (domain packages)

Unit tests remain in their domain packages alongside the code they test.
