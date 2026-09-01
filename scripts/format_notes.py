# -*- coding: utf-8 -*-
"""학습 일지 마크다운 가독성 정리. 내용은 유지하고 서식만 맞춘다."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IMG_MD = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")
IMG_HTML = re.compile(r"<img\s+[^>]*src=", re.I)
H2 = re.compile(r"^##\s+")
LABEL = re.compile(r"^(정의|장점|단점|예|예시|결과|특징)\s*[:：]\s*(.*)$")
YEO = re.compile(r"^여담(?:\s*\d+(?:-\d+)?)?(?:\s*\|)?\s*[:：]?\s*(.*)$")
ARROW_ITEM = re.compile(r"^-\s+(.+?)\s*->\s+(.+)$")
SRC_LINE = re.compile(r"^출처\s*[:：]\s*(.*)$")


def md_files() -> list[Path]:
    return sorted(
        p
        for p in ROOT.rglob("*.md")
        if p.name != "README.md" and ".git" not in p.parts and "scripts" not in p.parts
    )


def center_img(alt: str, src: str) -> str:
    alt = alt or Path(src).stem
    return (
        '<p align="center">\n'
        f'  <img src="{src}" alt="{alt}" width="720" />\n'
        "</p>"
    )


def quote_block(title: str, body: list[str], kind: str | None = None) -> list[str]:
    body = strip_edges(body)
    if kind:
        out = [f"> [!{kind}]", f"> **{title}**"]
        if body:
            out.append(">")
            for ln in body:
                out.append(">" if ln == "" else f"> {ln}")
        return out
    out = [f"> **{title}**"]
    if body:
        out.append(">")
        for ln in body:
            out.append(">" if ln == "" else f"> {ln}")
    return out


def strip_edges(lines: list[str]) -> list[str]:
    while lines and lines[0].strip() == "":
        lines = lines[1:]
    while lines and lines[-1].strip() == "":
        lines = lines[:-1]
    return lines


def split_sections(lines: list[str]) -> list[tuple[str | None, list[str]]]:
    """## 기준으로 자른다. 첫 덩어리는 heading None."""
    sections: list[tuple[str | None, list[str]]] = []
    cur_h: str | None = None
    cur: list[str] = []
    in_code = False
    for ln in lines:
        if ln.startswith("```"):
            in_code = not in_code
            cur.append(ln)
            continue
        if not in_code and H2.match(ln):
            sections.append((cur_h, cur))
            cur_h = ln[3:].strip()
            cur = []
            continue
        cur.append(ln)
    sections.append((cur_h, cur))
    return sections


