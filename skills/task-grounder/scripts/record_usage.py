#!/usr/bin/env python3
"""追加一条安全的任务地基使用记录。"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


SENSITIVE_HINTS = (
    "api_key",
    "apikey",
    "token",
    "secret",
    "password",
    "passwd",
    "密钥",
    "令牌",
    "密码",
)


def clean(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return "无"
    lowered = text.lower()
    if any(hint in lowered for hint in SENSITIVE_HINTS):
        return "[已省略：疑似敏感信息]"
    return text.replace("\r\n", "\n").replace("\r", "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="追加一条任务地基使用记录。")
    parser.add_argument("--log", default=None, help="usage-log.local.md 路径")
    parser.add_argument("--task", required=True, help="任务简称")
    parser.add_argument("--goal", default="", help="用户目标")
    parser.add_argument("--constraints", default="", help="关键约束")
    parser.add_argument("--assumptions", default="", help="采用的默认假设")
    parser.add_argument("--preference", default="", help="新增或修正的用户偏好")
    parser.add_argument("--next-adjustment", default="", help="后续应如何调整")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    log_path = Path(args.log) if args.log else skill_root / "references" / "usage-log.local.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    entry = f"""
## {datetime.now().strftime("%Y-%m-%d")} - {clean(args.task)}

- 用户目标：{clean(args.goal)}
- 关键约束：{clean(args.constraints)}
- 采用的默认假设：{clean(args.assumptions)}
- 用户纠正/新增偏好：{clean(args.preference)}
- 下次应调整：{clean(args.next_adjustment)}
"""
    with log_path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(entry)
    print(f"已追加使用记录：{log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
