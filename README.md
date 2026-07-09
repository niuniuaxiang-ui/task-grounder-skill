# Task Grounder Skill

`task-grounder` is a Codex skill for turning vague software ideas into a constrained, implementation-ready project brief.

它适合在正式编码前使用：先通过约束提问明确目标、非目标、模块边界、数据契约、接口契约、迭代顺序和验证方式，再把结果整理成一份后续 Codex 可以直接阅读执行的 Markdown 地基文档。

## What It Does

`task-grounder` helps Codex:

- Clarify fuzzy project ideas before coding.
- Define MVP scope and non-goals.
- Split modules and assign clear owners.
- Establish input/output contracts, state transitions, API/UI/CLI boundaries.
- Identify missing constraints and ask focused follow-up questions.
- Produce a reusable `.md` execution brief for future Codex sessions.
- Track local usage preferences over time without publishing private logs.

## When To Use

Use this skill when you want to:

1. Turn an idea into a buildable plan.
2. Decide what the first version should include.
3. Check what is still unconstrained before implementation.
4. Prepare a plan for Codex, VS Code Codex, Cursor, Claude Code, or another coding agent.
5. Avoid feature creep before vibe coding.
6. Design a paid feature, realtime feature, internal tool, data workflow, or integration.
7. Create a project handoff document that another agent can safely continue from.

Example prompts:

```text
Use $task-grounder to plan an Excel reconciliation tool. Ask constraint questions first, then produce an implementation brief.
```

```text
使用 $task-grounder，帮我把这个软件想法拆成 MVP、模块契约和分阶段计划，先不要写代码。
```

```text
Use task-grounder to check what is missing before I start coding this project.
```

## Output

The skill can produce a Markdown grounding document containing:

- Goal and non-goals
- Assumptions and open questions
- Constraint coverage table
- User roles and workflows
- MVP boundary
- Module/owner map
- Data entities and state transitions
- API / UI / CLI contracts
- Auth, payment, permission, and security constraints when relevant
- Iteration plan
- Verification gates
- Risk register
- Implementation handoff prompt

## Installation

### Install From This Repository

Use Codex's skill installer:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo niuniuaxiang-ui/task-grounder-skill --path skills/task-grounder
```

Windows PowerShell example:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo niuniuaxiang-ui/task-grounder-skill --path skills/task-grounder
```

Restart Codex after installation so the new skill is discovered.

### Manual Install

Copy this folder:

```text
skills/task-grounder
```

to your local Codex skills directory:

```text
~/.codex/skills/task-grounder
```

On Windows this is usually:

```text
%USERPROFILE%\.codex\skills\task-grounder
```

## Repository Structure

```text
skills/task-grounder/
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ constraint-checklist.md
│  ├─ grounding-template.md
│  ├─ usage-log.example.md
│  ├─ user-agent-constitution.md
│  └─ user-profile.md
└─ scripts/
   └─ record_usage.py
```

## Important Files

| File | Purpose |
|---|---|
| `SKILL.md` | Trigger metadata and main workflow |
| `agents/openai.yaml` | Codex UI metadata |
| `references/constraint-checklist.md` | Checklist for missing scope, owner, data, interface, payment, permission, and delivery constraints |
| `references/grounding-template.md` | Template for the generated project brief |
| `references/user-profile.md` | Default user preference profile; customize locally |
| `references/user-agent-constitution.md` | General agent rules used as a planning reference |
| `references/usage-log.example.md` | Template for local usage history |
| `scripts/record_usage.py` | Utility for appending local usage records |

## Personalization

After installing, you can customize:

```text
references/user-profile.md
```

Use it to record stable preferences such as:

- Preferred language
- Coding stack
- Planning style
- Verification expectations
- File organization rules
- Frontend or backend preferences

The skill can also write local usage history to:

```text
references/usage-log.local.md
```

This file is intentionally not included in the repository and should not be committed.

## Privacy

Do not record or publish:

- API keys
- tokens
- passwords
- payment credentials
- customer data
- production system data
- private business information

`record_usage.py` filters obvious sensitive keywords, but users are still responsible for not writing secrets into skill files or Git history.

## Readiness Gate

The skill uses a practical "95% readiness" gate before implementation.

This does not mean mathematical certainty. It means the task is constrained enough that Codex can implement with low drift:

- Goal is clear.
- Non-goals are stated.
- Owners are defined.
- Module contracts are written.
- Data and state are described.
- First implementation phase is scoped.
- Verification method is known.
- Remaining unknowns are classified as blocking, assumed, or deferred.

If readiness is not met, the skill should ask focused follow-up questions instead of jumping into code.

## Example Use Cases

| Use case | What the skill helps define |
|---|---|
| Excel reconciliation tool | Input files, matching keys, diff rules, export format, validation samples |
| Production reporting app | Data source, calculation rules, report layout, error states |
| Paid unlock flow | Payment method, manual approval vs official callback, entitlement state, security boundary |
| Realtime collaboration tool | Room model, WebSocket events, reconnect behavior, state ownership |
| Internal admin tool | Roles, permissions, audit log, data lifecycle, deployment boundary |
| AI-assisted workflow | Prompt boundary, user input contract, model output validation, fallback behavior |

## Validation

Run the skill validator:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/task-grounder
```

Windows PowerShell:

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\task-grounder"
```

Expected output:

```text
Skill is valid!
```

## Updating The Skill

Recommended workflow:

1. Edit `SKILL.md` for core behavior.
2. Edit files in `references/` for detailed templates or checklists.
3. Keep `SKILL.md` concise and move long reusable content into references.
4. Run validation.
5. Test the skill on a real planning task.
6. Avoid committing `usage-log.local.md` or any private data.

## Notes For Forks

If you fork this skill:

- Replace `references/user-profile.md` with your own preferences.
- Keep `usage-log.local.md` local only.
- Keep the installable skill path as `skills/task-grounder`.
- Ensure `SKILL.md` starts with valid YAML frontmatter:

```md
---
name: task-grounder
description: ...
---
```