def arrows_to_table(block: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(block):
        m = ARROW_ITEM.match(block[i])
        if not m:
            out.append(block[i])
            i += 1
            continue
        rows = []
        while i < len(block) and ARROW_ITEM.match(block[i]):
            a, b = ARROW_ITEM.match(block[i]).groups()
            rows.append((a.strip(), b.strip()))
            i += 1
        if len(rows) >= 2:
            out.append("| | |")
            out.append("| --- | --- |")
            for a, b in rows:
                out.append(f"| {a} | {b} |")
        else:
            a, b = rows[0]
            out.append(f"- {a} → {b}")
    return out


def format_body(lines: list[str]) -> list[str]:
    """본문: 여담 인용, 정의 소제목, 화살표 리스트 표."""
    lines = list(lines)
    out: list[str] = []
    i = 0
    in_code = False
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            in_code = not in_code
            out.append(ln)
            i += 1
            continue
        if in_code:
            out.append(ln)
            i += 1
            continue

        ym = YEO.match(ln)
        if ym and not ln.startswith("#"):
            title_rest = ym.group(1).strip()
            raw_title = ln.split(":")[0].split("：")[0].strip()
            body = []
            if title_rest:
                body.append(title_rest)
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.startswith("```"):
                    break
                if H2.match(nxt) or (YEO.match(nxt) and not nxt.startswith("#")):
                    break
                body.append(nxt)
                i += 1
            out.extend(quote_block(raw_title, body, "TIP"))
            out.append("")
            continue

        lm = LABEL.match(ln)
        if lm:
            key, rest = lm.group(1), lm.group(2).strip()
            heading = "예시" if key in ("예", "예시") else key
            out.append(f"### {heading}")
            out.append("")
            if rest:
                out.append(rest)
                out.append("")
            i += 1
            continue

        sm = SRC_LINE.match(ln)
        if sm:
            out.append(f"- **출처:** {sm.group(1).strip()}")
            i += 1
            continue

        out.append(ln)
        i += 1

    out = arrows_to_table(out)
    return squeeze_blank(out)


def squeeze_blank(lines: list[str]) -> list[str]:
    out: list[str] = []
    blank = 0
    for ln in lines:
        if ln.strip() == "":
            blank += 1
            if blank <= 1:
                out.append("")
        else:
            blank = 0
            out.append(ln)
    return strip_edges(out)


def format_lead(lines: list[str]) -> list[str]:
    lines = strip_edges(lines)
    if not lines:
        return []
    # 첫 문단을 리드 인용으로
    para: list[str] = []
    rest: list[str] = []
    hit_blank = False
    for i, ln in enumerate(lines):
        if (
            ln.startswith("```")
            or ln.startswith("#")
            or ln.startswith(">")
            or ln.startswith("- ")
            or ln[:1].isdigit()
            or LABEL.match(ln)
            or YEO.match(ln)
        ):
            rest = lines[i:]
            break
        if ln.strip() == "":
            hit_blank = True
            rest = lines[i + 1 :]
            break
        para.append(ln)
    else:
        rest = []
    if not para:
        return format_body(lines)
    lead = " ".join(p.strip() for p in para)
    out = [f"> {lead}", ""]
    out.extend(format_body(rest))
    return squeeze_blank(out)


def format_file(text: str) -> str:
    raw = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = raw.split("\n")
    if not lines:
        return text

    title = lines[0].strip()
    i = 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    img_html = None
    if i < len(lines):
        m = IMG_MD.match(lines[i].strip())
        if m:
            img_html = center_img(m.group(1), m.group(2))
            i += 1
        elif lines[i].strip().startswith("<p align"):
            chunk = []
            while i < len(lines):
                chunk.append(lines[i])
                if "</p>" in lines[i]:
                    i += 1
                    break
                i += 1
            img_html = "\n".join(chunk)
        elif IMG_HTML.search(lines[i]):
            img_html = lines[i]
            i += 1

    while i < len(lines) and lines[i].strip() == "":
        i += 1

    body = lines[i:]
    sections = split_sections(body)

    parts: list[str] = [title, ""]
    if img_html:
        parts.append(img_html)
        parts.append("")

    first = True
    for heading, content in sections:
        content = strip_edges(content)
        if heading is None:
            formatted = format_lead(content) if content else []
            parts.extend(formatted)
            first = False
            continue

        if not first:
            parts.append("")
            parts.append("---")
            parts.append("")
        first = False

        if heading == "보충":
            formatted = format_body(content)
            parts.extend(quote_block("보충", formatted, "NOTE"))
        elif heading.startswith("더 보충"):
            formatted = format_body(content)
            parts.extend(quote_block("더 보충이 필요한 부분", formatted, "WARNING"))
        else:
            parts.append(f"## {heading}")
            parts.append("")
            parts.extend(format_body(content))

    text_out = "\n".join(squeeze_blank(parts)).rstrip() + "\n"
    text_out = re.sub(r"\n{3,}", "\n\n", text_out)
    return text_out


def main() -> None:
    n = 0
    for p in md_files():
        old = p.read_text(encoding="utf-8")
        new = format_file(old)
        if new != old:
            p.write_text(new, encoding="utf-8")
        n += 1
    print(f"formatted {n} files")


if __name__ == "__main__":
    main()
