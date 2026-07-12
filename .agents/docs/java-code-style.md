### Java Code Style

The project enforces [Google Java Style](https://google.github.io/styleguide/javaguide.html) via Checkstyle (`config/checkstyle/checkstyle.xml`). Key rules:

| Rule | Detail |
|------|--------|
| **Javadoc on types** | All `public` and `protected` classes, interfaces, enums, records, and annotations **must** have a Javadoc comment — including enums |
| **Javadoc on methods** | All `public` methods with 2+ lines must have Javadoc (except `@Override` and `@Test`) |
| **Final parameters** | All method parameters must be declared `final` |
| **Final local variables** | Local variables that can be final must use `final` (or `final var`) |
| **No star imports** | `import java.util.*` is forbidden |
| **Import order** | Static imports first (alphabetically), then third-party packages (alphabetically), with a blank line between groups |
| **Line length** | 120 characters max for Java |
| **Indentation** | 2 spaces — no tabs |
| **Braces** | Opening brace on same line; `if`/`for`/`while`/`else`/`do` always require braces |

```java
// ✅ Good - follows Google Java Style, proper Javadoc, final parameters
package com.workday.globalpartnerportal.partner;

import org.springframework.stereotype.Service;

/**
 * Service for managing partner operations.
 */
@Service
public class PartnerService {

  private final PartnerRepository partnerRepository;

  public PartnerService(final PartnerRepository partnerRepository) {
    this.partnerRepository = partnerRepository;
  }

  /**
   * Retrieves a partner by their unique identifier.
   *
   * @param partnerId the partner's unique ID
   * @return the partner entity
   */
  public Partner getPartnerById(final Long partnerId) {
    if (partnerId == null) {
      throw new IllegalArgumentException("Partner ID is required");
    }
    return this.partnerRepository
            .findById(partnerId)
            .orElseThrow(() -> new PartnerNotFoundException(partnerId));
  }
}

// ❌ Bad - missing Javadoc, star imports, no final, poor naming
package com.workday.globalpartnerportal.service;  // WRONG: layer-based package

import org.springframework.stereotype.*;
import com.workday.globalpartnerportal.repository.*;

@Service
public class PS {
  PartnerRepository r;
  public Partner get(Long x) {
    return r.findById(x).get();
  }
}
```
