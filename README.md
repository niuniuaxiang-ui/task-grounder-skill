# 任务地基技能

`task-grounder` 是一个用于 Codex 的规划约束类技能。它的作用是：在正式编码前，把模糊的软件想法、功能需求、集成任务或 vibe coding 方向，整理成边界清晰、契约明确、可以继续执行的项目地基文档。

它不追求一上来写代码，而是先帮助使用者明确：要做什么、不做什么、谁负责什么、数据怎么流动、接口怎么约定、每一阶段怎么验收、哪些风险需要提前挡住。

## 能做什么

`task-grounder` 可以帮助 Codex：

- 把模糊想法整理成可执行计划。
- 明确第一版最小可用范围。
- 写清目标、非目标和防跑偏规则。
- 拆分模块，并确定每个模块的责任边界。
- 建立输入、输出、状态、错误和验证契约。
- 检查还有哪些关键约束没有确定。
- 通过少量高价值问题继续收敛任务。
- 生成后续 Codex 可以直接阅读执行的 `.md` 地基文档。
- 在本地记录使用偏好，逐步更贴合个人习惯。

## 适合什么时候用

适合这些场景：

1. 只有一个想法，还不知道怎么开始。
2. 想先规划，不想直接写代码。
3. 要做一个新项目，需要先划清第一版边界。
4. 要把需求交给 Codex、VS Code Codex、Cursor、Claude Code 或其他编程助手继续实现。
5. 想避免 vibe coding 时越做越大、功能失控。
6. 要设计付费解锁、实时联机、内部工具、数据处理、系统对接等功能。
7. 要生成一份可以跨会话、跨工具继续执行的交接文档。

示例：

```text
使用 $task-grounder，帮我规划一个 Excel 对账工具，先提问约束边界，再生成可执行地基文档。
```

```text
使用 $task-grounder，把这个软件想法拆成第一版范围、模块契约和分阶段计划，先不要写代码。
```

```text
使用 task-grounder，检查这个项目开始编码前还有哪些地方没约束到。
```

## 会产出什么

它可以产出一份 Markdown 地基文档，通常包含：

- 目标与非目标
- 假设与待确认问题
- 约束覆盖表
- 用户角色与核心流程
- 第一版最小可用边界
- 模块与责任边界拆分
- 数据实体与状态流转
- API / UI / CLI 契约
- 登录、支付、权限、安全约束
- 分阶段迭代计划
- 验证门禁
- 风险清单
- 给后续 Codex 执行的提示词

## 安装

### 从本仓库安装

使用 Codex 的技能安装脚本：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo niuniuaxiang-ui/task-grounder-skill --path skills/task-grounder
```

Windows PowerShell 示例：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo niuniuaxiang-ui/task-grounder-skill --path skills/task-grounder
```

安装后重启 Codex，让新技能生效。

### 手动安装

复制这个文件夹：

```text
skills/task-grounder
```

到本地 Codex 技能目录：

```text
~/.codex/skills/task-grounder
```

Windows 通常是：

```text
%USERPROFILE%\.codex\skills\task-grounder
```

## 仓库结构

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

## 关键文件

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 技能触发说明和主工作流 |
| `agents/openai.yaml` | Codex 界面展示信息 |
| `references/constraint-checklist.md` | 检查范围、owner、数据、接口、支付、权限、交付等约束是否完整 |
| `references/grounding-template.md` | 地基文档模板 |
| `references/user-profile.md` | 默认用户偏好档案，安装后可自行修改 |
| `references/user-agent-constitution.md` | 通用工作规范参考 |
| `references/usage-log.example.md` | 本地使用记录模板 |
| `scripts/record_usage.py` | 追加本地使用记录的脚本 |

## 个性化

安装后可以修改：

```text
references/user-profile.md
```

可以在里面记录稳定偏好，例如：

- 回复语言
- 常用技术栈
- 规划风格
- 验证要求
- 文件组织规则
- 前端或后端偏好

技能也可以把关键使用记录写入本地文件：

```text
references/usage-log.local.md
```

这个文件不会随仓库发布，也不应该提交到 GitHub。

## 隐私与安全

不要记录或发布：

- API key
- token
- 密码
- 支付凭据
- 客户数据
- 生产系统数据
- 私有业务信息

`record_usage.py` 会过滤明显的敏感关键词，但使用者仍然需要自己避免把密钥或隐私写进技能文件和 Git 历史。

## 准备度门槛

这个技能使用一个实用的“95% 准备度”门槛。

它不是数学保证，而是工程判断：任务已经被约束到足以进入实现，后续 Codex 不容易明显跑偏。

进入实现前应尽量明确：

- 目标清楚。
- 非目标清楚。
- 责任边界已定义。
- 模块契约已写清。
- 数据和状态已描述。
- 第一阶段范围已限定。
- 验证方式已确定。
- 剩余未知项已分为阻断、可假设或可后置。

如果准备度不够，技能应继续提出聚焦问题，而不是直接开始写代码。

## 示例场景

| 场景 | 技能重点约束什么 |
|---|---|
| Excel 对账工具 | 输入文件、匹配主键、差异规则、导出格式、验证样例 |
| 生产日报工具 | 数据来源、统计规则、报表样式、错误状态 |
| 付费解锁流程 | 支付方式、人工审核或官方回调、授权状态、安全边界 |
| 实时协作工具 | 房间模型、WebSocket 事件、重连机制、状态归属 |
| 内部管理工具 | 角色、权限、审计日志、数据生命周期、部署边界 |
| AI 辅助流程 | 提示词边界、用户输入契约、模型输出验证、失败兜底 |

## 验证

运行技能校验：

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/task-grounder
```

Windows PowerShell：

```powershell
$env:PYTHONUTF8='1'
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skills\task-grounder"
```

期望输出：

```text
Skill is valid!
```

## 更新建议

推荐流程：

1. 修改 `SKILL.md` 调整核心行为。
2. 修改 `references/` 里的模板或检查清单。
3. 保持 `SKILL.md` 简洁，长内容放进引用文件。
4. 运行校验。
5. 用真实规划任务测试。
6. 不要提交 `usage-log.local.md` 或任何隐私数据。

## 二次修改注意

如果你 fork 这个技能：

- 用自己的偏好替换 `references/user-profile.md`。
- 只在本地保留 `usage-log.local.md`。
- 保持可安装路径为 `skills/task-grounder`。
- 确保 `SKILL.md` 开头是合法 YAML frontmatter：

```md
---
name: task-grounder
description: ...
---
```
