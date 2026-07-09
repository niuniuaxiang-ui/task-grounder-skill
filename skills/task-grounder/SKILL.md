---
name: task-grounder
description: Plan and constrain vague software/product/vibe-coding tasks before implementation. Use when the user asks to plan a project, define boundaries, split modules, establish contracts, design an MVP, create a phased execution brief, decide what to build next, convert an idea into an actionable .md plan, or repeatedly refine requirements through questions before coding. Also use when the user asks Codex to follow their personal AGENTS-style rules, check missing constraints, or optimize future work from usage habits.
---

# Task Grounder

## Purpose

Turn fuzzy intent into a grounded execution brief that Codex can later implement with minimal drift. Prioritize boundary, owner, contract, iteration plan, verification, and user-specific rules before code.

This skill is for planning and constraint-setting. Do not implement code during grounding unless the user explicitly asks to proceed after the brief is accepted.

## Required Reads

Before finalizing any execution brief, read:

- `references/user-profile.md` for the user's current working preferences.
- `references/grounding-template.md` for the output structure.
- `references/constraint-checklist.md` for missing-boundary checks.

Read `references/user-agent-constitution.md` when the task will produce a development plan, handoff, project rule file, or implementation brief. Treat it as the user's local rule source unless a newer explicit user instruction overrides it.

Read `references/usage-log.local.md` when improving the user's preference profile or when the user asks why the skill made a particular planning choice. If it does not exist yet, create it from `references/usage-log.example.md`.

## Workflow

1. Restate the task in one sentence.
2. Identify whether the task is a new project, existing project, feature, refactor, debugging task, monetization flow, integration, document, or review.
3. Audit available truth: user request, attached files, repo files, current `AGENTS.md`, docs, package scripts, tests, and current git state when relevant.
4. Build a constraint matrix using `references/constraint-checklist.md`.
5. If blockers remain, ask at most 3 high-impact questions. Prefer questions that decide owner, product boundary, data contract, payment/security, deployment, or verification. Do not ask cosmetic questions before architecture blockers.
6. When safe assumptions can unblock progress, state the assumption and continue. Mark it as `待确认`.
7. Define owner boundaries and module contracts before implementation steps.
8. Produce a phased plan with validation gates after every phase.
9. Generate or update a self-contained Markdown execution brief when the user asks for a plan, handoff, or "next step" document.
10. End with one recommended next action, not a menu of equal options.

## Question Rules

- Ask only what changes the plan materially.
- Use short, concrete questions.
- Do not ask more than 3 questions in one pass.
- If the user is exploring ideas, guide them with defaults.
- If the user says "先做计划", "先别写代码", "先划边界", or similar, stay in planning mode.
- If the user asks "下一步怎么做", return the next smallest validated step and the stop condition.

## Readiness Gate

Use a "95% readiness" gate as an operational threshold, not a mathematical guarantee.

Do not mark a task ready for implementation unless:

- All blocker items in the constraint checklist are either constrained or explicitly marked `不适用`.
- Owner boundaries are named.
- Module contracts have inputs, outputs, responsibilities, non-responsibilities, and validation points.
- Unknowns are classified as `阻断`, `可假设`, or `可后置`.
- The first implementation phase has exact file/module scope and verification commands or evidence.
- The brief includes non-goals and anti-drift rules.

If the gate fails, tell the user what is missing and ask the next 1-3 questions.

## Execution Brief Requirements

Use `references/grounding-template.md`.

The brief must be useful to a future Codex instance without relying on chat memory. Include:

- Goal and non-goals.
- Assumptions.
- Product boundary.
- User roles and workflows.
- Module/owner map.
- Data contracts and state transitions.
- API/UI/CLI contracts when applicable.
- Payment/auth/security constraints when applicable.
- Iteration plan.
- Verification gates.
- Risk register.
- Open questions.
- Handoff prompt for implementation.
- User-specific rules from `references/user-profile.md`.

Save the brief only when it helps the task. Default locations:

- Existing repo: `docs/task-grounding/<short-project-name>.md`.
- Projectless or exploratory work: `outputs/<short-project-name>-grounding.md`.
- If the user gives a path, use that path.

## Habit Iteration

At the end of each meaningful use:

1. Append a short entry to `references/usage-log.local.md` when file writing is available and the user did not forbid persistence. Prefer running `scripts/record_usage.py` for consistent formatting.
2. Update `references/user-profile.md` only when the user explicitly states a stable preference, corrects the skill, or the same preference appears in at least two uses.
3. Never record secrets, private tokens, payment credentials, customer data, or sensitive production data.
4. Keep the profile concise. Prefer rules that change future behavior.
5. Mention any profile update in the final response.

Example:

```bash
python scripts/record_usage.py --task "U9/MES 对账工具规划" --goal "约束 MVP 和模块契约" --constraints "不碰生产库；先 Excel 导入导出" --assumptions "使用 Python + TypeScript" --next-adjustment "同类企业工具优先先做离线 MVP"
```

## Output Style

- Use simplified Chinese.
- Be concise but do not omit boundary, contract, validation, or risk.
- Prefer tables for comparison and constraint coverage.
- Prefer numbered phases for execution plans.
- Give one recommended main path.
- Avoid implementation details until the ground is stable.
