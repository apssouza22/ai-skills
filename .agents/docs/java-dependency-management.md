### Dependency Management

All versions MUST be defined in `gradle/libs.versions.toml`:

```toml
# ✅ Good - centralized in libs.versions.toml
[versions]
springBootPlugin = "3.5.8"

[libraries]
spring-boot-starter-web = { module = "org.springframework.boot:spring-boot-starter-web" }

[plugins]
springBoot = { id = "org.springframework.boot", version.ref = "springBootPlugin" }
```

```kotlin
// ✅ Good - reference from catalog in build.gradle.kts
dependencies {
    implementation(libs.spring.boot.starter.web)
}

// ❌ Bad - hardcoded version
dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web:3.5.8")
}
```
