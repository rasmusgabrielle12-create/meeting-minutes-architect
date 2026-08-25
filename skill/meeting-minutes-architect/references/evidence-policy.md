# Evidence, ambiguity, and correction policy

Use this reference when source quality is poor or when a classification could change accountability.

## 1. Evidence hierarchy

Prefer evidence in this order when multiple source fragments conflict:

1. An explicit closing statement that names the chosen option or commitment.
2. A direct assignment accepted by the assignee.
3. A contemporaneous written note clearly labeled as a decision or action.
4. A participant proposal or recollection.
5. Contextual inference.

Higher-ranked evidence does not automatically erase a conflict. If the sources appear to describe different versions or different moments, preserve both and mark the issue pending.

## 2. Decision threshold

Classify an item as `✅ 已决议` only when the source contains a clear closure signal, for example:

- “就按 A 方案执行。”
- “大家同意周五上线。”
- “最终决定先关闭这个入口。”
- “Approved. Ship option B.”
- “Let's lock this and move forward.”

Do not classify these as decisions without further closure:

- “我倾向于 A。”
- “要不试试 B？”
- “看起来周五也许可以。”
- “The team should probably...”
- silence after a proposal

If a chair or decision owner clearly summarizes the outcome, treat that as closure even if the exact word “决定” is absent.

## 3. Action threshold

Create an action item when a statement includes or strongly implies future work. Common signals include:

- first-person commitment: “我来整理”“I'll send it”
- imperative assignment: “小王周三前补数据”
- agreed team task: “研发这周完成评估”
- follow-up dependency: “等法务确认后更新合同”

Separate compound actions when they have different owners, deadlines, or acceptance criteria. Keep them together when they form one deliverable owned and completed as a unit.

### Owner rules

- Use the named person or team exactly as supported.
- Resolve pronouns only when the active speaker is reliably identified.
- Do not infer an owner merely because a participant normally holds the relevant role.
- Use `（素材未提及）` when missing.

### Deadline rules

- Preserve exact dates when present.
- Preserve relative dates exactly if the meeting date is unknown: `下周三（会议日期未知，无法换算）`.
- Convert a relative date to an absolute date only when the meeting date and locale make it unambiguous. Optionally retain the original phrase.
- Do not turn “尽快” into a calendar deadline. Record `尽快（未给出明确日期）` and flag it.

### Priority rules

- Use an explicitly stated priority.
- Infer priority only from an unambiguous urgency signal such as a release blocker, and label it `高（根据阻塞关系推断）`.
- Otherwise use `（素材未提及）`; do not assign “中” as a silent default.

## 4. Transcription corrections

Apply a correction silently only when confidence is very high and meaning is not controversial, such as a repeated product name that is spelled correctly elsewhere in the same source.

Show uncertain corrections when they affect:

- people or organizations
- product, project, or technical names
- numbers, units, currencies, and percentages
- dates and deadlines
- contractual or compliance language

Format: `候选词（原文：疑似转写词）`. If more than one correction is plausible, leave the original text and mark the item pending confirmation.

## 5. Inference boundary

Permitted inference:

- likely meeting type, clearly labeled as inferred
- grammatical expansion of shorthand
- grouping related statements under a neutral topic title
- obvious deduplication

Forbidden inference:

- unstated decision, rationale, owner, deadline, attendee, metric, or result
- emotional judgment or speaker intention
- causal claims not present in the source
- replacing disagreement with artificial consensus

## 6. Conflict reporting

Use this compact structure:

```markdown
- ⏳ 待确认：上线日期存在冲突。
  - 来源 A：9 月 3 日
  - 来源 B：9 月 5 日
  - 需确认：最终上线日期及确认人
```

Do not choose the more plausible value unless the user explicitly asks for a best-effort interpretation; even then, retain the conflict and confidence level.

## 7. Traceability

For ordinary minutes, topic-level traceability is sufficient: every summary decision must reappear under the relevant detailed topic with its discussion basis.

For regulated, legal, incident, or audit-sensitive meetings, add source pointers when available, such as timestamps, speaker labels, page numbers, or note IDs. Never fabricate a pointer.
