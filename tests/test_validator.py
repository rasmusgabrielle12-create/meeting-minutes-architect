from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "skill/meeting-minutes-architect/scripts/validate_minutes.py"
SPEC = importlib.util.spec_from_file_location("validate_minutes", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    def test_sample_output_passes_strict_validation(self) -> None:
        sample = (ROOT / "examples/sample-output.md").read_text(encoding="utf-8")
        errors, warnings = VALIDATOR.validate(sample)
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_missing_sections_fail(self) -> None:
        errors, _ = VALIDATOR.validate("# Notes\nNothing decided.")
        self.assertGreaterEqual(len(errors), 3)

    def test_unresolved_placeholder_fails(self) -> None:
        text = """## 📋 决议摘要
**一句话结论**：{{outcome}}
未识别到明确待办
## 📝 完整记录
"""
        errors, _ = VALIDATOR.validate(text)
        self.assertTrue(any("placeholder" in error.lower() for error in errors))

    def test_missing_owner_requires_warning_marker(self) -> None:
        text = """## 📋 决议摘要
**一句话结论**：已完成讨论。
### 📌 待办行动
| # | 任务 | 负责人 | 截止时间 | 优先级 |
|---|---|---|---|---|
| 1 | 补充数据 | （素材未提及） | 明天 | 高 |
## 📝 完整记录
"""
        errors, warnings = VALIDATOR.validate(text)
        self.assertEqual([], errors)
        self.assertTrue(any("owner" in warning.lower() for warning in warnings))

    def test_tentative_deadline_requires_warning_marker(self) -> None:
        text = """## 📋 决议摘要
**一句话结论**：已完成讨论。
### 📌 待办行动
| # | 任务 | 负责人 | 截止时间 | 优先级 |
|---|---|---|---|---|
| 1 | 更新文档 | 许经理 | 9 月 1 日（待确认） | 中 |
## 📝 完整记录
"""
        errors, warnings = VALIDATOR.validate(text)
        self.assertEqual([], errors)
        self.assertTrue(any("deadline" in warning.lower() for warning in warnings))


if __name__ == "__main__":
    unittest.main()
