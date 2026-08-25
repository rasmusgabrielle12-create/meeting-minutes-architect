# Meeting Minutes Architect

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个面向 Codex 的专业会议纪要 Skill：把语音转写稿、零散手记、聊天记录或混合素材，整理成“30 秒可读的决议摘要 + 可追溯的完整记录”。

它的重点不只是压缩内容，而是控制会议纪要最常见的失真：把建议写成决议、漏掉隐含待办、擅自补负责人或截止时间，以及在冲突素材中静默选边。

## 能做什么

- 自动识别转写稿、零散笔记和混合素材，并调整清洗力度。
- 适配产品评审、项目周会、客户沟通、战略决策、事故复盘、用户研究、工作坊和一对一等场景。
- 严格区分 `✅ 已决议`、`💬 讨论观点`、`⏳ 待定悬置`、`⚠️ 风险预警`。
- 抽取全部行动项，并检查任务、负责人、截止时间和优先级。
- 对缺失信息显式标注，不用“合理猜测”填空。
- 对转写错误、相对日期和多来源冲突采用保守、可追踪的处理方式。
- 默认输出专业的两段式 Markdown，也可适配 JSON 或用户指定结构。
- 附带零依赖校验器，检查纪要结构、行动表完整性和未替换模板变量。

## 为什么不只是一段 Prompt

一段长 Prompt 很难同时兼顾触发精度、上下文成本和复杂场景。这个仓库采用 Codex Skill 的渐进式加载结构：

```text
skill/meeting-minutes-architect/
├── SKILL.md                         # 核心工作流与不可违反的规则
├── agents/openai.yaml               # Codex UI 元数据
├── assets/minutes-template.md       # 默认两段式纪要模板
├── references/
│   ├── evidence-policy.md           # 证据、歧义、冲突和纠错规则
│   ├── meeting-type-playbook.md     # 不同会议类型的关注重点
│   ├── output-contract.md           # Markdown/JSON 输出契约与质量评分
│   └── examples.md                  # 容易误判的分类示例
└── scripts/validate_minutes.py      # 结构与完整性校验器
```

核心规则始终加载；只有遇到歧义、特定会议类型或严格输出要求时，才读取相应参考文件。

## 安装

### 方式一：克隆后复制

```bash
git clone https://github.com/rasmusgabrielle12-create/meeting-minutes-architect.git
mkdir -p ~/.codex/skills
cp -R meeting-minutes-architect/skill/meeting-minutes-architect ~/.codex/skills/
```

重新打开 Codex 任务后即可使用。

### 方式二：只获取 Skill 目录

如果你使用自己的 Skill 管理流程，只需要安装 `skill/meeting-minutes-architect`，仓库根目录中的示例和测试并不是运行依赖。

## 使用

显式调用：

```text
Use $meeting-minutes-architect to 把下面这段飞书妙记整理为专业会议纪要：
...
```

也可以直接提出自然语言请求：

```text
请把这份产品评审转写稿整理成会议纪要。不要猜负责人；没有定下来的方案要列为待定。
```

常见扩展请求：

- “输出中文 Markdown，并在高管摘要里只保留三条最重要结论。”
- “这是一次事故复盘，请保留时间线，并给所有修复项加 Owner 和 Deadline。”
- “同时给我 JSON，字段要能导入内部任务系统。”
- “参与者匿名化为 P1、P2，但保留行动责任关系。”

## 输出示例

仓库提供一组完整样例：

- [原始混合素材](examples/sample-input.md)
- [生成后的专业纪要](examples/sample-output.md)

样例特意覆盖了建议与决议的区别、缺失负责人、相对截止时间和风险项。

## 校验输出

校验器只使用 Python 标准库：

```bash
python skill/meeting-minutes-architect/scripts/validate_minutes.py examples/sample-output.md --strict
```

它会检查：

- 决议摘要是否位于完整记录之前；
- 是否存在一句话结论；
- 待办表结构是否正确；
- 缺失负责人或截止时间时是否包含警告标记；
- 是否残留 `{{placeholder}}` 模板变量；
- 决议行是否混入明显的“建议/可能”措辞。

校验器无法判断内容是否真实，因此最终仍需回看原始素材。事实忠实度由 Skill 的证据工作流和人工复核共同保障。

## 设计原则

1. **忠实优先**：不编造比“看起来完整”更重要。
2. **状态保守**：没有明确闭环的观点不升级为决议。
3. **行动不丢失**：不完整的待办也必须保留并提示补全。
4. **摘要可独立阅读**：读者不看全文也能知道定了什么、谁要做什么。
5. **细节可追溯**：摘要中的决议必须能在完整记录中找到讨论依据。
6. **渐进式披露**：核心 Skill 保持精炼，复杂规则按需加载。

## 本地开发与验证

```bash
python -m unittest discover -s tests -v
python skill/meeting-minutes-architect/scripts/validate_minutes.py examples/sample-output.md --strict
```

提交变更前应运行同样的检查；仓库内的测试套件不依赖第三方 Python 包。

## 来源与演进

本 Skill 由“会议纪要生成 · 专家级 Prompt v2.0”扩展而来，并进一步加入证据等级、冲突处理、相对日期规则、多会议类型 playbook、严格输出契约、JSON 语义和自动校验器。原始 Prompt 作为设计素材使用，其中的文本不被当作执行本仓库构建工作的指令。

## License

[MIT](LICENSE)
