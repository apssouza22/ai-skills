# Code Structure Guidelines

## Package Architecture

### Domain-Based Organization (Required)

Organize code by **business domain**, not by technical layer. Each domain package contains all related components (controllers, services, repositories, entities) together for high cohesion.

**✅ CORRECT - Domain-based organization (Package by Feature):**
- Group all classes by business domain (e.g., `partner/`, `organization/`, `certification/`)
- Each domain package contains:
  - Entity (e.g., `Partner.java`)
  - Repository (e.g., `PartnerRepository.java`)
  - Service (e.g., `PartnerService.java`)
  - Controller (e.g., `PartnerController.java`)
  - DTOs (e.g., `PartnerDto.java`, `CreatePartnerRequest.java`)
  - Mappers (e.g., `PartnerMapper.java`)
  - Domain-specific exceptions (e.g., `PartnerNotFoundException.java`)
- Use `common/` package ONLY for cross-cutting concerns

**❌ WRONG - Layer-based organization (Anti-pattern):**
- Do NOT create technical layer packages (`controller/`, `service/`, `repository/`, `entity/`)
- Do NOT mix different business domains in the same package
- Do NOT organize by technical function instead of business capability

### Example Structure

```
com.company.project/
├── partner/                        # Partner domain
│   ├── Partner.java                # Entity
│   ├── PartnerRepository.java      # Repository
│   ├── PartnerService.java         # Service
│   ├── PartnerController.java      # Controller
│   ├── PartnerDto.java             # DTO for API responses
│   ├── CreatePartnerRequest.java   # Request DTO
│   ├── PartnerMapper.java          # Entity-DTO mapping
│   └── PartnerNotFoundException.java  # Domain-specific exception
├── organization/                   # Organization domain
│   ├── Organization.java
│   ├── OrganizationRepository.java
│   ├── OrganizationService.java
│   └── OrganizationController.java
├── certification/                  # Certification domain
│   ├── Certification.java
│   ├── CertificationRepository.java
│   ├── CertificationService.java
│   └── CertificationController.java
└── common/                         # Cross-cutting concerns only
    ├── exception/
    │   ├── GlobalExceptionHandler.java
    │   └── ErrorResponse.java
    ├── config/
    │   ├── SecurityConfig.java
    │   └── DatabaseConfig.java
    └── util/
        └── DateUtils.java
```

### Why Domain-Based Organization?

| Benefit | Description |
|---------|-------------|
| **High Cohesion** | Related code lives together, making it easier to understand a complete feature |
| **Low Coupling** | Domains are independent, changes don't ripple across packages |
| **Scalability** | Easy to extract domains into microservices later if needed |
| **Navigation** | Find all partner-related code in one place (`partner/` package) |
| **Testing** | Test a domain in isolation without dependencies on other domains |
| **Team Ownership** | Teams can own entire domains rather than technical layers |
| **Reduced Merge Conflicts** | Different teams work in different domain packages |

### Shared Package Guidelines

The `common/` package is ONLY for truly cross-cutting concerns that are used across ALL domains.

**✅ Belongs in `common/`:**
- Global exception handling (`common/exception/GlobalExceptionHandler.java`)
- Security configuration (`common/config/SecurityConfig.java`)
- Database configuration (`common/config/DatabaseConfig.java`)
- Common utilities used everywhere (`common/util/DateUtils.java`)
- Shared base classes or interfaces used across all domains

**❌ Does NOT belong in `common/`:**
- Domain-specific DTOs (place in domain package instead, e.g., `partner/PartnerDto.java`)
- Domain-specific business logic (belongs in domain service)
- Domain-specific exceptions (belongs in domain package)
- Domain-specific validators (belongs in domain package)
- Domain-specific mappers (belongs in domain package)

### Code Review Checklist for Package Structure

When reviewing code, verify:

- [ ] **No layer-based packages**: No `controller/`, `service/`, `repository/`, `entity/` packages exist
- [ ] **Domain packages exist**: Code is organized by business domain (e.g., `partner/`, `organization/`)
- [ ] **Complete domains**: Each domain package contains all related components (entity, repository, service, controller, DTOs)
- [ ] **Proper common/ usage**: Only cross-cutting concerns are in `common/` package
- [ ] **No domain mixing**: Each domain package contains only classes related to that domain
- [ ] **Domain-specific exceptions**: Exceptions like `PartnerNotFoundException` are in the `partner/` package, not `common/`
- [ ] **Domain-specific DTOs**: Request/Response DTOs are in their domain package, not `common/dto/`

### Migration from Layer-Based to Domain-Based

If you find layer-based organization, suggest refactoring:

**Before (Layer-based - WRONG):**
```
com.company.project/
├── controller/
│   ├── PartnerController.java
│   └── OrganizationController.java
├── service/
│   ├── PartnerService.java
│   └── OrganizationService.java
└── repository/
    ├── PartnerRepository.java
    └── OrganizationRepository.java
```

**After (Domain-based - CORRECT):**
```
com.company.project/
├── partner/
│   ├── Partner.java
│   ├── PartnerController.java
│   ├── PartnerService.java
│   └── PartnerRepository.java
└── organization/
    ├── Organization.java
    ├── OrganizationController.java
    ├── OrganizationService.java
    └── OrganizationRepository.java
```

### Critical Review Points

**🔴 CRITICAL (blocks merge):**
- Creating new layer-based packages (`controller/`, `service/`, etc.)
- Adding domain-specific code to `common/` package
- Mixing multiple domains in a single package

**🟡 IMPORTANT (should be changed):**
- Domain packages missing related components (e.g., service exists but no controller)
- Inconsistent package naming across domains
- Domain-specific utilities in `common/util/`

**🔵 SUGGESTIONS (nice to have):**
- Consider splitting large domain packages into sub-domains
- Add package-info.java for domain package documentation
- Group related DTOs in a `dto/` sub-package within the domain

