#!/usr/bin/env python3
"""Replace inline <style> blocks in lesson HTML with centralized CSS links."""

from __future__ import annotations

import re
from pathlib import Path

WEB = Path(__file__).resolve().parent.parent / "web"

STYLE_BLOCK = re.compile(r"\s*<style>.*?</style>\s*", re.DOTALL)

KATEX_LINKS = """  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" />
"""

CSS_LINK_TEMPLATE = """  <link rel="stylesheet" href="{prefix}assets/css/tokens.css" />
  <link rel="stylesheet" href="{prefix}assets/css/lesson.css" />
{extra}"""


def assets_prefix(path: Path) -> str:
    rel = path.relative_to(WEB)
    depth = len(rel.parts) - 1
    return "../" * depth


def extra_theme(path: Path) -> str:
    rel = path.as_posix()
    if "/s2/" in rel or rel.startswith("concepts/"):
        prefix = assets_prefix(path)
        return f'  <link rel="stylesheet" href="{prefix}assets/css/lesson-s2.css" />\n'
    return ""


def migrate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "<style>" not in text:
        if 'href="note.css"' in text:
            prefix = assets_prefix(path)
            new = text.replace('href="note.css"', f'href="{prefix}assets/css/lesson.css"')
            if new != text:
                path.write_text(new, encoding="utf-8")
                return True
        return False

    prefix = assets_prefix(path)
    extra = extra_theme(path)
    css_links = CSS_LINK_TEMPLATE.format(prefix=prefix, extra=extra)

    new_text, count = STYLE_BLOCK.subn("\n" + css_links, text, count=1)
    if count == 0:
        return False

    if "katex.min.css" not in new_text:
        new_text = new_text.replace(
            '<link href="https://fonts.googleapis.com',
            KATEX_LINKS + '  <link href="https://fonts.googleapis.com',
            1,
        )

    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    skip = {"index.html", "about.html"}
    changed = 0
    for path in sorted(WEB.rglob("*.html")):
        if path.name in skip:
            continue
        if migrate_file(path):
            changed += 1
            print(f"  updated {path.relative_to(WEB)}")
    print(f"\nDone — {changed} file(s) updated.")


if __name__ == "__main__":
    main()
