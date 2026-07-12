Frontend Guidelines
===================

## Shared components
- Use the `ErrorModal` component to display errors. The `ErrorModal` component will display the error message and a button to dismiss the modal.
- Use the `LoggedLayout` component to wrap pages that require authentication. The `LoggedLayout` component will display the top navigation bar and the side navigation bar.


## Frontend Testing Guidelines
- Place the test files along with the file being tested. No __tests__ folder.
- Don't place tests in `tests/` folder.`
- Name the test file with the following pattern: `filename.test.tsx` or `filename.test.ts`

## CSS styling

### Inline `cs` vs. `createStyles` Threshold

Use this rule to decide whether to inline or extract:

- **Single property** — inline is acceptable: `cs={{ width: '100%' }}`
- **Two or more properties** — extract to a module-level `createStyles` constant

```tsx
// ✅ Good - single property, inline is fine
<Card cs={{ width: '100%' }}>

// ✅ Good - multiple properties extracted to module level
const cardContentStyles = createStyles({
  flexDirection: 'column',
  rowGap: system.space.x4,
  paddingBottom: system.space.x6,
});

<Flex cs={cardContentStyles}>

// ❌ Bad - multiple properties inlined
<Flex cs={{ flexDirection: 'column', rowGap: system.space.x4, paddingBottom: system.space.x6 }}>

## Frontend Testing

The partner portal currently serves a small user base (3–10 partners) where manual smoke-checks against the dev server (`npm run partner-dev`) are faster and more reliable than maintaining UI-level tests. Keep the frontend test surface focused on logic — not on rendering — until the user base scales.

### ✅ Worth testing (Vitest)
- Conditional rendering driven by state, props, or query results
- Form validation, parsing, and submit handlers
- Click/keyboard handlers that trigger navigation, mutations, or state transitions
- Pure helpers: data transforms, reducers, derived values
- Error paths and edge cases that are tedious to reproduce in the browser

### 🚫 Not worth testing
- "Page X mounts without throwing" with no further assertions
- "Heading Y is in the document" smoke tests of static content
- Snapshot tests of static markup
- Re-tests of Canvas Kit / third-party component behavior
- Anything a 10-second click-through on the dev server would catch

Spacing tokens
Use Canvas Kit semantic spacing tokens from @workday/canvas-tokens-web as the default for these two properties. Do not use raw values, and prefer the semantic system.padding.* / system.gap.* tokens over system.space.x* here.

padding — always use system.padding.md.
gap — always use system.gap.sm.
import { system } from '@workday/canvas-tokens-web';
import { createStyles } from '@workday/canvas-kit-styling';

// ✅ Good
const rowStyles = createStyles({
  padding: system.padding.md,
  gap: system.gap.sm,
});

// ❌ Bad - hardcoded values
const rowStyles = createStyles({
  padding: '16px',
  gap: '8px',
});

// ❌ Bad - raw space token where a semantic one exists
const rowStyles = createStyles({
  padding: system.space.x4,
  gap: system.space.x2,
});
If a different size is genuinely required (for example asymmetric padding), still compose from system.padding.* tokens rather than raw values:

padding: `${system.padding.sm} ${system.padding.lg}`,

Colour tokens
Always use Canvas Kit colour tokens from @workday/canvas-tokens-web. Never use hardcoded colour values (hex, rgb, rgba, hsl, or named CSS colours like `red`/`white`). Prefer the semantic `system.color.*` tokens (text, background, border, icon, static, etc.) so components stay theme-aware; fall back to base palette tokens (`base.*`) only when no semantic token fits. See the full token reference at https://canvas.workdaydesign.com/styles/tokens/color.

import { system } from '@workday/canvas-tokens-web';
import { createStyles } from '@workday/canvas-kit-styling';

// ✅ Good - semantic colour tokens
const bannerStyles = createStyles({
  color: system.color.text.inverse,
  background: system.color.bg.primary.default,
  borderColor: system.color.border.divider,
});

// ❌ Bad - hardcoded colour values
const bannerStyles = createStyles({
  color: '#ffffff',
  background: '#0875e1',
  borderColor: 'rgba(0, 0, 0, 0.12)',
});

// ❌ Bad - named CSS colours
const bannerStyles = createStyles({
  color: 'white',
  background: 'blue',
});

