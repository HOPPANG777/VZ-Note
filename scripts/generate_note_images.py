# -*- coding: utf-8 -*-
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from diagram_draw import render, save  # noqa: E402
from diagram_specs import SPECS  # noqa: E402

IMG_ROOT = ROOT / "Images"


def md_files() -> list[Path]:
    skip = {"README.md"}
    return sorted(
        p for p in ROOT.rglob("*.md") if p.name not in skip and ".git" not in p.parts and "scripts" not in p.parts
    )


def rel_posix(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def embed(md: Path, img: Path) -> None:
    rel = Path(os_rel(md.parent, img)).as_posix()
    alt = md.stem
    tag = f"![{alt}]({rel})"
    text = md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        return
    out: list[str] = []
    i = 0
    out.append(lines[0])
    i = 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines) and lines[i].startswith("![") and "Images/" in lines[i].replace("\\", "/"):
        i += 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
    out.append("")
    out.append(tag)
    out.append("")
    rest = lines[i:]
    if rest:
        out.extend(rest)
    md.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def os_rel(start: Path, target: Path) -> str:
    return str(Path(os_path_rel(start, target)))


def os_path_rel(start: Path, target: Path) -> Path:
    import os

    return Path(os.path.relpath(target, start))


def main() -> None:
    missing = []
    made = 0
    for md in md_files():
        key = rel_posix(md)
        spec = SPECS.get(key)
        if spec is None:
            missing.append(key)
            continue
        kind, title, data = spec
        img_path = IMG_ROOT / Path(key).with_suffix(".png")
        img = render(kind, title, data)
        save(img, img_path)
        embed(md, img_path)
        made += 1
    print(f"generated {made} images")
    if missing:
        print("MISSING SPECS:")
        for m in missing:
            print(" ", m)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
