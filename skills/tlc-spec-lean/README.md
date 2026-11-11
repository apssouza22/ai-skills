# tlc-spec-lean

**Spec-driven feature work that freezes obligations, not the implementation plan.**

A Cursor/Claude agent skill from [Tech Leads Club](https://github.com/tech-leads-club). Version **2.2.0** (see `SKILL.md`). Derived from tlc-spec-driven 3.3.0 (Felipe Rodrigues), tlc-plan, and tlc-implement.

> Freeze the obligations. Free the plan. Prove it with someone who did not build it.

Agents often ship requirements that never became testable obligations, then claim done. This skill forces a **human-approved plan**, a **frozen checklist of claims with proofs**, implementation, then **scripted gates** plus an **independent Verifier** (and a screens judge when UI captures bind).

```
┌──────┐   ┌────────┐   ┌───────┐   ┌────────┐
│ PLAN │ → │ CHECKS │ → │ BUILD │ → │ VERIFY │
└──────┘   └────────┘   └───────┘   └────────┘
 human      obligations   agent       always
```

## When to use

Invoke when you want end-to-end feature delivery with proof, for example:

- `tlc-spec-lean`
- `plan feature`
- `specify feature`
- `write the checks`
- `build this plan`
- `verify work`

**Do not use** for standalone design docs, architecture-only decomposition, or work that is already a task list to execute.

**Small change shortcut:** roughly three files touched and no one-way door → write only `.agents/plans/<feature>/checks.md` with an `## Intent` paragraph (skip `plan.md`).

## Installation

Copy or symlink the skill folder into your agent skills directory (Cursor example):

```bash
mkdir -p ~/.cursor/skills
cp -R /path/to/ai-commands/skills/tlc-spec-lean ~/.cursor/skills/tlc-spec-lean
```

Or point your project at this repo’s copy and let the agent load `skills/tlc-spec-lean/SKILL.md`.

**Requirements**

| Need | Purpose |
| --- | --- |
| Python 3.8+ (stdlib only) | Validation gates |
| git | Proofs at `HEAD`, commit discipline |
| Sub-agents (recommended) | Independent Verifier and screens judge |
| Browser automation (optional) | `<capture>.running.png` and walk proofs |
| Vision-capable model (optional) | Compare running screenshots to captures |

The skill does not bundle a test runner; proofs use **your** project's commands.

## Quick start (humans)

1. Ask the agent to **plan** a named feature (e.g. `billing-dunning`).
2. Review `.agents/plans/billing-dunning/plan.md`, answer open questions, and approve (the agent records your exact words in `**Approved**:`).
3. Let the agent write **checks** and run `validate_checks.py … --execute` (build must be green before code changes).
4. **Build** proceeds; tests are written from checks, not by reading implementation first.
5. **Verify:** `check_proofs.py`, Verifier + screens sub-agents, fixes, then `validate_verification.py` must exit 0 before "done."

Artifacts live under `.agents/plans/` in the target repository (not inside this skill folder).

## Workflow

| Phase | You / agent | Output |
| --- | --- | --- |
| **Plan** | Human reviews one document | Problem, EARS criteria, path & diagrams, API surface, one-way **Landing** doors |
| **Checks** | Obligations frozen after gate | Numbered checks, `Proof:` lines, **Coverage** join, **Swept** (9 dimensions) |
| **Build** | Agent implements freely within conventions | Code, tests, commits, optional screenshots & walk |
| **Verify** | Always runs | `proofs.md`, `verification.md`, `screens.md`, completion gate |

### EARS criteria (plan)

Requirements use patterns like:

- **Ubiquitous:** The system SHALL …
- **WHEN** trigger **THEN** …
- **WHILE** state …
- **IF** unwanted condition **THEN** …

Each criterion carries a **concrete value** (status code, field name, bound)—not “fast” or “user-friendly.”

### Checks and proofs

Every check is one observable claim plus how to settle it:

```markdown
Run unit: `npm test -- --reporter=verbose`

**C1** - A failed charge sets status to Suspended, never Cancelled (AC 1)
Proof: run unit | ✓ billing > suspends on a failed charge
```

Grouped runs execute once; each check must match a **specific passing line** in output (guards against empty test filters). Lone proofs use exit code only.

UI that matches a design capture:

```markdown
Proof: browser - reach the state, save `captures/admin.running.png`
```

### Independent verification

| Layer | Catches |
| --- | --- |
| `check_proofs.py` | Proofs, build, pictures, walk at `HEAD` |
| **Verifier** sub-agent | Weak assertions, missing edge cases, criteria vs tests |
| **Screens** sub-agent | Running PNG vs binding capture (when applicable) |

The builder must **not** be the Verifier.

## Repository layout (this skill)

```
tlc-spec-lean/
├── README.md                 # This file (humans)
├── SKILL.md                  # Agent entrypoint and rules
├── references/
│   ├── plan.md               # Plan phase
│   ├── checks.md             # Checks phase
│   ├── build.md              # Build phase
│   ├── verify.md             # Verifier round
│   ├── verify-screens.md     # Screenshot judge
│   └── memory.md             # STATE, lessons, resume after compaction
└── scripts/
    ├── validate_plan.py
    ├── validate_checks.py
    ├── check_commit.py
    ├── check_proofs.py
    ├── validate_verification.py
    ├── lessons.py
    ├── selftest.py           # Mutation tests on fixtures
    └── fixtures/             # Worked example artifact set
```

Run scripts from the project root (or pass `--root`):

```bash
SKILL=~/.cursor/skills/tlc-spec-lean   # adjust path

python3 $SKILL/scripts/validate_plan.py my-feature
python3 $SKILL/scripts/validate_checks.py my-feature --execute
python3 $SKILL/scripts/check_commit.py --message "feat(billing): suspend on failed charge"
python3 $SKILL/scripts/check_proofs.py my-feature
python3 $SKILL/scripts/validate_verification.py my-feature
```

Non-zero exit means stop and fix what the script reports.

## Artifacts in the target project

```
.agents/plans/
├── STATE.md                          # AD-NNN decisions
├── LESSONS.md                        # generated; do not hand-edit
└── <feature>/
    ├── plan.md
    ├── checks.md
    ├── captures/                     # binding sources + *.running.png
    ├── proofs.md                     # written by check_proofs.py
    ├── screens.md
    └── verification.md
```

**Files are the source of truth.** Chat and compaction are not durable; the agent re-reads `SKILL.md`, the phase reference, and feature files when resuming (`references/memory.md`).

## Core rules (summary)

1. Every check = claim + proof (test line, command exit code, or screenshot judge).
2. Write tests from the **check**, not from the implementation.
3. Change a test only when its claim changes; ship test and code in the same commit.
4. After `validate_checks.py` passes, checks are frozen (append only for gaps).
5. Verifier is always a fresh sub-agent; `validate_verification.py` is the done gate.
6. Approved spec allows **local commits**; push/deploy/production need explicit approval.

Full rules: `SKILL.md`.

## Learning the format

`scripts/fixtures/` holds a minimal passing **plan**, **checks**, **proofs**, and **verification** set used by `selftest.py`. Read those files after reading `SKILL.md` for a concrete shape.

## License

**CC-BY-4.0** — Tech Leads Club. See `SKILL.md` front matter.

When redistributing or adapting, keep attribution and note modifications.
