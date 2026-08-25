# Output contract

Use this reference for strict Markdown, integrations, or JSON output.

## Markdown contract

The default deliverable has exactly two top-level sections:

1. `## 📋 决议摘要` or `## 📋 Decision Summary`
2. `## 📝 完整记录` or `## 📝 Detailed Record`

The decision summary contains:

- meeting topic, type, date, and attendees
- one-sentence outcome
- confirmed decisions
- action table
- pending items and risks

The action table uses these columns:

| # | 任务 / Action | 负责人 / Owner | 截止时间 / Deadline | 优先级 / Priority |
|---|---|---|---|---|

Use explicit missing markers. Do not leave cells blank. In Owner and Deadline cells, use `（素材未提及）⚠️` / `(not stated in source) ⚠️` when absent. Append `⚠️` to tentative, disputed, or non-committed values and explain the uncertainty in the same cell or in the pending section.

The detailed record contains one subsection per topic. Each subsection may contain only the applicable state lines:

- `💬 讨论 / Discussed`
- `✅ 决议 / Decided`
- `📌 待办 / Action`
- `⏳ 待定 / Pending`
- `⚠️ 风险 / Risk`

Do not add an empty state line merely to satisfy the template.

## One-sentence outcome semantics

Summarize the highest-value meeting result. If no decision was made, say what the meeting clarified or what remains pending. Do not disguise “no decision” as a weak decision.

Examples:

- `确定采用分阶段发布方案，并在 9 月 3 日前完成灰度验证。`
- `评审了三个方案，但因成本数据缺失未形成最终决议。`

## JSON contract

When the user asks for JSON, use this logical shape unless another schema is supplied:

```json
{
  "metadata": {
    "topic": "string | null",
    "meeting_type": "string | null",
    "meeting_type_inferred": true,
    "date": "string | null",
    "attendees": ["string"]
  },
  "one_sentence_outcome": "string",
  "decisions": [
    {
      "id": "D1",
      "statement": "string",
      "rationale": "string | null",
      "topic_id": "T1",
      "source_pointer": "string | null"
    }
  ],
  "actions": [
    {
      "id": "A1",
      "task": "string",
      "owner": "string | null",
      "deadline": "string | null",
      "priority": "high | medium | low | null",
      "topic_id": "T1",
      "source_pointer": "string | null"
    }
  ],
  "pending": ["string"],
  "risks": ["string"],
  "topics": [
    {
      "id": "T1",
      "title": "string",
      "discussion": ["string"],
      "decision_ids": ["D1"],
      "action_ids": ["A1"],
      "pending": ["string"],
      "risks": ["string"]
    }
  ]
}
```

Use JSON `null` for missing scalar values. Do not substitute guessed strings. Ensure every `topic_id`, `decision_id`, and `action_id` resolves.

## Quality rubric

Score internally before delivery:

- Fidelity (0–4): all claims source-supported; states correctly separated.
- Action completeness (0–4): all actions captured; owners/deadlines explicit or flagged.
- Traceability (0–4): summary decisions map to detailed evidence.
- Compression (0–4): noise removed without losing meaningful content.
- Readability (0–4): standalone summary, scannable tables, parallel phrasing.

Do not deliver below 3 in any category. Fix the draft or disclose source limitations that prevent a higher score.
