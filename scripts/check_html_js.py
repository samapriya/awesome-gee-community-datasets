"""Validate the inline JavaScript in a standalone HTML page.

Catches the class of bug that shipped a broken contributors.html: an
unescaped apostrophe inside a single-quoted string, e.g.

    'That's everyone'

which silently terminates the string and makes the WHOLE script fail to
parse — so nothing runs, the skeletons never clear, and the page just spins.

There is no JS runtime in this environment, so this is a lightweight scanner
rather than a real parser. It checks the two things that actually break:
unterminated string literals, and unbalanced delimiters.

Usage:
    python scripts/check_html_js.py contributors.html browse.html
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BACKSLASH = chr(92)
QUOTES = ('"', "'", "`")


# A '/' in one of these positions starts a regex literal, not division.
# Without this, a pattern like /[&<>"']/g reads as the start of a string and
# every check after it is nonsense.
REGEX_PRECEDERS = set("(,=:[!&|?{};+-*%~^") | {"return", "typeof", "case", "in", "of"}


def _starts_regex(js: str, i: int) -> bool:
    j = i - 1
    while j >= 0 and js[j] in " \t\n":
        j -= 1
    if j < 0:
        return True
    if js[j] in REGEX_PRECEDERS:
        return True
    word = re.search(r"[A-Za-z]+$", js[max(0, j - 9):j + 1])
    return bool(word and word.group() in REGEX_PRECEDERS)


def scan(js: str) -> list[str]:
    errs: list[str] = []
    i, line, n = 0, 1, len(js)

    while i < n:
        c = js[i]

        if c == "\n":
            line += 1
            i += 1
            continue

        # regex literal — consume it wholesale, including any quotes inside
        if c == "/" and i + 1 < n and js[i + 1] not in "/*" and _starts_regex(js, i):
            i += 1
            in_class = False
            while i < n and js[i] != "\n":
                if js[i] == BACKSLASH:
                    i += 2
                    continue
                if js[i] == "[":
                    in_class = True
                elif js[i] == "]":
                    in_class = False
                elif js[i] == "/" and not in_class:
                    i += 1
                    break
                i += 1
            continue

        # line comment
        if c == "/" and i + 1 < n and js[i + 1] == "/":
            while i < n and js[i] != "\n":
                i += 1
            continue

        # block comment
        if c == "/" and i + 1 < n and js[i + 1] == "*":
            i += 2
            while i + 1 < n and not (js[i] == "*" and js[i + 1] == "/"):
                if js[i] == "\n":
                    line += 1
                i += 1
            i += 2
            continue

        if c in QUOTES:
            quote, start = c, line
            i += 1
            closed = False
            while i < n:
                ch = js[i]
                if ch == BACKSLASH:
                    i += 2
                    continue
                if ch == "\n":
                    line += 1
                    if quote != "`":       # only template literals may span lines
                        break
                    i += 1
                    continue
                if ch == quote:
                    closed = True
                    i += 1
                    break
                i += 1
            if not closed:
                errs.append(
                    f"line {start}: unterminated {quote} string "
                    f"(likely an unescaped {quote} inside it)"
                )
            continue

        i += 1

    for open_c, close_c, name in (("{", "}", "braces"),
                                  ("(", ")", "parens"),
                                  ("[", "]", "brackets")):
        a, b = js.count(open_c), js.count(close_c)
        if a != b:
            errs.append(f"unbalanced {name}: {a} {open_c} vs {b} {close_c}")

    return errs


def main() -> int:
    paths = sys.argv[1:] or ["contributors.html"]
    failed = False

    for name in paths:
        p = Path(name)
        if not p.exists():
            print(f"{name}: not found")
            failed = True
            continue

        html = p.read_text(encoding="utf-8")
        blocks = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S)
        if not blocks:
            print(f"{name}: no inline script blocks")
            continue

        errs: list[str] = []
        for b in blocks:
            errs += scan(b)

        if errs:
            failed = True
            print(f"{name}: FAIL")
            for e in errs:
                print(f"   {e}")
        else:
            print(f"{name}: OK ({len(blocks)} inline block(s))")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
