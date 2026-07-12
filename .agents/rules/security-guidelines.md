
## Security Guidelines

### Secrets Management

**Never hardcode secrets in configuration files.** All sensitive values must be injected via environment variables or a secrets manager.

**Secrets that must NEVER be committed:**
- Database passwords
- API keys and tokens
- OAuth client secrets
- JWT signing keys
- Encryption keys
- Private certificates
- Third-party service credentials

### Error Handling and API Responses

**Never expose internal exception messages, stack traces, or system details to API consumers.** This prevents information disclosure that attackers could exploit.

### Input Validation

**Always validate and sanitize user input at system boundaries.**

```java
// ✅ CORRECT - Validate input with Bean Validation
public record CreatePartnerRequest(
    @NotBlank(message = "Name is required")
    @Size(max = 255, message = "Name must not exceed 255 characters")
    String name,
    
    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    String email,
    
    @Pattern(regexp = "^[A-Z]{2,3}$", message = "Invalid country code")
    String countryCode
) {}

// ✅ CORRECT - Validate path variables and query params
@GetMapping("/partners/{id}")
public Partner getPartner(@PathVariable @Min(1) final Long id) {
  return partnerService.getPartnerById(id);
}
```

### Frontend Security (TypeScript/React)
- Use httpOnly cookies for authentication tokens (set by backend)
- Let React handle escaping automatically (avoid `dangerouslySetInnerHTML`)
- Store only public configuration in frontend code
- Use environment variables for API endpoints (`import.meta.env.VITE_*`)
- Validate and sanitize user input before rendering
