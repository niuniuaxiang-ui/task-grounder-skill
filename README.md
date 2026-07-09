# Task Grounder Skill

`task-grounder` 是一个面向 Codex 的规划约束型 skill，用来把模糊的软件想法、vibe coding 需求、功能改造或项目雏形，逐步收敛成可执行的项目地基文档。

它的目标不是马上写代码，而是先把任务边界、模块 owner、数据契约、接口契约、验证方式和迭代顺序划清楚，降低后续实现跑偏的概率。

## 适合什么时候用

适合这些场景：

1. 你只有一个模糊想法，不知道下一步怎么做。
2. 你想先生成计划，不想直接开写代码。
3. 你要做一个新项目，需要先划 MVP 边界。
4. 你要把需求交给 Codex、VS Code Codex、Cursor 或 Claude Code 继续实现。
5. 你希望 AI 通过持续提问帮你约束任务，而不是一上来堆功能。
6. 你需要模块拆分、接口契约、数据状态、验证门禁和风险清单。
7. 你希望 skill 根据使用记录逐步贴合你的工作习惯。

典型输入：

```text
使用 $task-grounder，帮我把“U9/MES Excel 对账工具”规划成可执行地基文档，先不要写代码。
```

```text
使用 task-grounder，通过提问帮我划定项目边界、模块契约和下一步计划。
```

```text
使用 $task-grounder，先检查我这个软件想法有哪些地方没有约束到。
```

## 它会产出什么

默认产出一份 Markdown 地基文档，内容包括：

- 项目目标与非目标
- 当前真源与假设
- 约束覆盖表
- 用户角色与核心场景
- MVP 边界
- 模块 owner 拆分
- 数据实体与状态机
- API / UI / CLI 契约
- 支付、账号、权限、安全约束
- 分阶段迭代计划
- 验证命令或验收证据
- 风险清单
- 待确认问题
- 给 Codex 继续实现的执行提示词

## 核心原则

| 原则 | 含义 |
|---|---|
| 先约束，后编码 | 任务没收敛前不急着实现 |
| 先 owner，后模块 | 先确定谁拥有业务真相，再拆实现 |
| 先契约，后接口 | 输入、输出、错误和状态先说清 |
| 先 MVP，后扩展 | 第一版只做最小闭环 |
| 先验收，后完成 | 每阶段必须有验证证据 |
| 先记录，后迭代 | 使用偏好通过本地日志逐步沉淀 |

## 安装

### 从 GitHub 安装

把下面命令里的 `<owner>/<repo>` 换成实际仓库地址：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo <owner>/<repo> --path skills/task-grounder
```

Windows 示例：

```powershell
python C:\Users\Tang\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py --repo <owner>/<repo> --path skills/task-grounder
```

安装后重启 Codex，让新 skill 生效。

### 手动安装

把 `skills/task-grounder` 文件夹复制到：

```text
~/.codex/skills/task-grounder
```

Windows 默认路径通常是：

```text
C:\Users\<你的用户名>\.codex\skills\task-grounder
```

## 使用方式

明确点名即可：

```text
使用 $task-grounder，帮我规划一个 Excel 自动清洗收费工具，先不断提问约束边界，最后输出可执行 .md 文档。
```

如果你只想让它检查缺口：

```text
使用 task-grounder，检查这个项目想法还有哪些关键约束没确定。
```

如果你要交给另一个 Codex 继续编码：

```text
使用 task-grounder，生成一份给 VS Code Codex 继续执行的地基文档和交接提示词。
```

## 工作流

```text
用户想法
  -> 任务类型识别
  -> 真源审计
  -> 约束检查
  -> 最多 3 个关键问题
  -> MVP 边界
  -> 模块 owner
  -> 数据/接口契约
  -> 分阶段迭代计划
  -> 验证门禁
  -> 地基文档
  -> 使用习惯记录
```

## 目录结构

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

## 关键文件说明

| 文件 | 作用 |
|---|---|
| `SKILL.md` | skill 触发描述和主工作流 |
| `constraint-checklist.md` | 检查目标、非目标、owner、数据、接口、支付、权限、工程交付等是否约束到 |
| `grounding-template.md` | 最终地基文档模板 |
| `user-profile.md` | 用户稳定偏好档案 |
| `user-agent-constitution.md` | 用户的通用 Agent 工作规范 |
| `usage-log.example.md` | 使用记录模板 |
| `record_usage.py` | 追加使用记录的脚本 |

## 使用习惯如何持续迭代

skill 会优先把每次关键使用记录写入本地文件：

```text
references/usage-log.local.md
```

这个文件不会随仓库发布，也不应该提交到 GitHub。

记录内容包括：

- 用户目标
- 关键约束
- 默认假设
- 用户纠正或新增偏好
- 下次应调整的地方

当某个偏好被用户明确表达，或在多次使用中重复出现时，再更新：

```text
references/user-profile.md
```

这样它会逐步更贴合个人习惯。

## 隐私与安全边界

不要记录：

- API key
- token
- 密码
- 支付凭据
- 客户隐私
- 生产敏感数据

`record_usage.py` 会对明显包含 `token`、`secret`、`password`、`密钥` 等关键词的内容做省略处理，但不要依赖脚本替你做全部安全判断。

## 95% readiness 的含义

这里的 95% 不是数学保证，而是一个工程门槛：

只有当以下内容基本明确时，才建议进入实现：

- 目标与非目标
- owner 边界
- 模块职责
- 输入输出契约
- 数据状态
- 权限和安全约束
- 第一阶段文件范围
- 验证命令或证据
- 剩余未知项是否阻断

如果这些没闭合，skill 会继续提问，而不是直接编码。

## 示例：适合规划的项目

| 项目 | task-grounder 会重点约束 |
|---|---|
| U9/MES Excel 对账工具 | 数据源、对账主键、差异分类、导出格式、验证样例 |
| Excel 自动清洗工具 | 模板、字段映射、错误报告、批量处理边界 |
| 生产日报生成器 | 输入口径、统计规则、报表格式、异常分类 |
| 付费解锁小工具 | 支付方式、人工审核/官方回调、授权状态、风控 |
| 实时联机工具 | 房间模型、WebSocket 消息契约、状态同步和断线恢复 |

## 验证

创建或修改 skill 后可运行：

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/task-grounder
```

Windows 示例：

```powershell
$env:PYTHONUTF8='1'
python C:\Users\Tang\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\codex-workshop\task-grounder-skill\skills\task-grounder
```

期望输出：

```text
Skill is valid!
```

## 发布注意

本仓库刻意不包含真实 `usage-log.local.md`。如果你 fork 或二次发布，请不要提交个人使用记录、客户信息、生产系统信息或密钥。

