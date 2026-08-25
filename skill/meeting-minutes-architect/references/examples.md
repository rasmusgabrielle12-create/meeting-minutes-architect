# Classification examples

Use these examples to calibrate ambiguous source language. They are patterns, not content templates.

## Proposal versus decision

Source:

> 李明：我建议 10% 灰度开始，风险小一点。大家先想想，下次再定。

Correct:

- 💬 讨论：李明建议首轮采用 10% 灰度，以降低风险。
- ⏳ 待定：首轮灰度比例将在下次会议确定。

Incorrect:

- ✅ 决议：采用 10% 灰度发布。

## Incomplete action

Source:

> 会后把竞品数据补一下。

Correct action row:

| # | 任务 | 负责人 | 截止时间 | 优先级 |
|---|---|---|---|---|
| 1 | 补充竞品数据 | （素材未提及）⚠️ | （素材未提及）⚠️ | （素材未提及） |

Do not drop the task or invent an analyst as owner.

## Relative deadline

Source metadata: meeting date is not available.

Source:

> 王敏：我下周三把报价单发给客户。

Correct:

- Task: 向客户发送报价单
- Owner: 王敏
- Deadline: 下周三（会议日期未知，无法换算）

## Accepted assignment

Source:

> 主持人：周五前谁能把埋点清单过一遍？赵宇：我来，周四下午给大家。

Correct:

- ✅ Decided/assignment: 赵宇负责复核埋点清单。
- 📌 Action: 周四下午前提交复核后的埋点清单；Owner 赵宇.

The deadline is Thursday afternoon because the assignee made a more specific commitment than the original request.

## Contradictory sources

Transcript:

> 上线定在 9 月 3 日。

Handwritten note:

> 发布：9/5

Correct:

- ⏳ 待确认：上线日期存在冲突；转写稿为 9 月 3 日，手写笔记为 9 月 5 日。

Do not silently pick one date.

## No decision outcome

Source:

> 团队比较了自建和采购两条路径，财务数据下周才齐，今天先不定。

Correct one-sentence outcome:

> 比较了自建与采购两条路径，但因财务数据尚未齐备，本次未形成最终决议。

## Uncertain transcription correction

Source:

> 这个要同步给“法务部/发布部”（音近，无法确认）。

Correct:

- 📌 待办：向相关部门同步该事项；负责人和截止时间未提及。
- ⏳ 待确认：接收部门名称，原文疑似“法务部/发布部”。

Do not choose the department based on what seems more likely.
