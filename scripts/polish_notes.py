# -*- coding: utf-8 -*-
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPLIT = re.compile(r"(?<=[다요까음임함됨음])\.\s+")


def md_files():
    return [
        p
        for p in ROOT.rglob("*.md")
        if p.name != "README.md" and ".git" not in p.parts and "scripts" not in p.parts
    ]


def wrap_lead(text: str) -> list[str]:
    text = text.strip()
    parts = [p.strip() for p in SPLIT.split(text) if p.strip()]
    if len(parts) <= 1:
        return [f"> {text}"]
    lines = []
    for i, p in enumerate(parts):
        if i < len(parts) - 1 and not p.endswith((".", "?", "!", "다", "요")):
            p = p + "."
        if i:
            lines.append(">")
        lines.append(f"> {p}")
    return lines


def polish(text: str) -> str:
    text = text.replace("| | |\n| --- | --- |", "| 항목 | 설명 |\n| --- | --- |")
    lines = text.split("\n")
    out = []
    i = 0
    seen_img = False
    while i < len(lines):
        ln = lines[i]
        if ln.strip() == "</p>":
            seen_img = True
            out.append(ln)
            i += 1
            continue
        if (
            seen_img
            and ln.startswith("> ")
            and not ln.startswith("> [!")
            and not ln.startswith("> **")
            and len(ln) > 110
        ):
            out.extend(wrap_lead(ln[2:]))
            seen_img = False
            i += 1
            continue
        if ln.startswith("#") or ln.startswith("---") or ln.startswith("> [!"):
            seen_img = False
        out.append(ln)
        i += 1
    return "\n".join(out)


def main():
    for p in md_files():
        old = p.read_text(encoding="utf-8")
        new = polish(old)
        if new != old:
            p.write_text(new, encoding="utf-8")
    print("polished")


if __name__ == "__main__":
    main()
