
### Domain-Based Organization (Required)

Organize code by **business domain**, not by technical layer. Each domain package contains all related components (controllers, services, repositories, entities) together for high cohesion.

```
# ✅ CORRECT - Domain-based organization (Package by Feature)
com.workday.globalpartnerportal/
├── partner/                        # Partner domain
│   ├── Partner.java                # Entity
│   ├── PartnerRepository.java      # Repository
│   ├── PartnerService.java         # Service
│   ├── PartnerDto.java             # DTO for API responses
│   ├── PartnerMapper.java          # Entity-DTO mapping
│   └── PartnerNotFoundException.java  # Domain-specific exception
├── organization/                   # Organization domain
│   ├── Organization.java
│   ├── OrganizationRepository.java
│   ├── OrganizationService.java
│   └── OrganizationController.java
└── common/                         # Cross-cutting concerns only
    ├── exception/
    │   ├── GlobalExceptionHandler.java
    │   └── ErrorResponse.java
    └── config/
        └── SecurityConfig.java
```


### Why Domain-Based?

| Benefit | Description |
|---------|-------------|
| **High Cohesion** | Related code lives together, easier to understand a feature |
| **Low Coupling** | Domains are independent, changes don't ripple across packages |
| **Scalability** | Easy to extract domains into microservices later |
| **Navigation** | Find all partner-related code in one place |
| **Testing** | Test a domain in isolation |


### Shared Package Guidelines

The `common/` package is ONLY for truly cross-cutting concerns:

```java
// ✅ Belongs in common/ - Global exception handling
package com.workday.globalpartnerportal.common.exception;

// ✅ Belongs in shared/ - Security configuration
package com.workday.globalpartnerportal.common.config;

// ✅ Belongs in common/ - Common utilities used everywhere
package com.workday.globalpartnerportal.common.util;

// ❌ Does NOT belong in common/ - Domain-specific DTOs
package com.workday.globalpartnerportal.common.dto;  // WRONG!
```
