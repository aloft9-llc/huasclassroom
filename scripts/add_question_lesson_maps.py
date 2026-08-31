#!/usr/bin/env python3
"""Inject Question–Lesson Map sections into unit test HTML and markdown notes."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TESTS = [
    {
        "html": "web/chapter2/unit-test-2.html",
        "md": "Notes/Chapter2/Unit_Test_2.md",
        "test_name": "Unit Test 2",
        "lesson_range": "Lessons 2.1–2.9",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Whole tens/hundreds × one-digit; two- and three-digit mental products; mixed × chains", ["2.1", "2.2", "2.4", "2.5", "2.6", "2.7", "2.8"]),
            ("2. Column method", "Written × for two- and three-digit × one-digit; regrouping; zeros in factors", ["2.4", "2.5", "2.6", "2.7", "2.8"]),
            ("3. Step by step", "Multi-step expressions with ×; friendly regrouping; distributive rewrites", ["2.4", "2.5", "2.6", "2.9"]),
            ("4. Compare", "Compare products with &gt;, &lt;, =; reason about nearby multiples", ["2.1", "2.2"]),
            ("5. Fill in the brackets", "Digit/place-value reasoning for products; estimate product size", ["2.4", "2.5", "2.6", "2.7", "2.8"]),
            ("6. Multiple choice", "Choose correct expression or estimate; interpret × stories", ["2.1", "2.2", "2.9"]),
            ("7. Number sentences", "Phrase → equation; unknown factor from quotient; product of equal addends", ["2.3", "2.9"]),
            ("8. Application problems", "Distance/speed, reading pages, flowers/groups, books/seats multi-step × stories", ["2.3", "2.9"]),
            ("9. Fill in the boxes", "Complete column × working; verify partial products", ["2.7", "2.8"]),
        ],
        "slugs": {
            "2.1": "2.1-whole-tens-hundreds-1",
            "2.2": "2.2-whole-tens-hundreds-2",
            "2.3": "2.3-read-pictures",
            "2.4": "2.4-two-digit-by-one-1",
            "2.5": "2.5-two-digit-by-one-2",
            "2.6": "2.6-two-digit-by-one-3",
            "2.7": "2.7-three-digit-by-one-1",
            "2.8": "2.8-three-digit-by-one-2",
            "2.9": "2.9-practice-and-exercise",
        },
    },
    {
        "html": "web/chapter3/unit-test-3.html",
        "md": "Notes/Chapter3/Unit_Test_3.md",
        "test_name": "Unit Test 3",
        "lesson_range": "Lessons 3.1–3.5",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "×÷ fluency review; order of operations (review from Chapters 1–2)", ["3.5"]),
            ("2. Column method", "Multi-digit +/− and × column review (review from Chapters 1–2)", ["3.5"]),
            ("3. Step by step", "Multi-step computation review alongside calendar unit", ["3.5"]),
            ("4. Fill in the spaces / calendars", "Common vs leap year; big/small months; read calendars; age/birthday on Feb 29", ["3.1", "3.2", "3.3", "3.4"]),
            ("5. True or false", "Leap-year rules; month-length facts; calendar reasoning", ["3.3"]),
            ("6. Multiple choice", "Max days in consecutive months; identify leap years", ["3.2", "3.3"]),
            ("7–14. Applications &amp; puzzles", "Weeks/days; reading pages; holiday spans; date-span sales; symbol equations; match scheduling", ["3.4", "3.5"]),
        ],
        "slugs": {
            "3.1": "3.1-year-month-day-1",
            "3.2": "3.2-year-month-day-2",
            "3.3": "3.3-common-leap-year",
            "3.4": "3.4-making-year-calendar",
            "3.5": "3.5-practice-and-exercise",
        },
    },
    {
        "html": "web/chapter4/unit-test-4.html",
        "md": "Notes/Chapter4/Unit_Test_4.md",
        "test_name": "Unit Test 4",
        "lesson_range": "Lessons 4.1–4.14",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Whole tens/hundreds ÷; mixed ×÷/+− chains; order of operations", ["4.1", "4.2"]),
            ("2. Column method", "Column ÷ with remainders; related × check", ["4.2", "4.7", "4.8", "4.9", "4.10"]),
            ("3. Step by step", "Regroup with ÷; distributive/friendly pairs in multi-step expressions", ["4.2", "4.3", "4.10", "4.14"]),
            ("4. Write the number sentences", "Phrase → equation; find dividend from divisor/quotient/remainder", ["4.2", "4.11"]),
            ("5. Fill in the brackets", "Division vocabulary; place of quotient; digit bounds; zeros in quotient; remainder cases", ["4.1", "4.4", "4.7", "4.10"]),
            ("6–12. Application problems", "Equal groups with remainder; books/notebooks; flowers per day; mass and money stories", ["4.11", "4.12", "4.13", "4.14"]),
            ("13–15. Enhancement", "Shopping combinations; missing-digit puzzle; partition a set into equal teams", ["4.14"]),
        ],
        "slugs": {
            "4.1": "4.1-dividing-whole-tens-hundreds",
            "4.2": "4.2-two-digit-by-one-1",
            "4.3": "4.3-two-digit-by-one-2",
            "4.4": "4.4-two-digit-by-one-3",
            "4.5": "4.5-two-digit-by-one-4",
            "4.6": "4.6-two-digit-by-one-5",
            "4.7": "4.7-three-digit-by-one-1",
            "4.8": "4.8-three-digit-by-one-2",
            "4.9": "4.9-three-digit-by-one-3",
            "4.10": "4.10-three-digit-by-one-4",
            "4.11": "4.11-application-of-division",
            "4.12": "4.12-unit-price-quantity-total-1",
            "4.13": "4.13-unit-price-quantity-total-2",
            "4.14": "4.14-practice-and-exercise",
        },
    },
    {
        "html": "web/chapter5/unit-test-5.html",
        "md": "Notes/Chapter5/Unit_Test_5.md",
        "test_name": "Unit Test 5",
        "lesson_range": "Lessons 5.1–5.9",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Warm-up +/−/×/÷ fluency at start of geometry chapter", ["5.1"]),
            ("2. Column method", "Column +/−/×/÷ review with geometry chapter", ["5.1"]),
            ("3. Step by step", "Multi-step computation review", ["5.1"]),
            ("4. Fill in the spaces", "Length units (km, m, cm, dm); area units; rectangle area; equilateral/regular; symmetry counts", ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.9"]),
            ("5. Triangles", "Classify acute/obtuse/right; identify isosceles", ["5.5"]),
            ("6. True or false", "Length/area unit facts; symmetry properties; triangle names", ["5.4", "5.5", "5.6"]),
            ("7. Multiple choice", "Choose correct unit, symmetry count, or area statement", ["5.1", "5.4", "5.7", "5.9"]),
            ("8–10. Area diagrams", "Find rectangle areas; identify isosceles pairs; shaded grid area", ["5.5", "5.6", "5.7", "5.8", "5.9"]),
            ("11. Application problems", "Paper rectangle; wall − windows; composite areas; unit conversion (cm², dm², m²)", ["5.7", "5.8", "5.9"]),
        ],
        "slugs": {
            "5.1": "5.1-knowing-kilometres",
            "5.2": "5.2-metres-and-centimetres",
            "5.3": "5.3-knowing-decimetres",
            "5.4": "5.4-line-symmetry",
            "5.5": "5.5-classification-of-triangles",
            "5.6": "5.6-areas",
            "5.7": "5.7-areas-rectangles-squares-1",
            "5.8": "5.8-areas-rectangles-squares-2",
            "5.9": "5.9-square-metres",
        },
    },
    {
        "html": "web/chapter6/unit-test-6.html",
        "md": "Notes/Chapter6/Unit_Test_6.md",
        "test_name": "Unit Test 6",
        "lesson_range": "Lessons 6.1–6.11",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Mixed ×÷/+−; brackets; mental fluency across prior chapters", ["6.1", "6.2"]),
            ("2. Column method", "Column +/−/×/÷ with remainders; check reasonableness", ["6.1", "6.2"]),
            ("3. Step by step", "Multi-step regrouping; large-number chains", ["6.2"]),
            ("4. Fill in the brackets", "Greatest/least difference with digits; compare expressions; units; pattern in a sequence", ["6.1", "6.2", "6.5", "6.10"]),
            ("5. Application problems", "Cuts vs pieces; corridor intervals; reading rate; pay and change stories", ["6.3", "6.4", "6.5", "6.9"]),
            ("6. Symmetry", "Complete the mirror half of a symmetric figure", ["6.6"]),
            ("7. Area", "Find area of a composite figure (cm²)", ["6.7", "6.8"]),
            ("8. Subtraction towers", "Follow flowchart/tower subtraction to top value", ["6.11"]),
        ],
        "slugs": {
            "6.1": "6.1-multiplication-and-division-1",
            "6.2": "6.2-multiplication-and-division-2",
            "6.3": "6.3-problem-solving-1",
            "6.4": "6.4-problem-solving-2",
            "6.5": "6.5-problem-solving-3",
            "6.6": "6.6-tessellations",
            "6.7": "6.7-how-large-are-they",
            "6.8": "6.8-xiao-pang-home-area",
            "6.9": "6.9-math-plaza-tree-planting",
            "6.10": "6.10-math-plaza-repeated-patterns",
            "6.11": "6.11-math-plaza-flowcharts",
        },
    },
    {
        "html": "web/s2/chapter1/unit-test-1.html",
        "md": "Notes/SecondSemester/Chapter1/Unit_Test_1.md",
        "test_name": "Unit Test 1",
        "lesson_range": "Lessons 1.1–1.6",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Warm-up ×÷ and mixed operations fluency (Part A)", ["1.1"]),
            ("2. Column method", "Four-operation column work with show-working (Part A)", ["1.1", "1.2"]),
            ("3. Step by step", "Order of operations; work inside parentheses first (Part A)", ["1.2"]),
            ("4. Fill in the spaces", "Brackets in expressions; unit choices; dm² ↔ cm² (Part A–B)", ["1.2", "1.4"]),
            ("5. Area", "Estimate on grid; combined-figure area by splitting rectangles (Part B)", ["1.3", "1.5"]),
            ("6. Application problems", "Multi-step stories using parentheses and area (Part C)", ["1.5", "1.6"]),
        ],
        "slugs": {
            "1.1": "1.1-warm-up-revision",
            "1.2": "1.2-four-operations-parentheses",
            "1.3": "1.3-estimating-area-1",
            "1.4": "1.4-square-decimetres",
            "1.5": "1.5-area-combined-figures",
            "1.6": "1.6-practice-and-exercise",
        },
    },
    {
        "html": "web/s2/chapter2/unit-test-2.html",
        "md": "Notes/SecondSemester/Chapter2/Unit_Test_2.md",
        "test_name": "Unit Test 2",
        "lesson_range": "Lessons 2.1–2.15",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Tens/hundreds × and ÷; speed-related mental products", ["2.1", "2.2", "2.3"]),
            ("2. Column method", "Two- and three-digit × two-digit; multi-digit ÷ two-digit with remainders", ["2.4", "2.5", "2.6", "2.7", "2.9", "2.13", "2.14"]),
            ("3. Step by step", "Multi-step ×÷ chains; distributive rewrites", ["2.4", "2.5", "2.15"]),
            ("4. Number sentences", "Find divisor from dividend/quotient/remainder language", ["2.8", "2.9"]),
            ("5. Shaded area", "Area of shaded region on a unit grid (cm²)", ["2.15"]),
            ("6. Fill in the brackets", "Zeros in products; digit bounds for quotients; marks in long division", ["2.4", "2.6", "2.10", "2.12"]),
            ("7. True or false", "Speed/distance reasoning; division with remainder facts", ["2.1", "2.11"]),
            ("8. Multiple choice", "Choose correct ×÷ statement, estimate, or speed comparison", ["2.1", "2.2", "2.9", "2.12"]),
            ("9. Application problems", "Eggs over days; mass totals; months to save; dual prices; square tiling with remainder", ["2.1", "2.2", "2.15"]),
            ("10. Compare", "Unit-price comparison; rank speeds (km/h)", ["2.1", "2.2"]),
        ],
        "slugs": {
            "2.1": "2.1-speed-time-distance-1",
            "2.2": "2.2-speed-time-distance-2",
            "2.3": "2.3-multiplying-whole-tens-two-digit",
            "2.4": "2.4-two-digit-by-two-digit-1",
            "2.5": "2.5-two-digit-by-two-digit-2",
            "2.6": "2.6-three-digit-by-two-digit-1",
            "2.7": "2.7-three-digit-by-two-digit-2",
            "2.8": "2.8-dividing-by-tens",
            "2.9": "2.9-dividing-by-two-digit-1",
            "2.10": "2.10-dividing-by-two-digit-2",
            "2.11": "2.11-dividing-by-two-digit-3",
            "2.12": "2.12-dividing-by-two-digit-4",
            "2.13": "2.13-dividing-multi-digit-1",
            "2.14": "2.14-dividing-multi-digit-2",
            "2.15": "2.15-practice-and-exercise",
        },
    },
    {
        "html": "web/s2/chapter3/unit-test-3.html",
        "md": "Notes/SecondSemester/Chapter3/Unit_Test_3.md",
        "test_name": "Unit Test 3",
        "lesson_range": "Lesson 3.1",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Mixed ops; ×÷ before +−; brackets first (fluency review)", ["3.1"]),
            ("2. Column method", "Column ×÷ with remainder check (fluency review)", ["3.1"]),
            ("3. Step by step", "Distributive/friendly-pair rewrites in multi-step expressions", ["3.1"]),
            ("4. Number sentences", "Dividend = divisor × quotient + remainder", ["3.1"]),
            ("5. Composite area", "Split L-shape into rectangles; sum areas (m²)", ["3.1"]),
            ("6. Fill in the spaces", "Sensible units; speed table; area conversions; Olympic bar chart; division digit bounds", ["3.1"]),
            ("7. Multiple choice", "Greatest remainder when dividing by 25; who skipped fastest", ["3.1"]),
            ("8. Application problems", "Packing with leftovers; boxes and parts; ship distance = speed × time + remaining", ["3.1"]),
            ("9. Let's do statistics", "Read scale; complete Saturday bar; fewest/most; weekly total; write observation", ["3.1"]),
        ],
        "slugs": {"3.1": "3.1-bar-chart-2"},
    },
    {
        "html": "web/s2/chapter4/unit-test-4.html",
        "md": "Notes/SecondSemester/Chapter4/Unit_Test_4.md",
        "test_name": "Unit Test 4",
        "lesson_range": "Lessons 4.1–4.5",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "×÷ fluency review alongside fraction unit", ["4.5"]),
            ("2. Column method", "Large × and ÷ column review", ["4.5"]),
            ("3. Step by step", "Multi-step computation review", ["4.5"]),
            ("4. Number sentences", "Write and evaluate division sentences from language", ["4.5"]),
            ("5. Fill in the spaces", "Unit fractions of length; colour parts; name fractions; compare fractions; fraction of a set", ["4.1", "4.2", "4.3", "4.4", "4.5"]),
            ("6. True or false", "Equal parts; unit vs non-unit fractions; comparing denominators", ["4.1", "4.2", "4.4"]),
            ("7. Multiple choice", "Choose shaded fraction; equivalent representations", ["4.2", "4.3", "4.4"]),
            ("8. Diagrams / circle", "Shade to show a fraction; circle a fraction of a set", ["4.2", "4.3", "4.4", "4.5"]),
            ("9. Application problems", "Date-span rate; equal groups; speed; boys/girls fraction of class; tangram piece fractions", ["4.4", "4.5"]),
        ],
        "slugs": {
            "4.1": "4.1-whole-and-part",
            "4.2": "4.2-unit-fractions-1",
            "4.3": "4.3-unit-fractions-2",
            "4.4": "4.4-non-unit-fractions-1",
            "4.5": "4.5-non-unit-fractions-2",
        },
    },
    {
        "html": "web/s2/chapter5/unit-test-5.html",
        "md": "Notes/SecondSemester/Chapter5/Unit_Test_5.md",
        "test_name": "Unit Test 5",
        "lesson_range": "Lessons 5.1–5.3",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Warm-up before calculator-checked written work", ["5.1"]),
            ("2. Column + calculator", "Column ×÷ then verify with calculator keystrokes", ["5.2", "5.3"]),
            ("3. Step by step", "Multi-step expressions; check steps with calculator", ["5.3"]),
            ("4. Number sentences", "Evaluate a multi-step product expression", ["5.3"]),
            ("5. Abacus", "Read numbers shown on abacus diagrams", ["5.1"]),
            ("6. Calculator flow", "Follow chained keystroke instructions (+, ÷, ×, −)", ["5.2", "5.3"]),
            ("7. Application problems", "Average speed; fabric sets with remainder; compare daily rates", ["5.3"]),
            ("8. Average", "Mean of five test scores", ["5.3"]),
            ("9. Calculator keypad", "Different addition orders giving the same sum", ["5.2", "5.3"]),
            ("10. Make = 1", "Insert +, −, ×, ÷ and brackets so each line equals 1", ["5.2", "5.3"]),
        ],
        "slugs": {
            "5.1": "5.1-counting-rod-to-calculator",
            "5.2": "5.2-calculator",
            "5.3": "5.3-use-a-calculator",
        },
    },
    {
        "html": "web/s2/chapter6/unit-test-6.html",
        "md": "Notes/SecondSemester/Chapter6/Unit_Test_6.md",
        "test_name": "Unit Test 6",
        "lesson_range": "Lessons 6.1–6.4",
        "prefix": "",
        "rows": [
            ("1. Fill in the spaces", "Perimeter formulas P = 2(l + w), P = 4s; square area; find width from P", ["6.1", "6.2", "6.3"]),
            ("2. Tables", "Complete missing length, width, side, or perimeter in tables", ["6.3", "6.4"]),
            ("3. True or false", "Perimeter vs area facts; formula reasoning", ["6.1", "6.3"]),
            ("4. Multiple choice", "Choose correct perimeter statement; effect of dimension changes", ["6.3", "6.4"]),
            ("5. Diagrams", "Find perimeter and area of composite figures on grids", ["6.3", "6.4"]),
            ("6. Application problems", "Fencing, frames, ink-spill grid, vegetable patch; two-change area stories", ["6.2", "6.4"]),
        ],
        "slugs": {
            "6.1": "6.1-perimeter-1",
            "6.2": "6.2-perimeter-2",
            "6.3": "6.3-perimeters-rectangles-squares-1",
            "6.4": "6.4-perimeters-rectangles-squares-2",
        },
    },
    {
        "html": "web/s2/chapter7/unit-test-7.html",
        "md": "Notes/SecondSemester/Chapter7/Unit_Test_7.md",
        "test_name": "Unit Test 7",
        "lesson_range": "Lessons 7.1–7.8",
        "prefix": "",
        "rows": [
            ("1. Mental calculation", "Mixed ×÷/+− fluency across the year", ["7.1"]),
            ("2. Column method", "Large × and ÷ with remainders", ["7.1"]),
            ("3. Step by step", "Multi-step regrouping and large-number chains", ["7.1"]),
            ("4. Number sentences", "Phrase → equation; evaluate with remainder", ["7.1"]),
            ("5. L-shape perimeter and area", "Composite figure P and A (cm, cm²)", ["7.4"]),
            ("6. Fill in the spaces", "Area units; mass/speed; digit bounds for quotients; fraction 1/2; combinations count", ["7.1", "7.2", "7.4", "7.8"]),
            ("7. Multiple choice", "Fraction comparison; count triangles in a figure; choose correct statement", ["7.2", "7.6"]),
            ("8. Application problems", "Mass, distance, area, square side from area, two-method problems, ways to place objects", ["7.3", "7.4", "7.5", "7.7", "7.8"]),
        ],
        "slugs": {
            "7.1": "7.1-multiplying-and-dividing",
            "7.2": "7.2-fractions",
            "7.3": "7.3-problem-solving",
            "7.4": "7.4-perimeters-and-areas",
            "7.5": "7.5-math-plaza-larger-area",
            "7.6": "7.6-math-plaza-matching",
            "7.7": "7.7-math-plaza-counting-apples",
            "7.8": "7.8-math-plaza-placing-apples",
        },
    },
]


def lesson_links(test: dict, lessons: list[str]) -> str:
    parts = []
    for num in lessons:
        slug = test["slugs"][num]
        parts.append(f'<a href="{slug}.html">{num}</a>')
    return ", ".join(parts)


def build_html_section(test: dict) -> str:
    chapter_num = re.search(r"chapter(\d+)", test["html"]).group(1)
    intro = (
        f"Where each {test['test_name']} question was taught in Chapter {chapter_num} "
        f"({test['lesson_range']})."
    )
    rows = []
    for q, focus, lessons in test["rows"]:
        rows.append(
            "            <tr>\n"
            f"              <td><strong>{q}</strong></td>\n"
            f"              <td>{focus}</td>\n"
            f"              <td>{lesson_links(test, lessons)}</td>\n"
            "            </tr>"
        )
    body = "\n".join(rows)
    return f"""<section class="block" id="question-map">
        <h2>Question–Lesson Map</h2>
        <p>{intro}</p>
        <table>
          <thead><tr><th>Test question</th><th>Focus</th><th>Taught in</th></tr></thead>
          <tbody>
{body}
          </tbody>
        </table>
      </section>"""


def build_md_section(test: dict) -> str:
    chapter_num = re.search(r"chapter(\d+)", test["html"]).group(1)
    intro = (
        f"Where each {test['test_name']} question was taught in Chapter {chapter_num} "
        f"({test['lesson_range']})."
    )
    lines = [
        "### Question–Lesson Map",
        "",
        intro,
        "",
        "| Test question | Focus | Taught in |",
        "|---------------|-------|-----------|",
    ]
    for q, focus, lessons in test["rows"]:
        q_md = q.replace("&amp;", "&")
        focus_md = focus.replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<")
        lines.append(f"| **{q_md}** | {focus_md} | {', '.join(lessons)} |")
    lines.extend(["", "---", ""])
    return "\n".join(lines)


def patch_html(path: Path, test: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'id="question-map"' in text:
        return False

    section = build_html_section(test)

    text = re.sub(
        r'(<a class="sub" href="#eureka">Eureka Correspondence</a>\s*)',
        r'\1        <a class="sub" href="#question-map">Question–Lesson Map</a>\n',
        text,
        count=1,
    )

    new_text, count = re.subn(
        r'(<section class="block" id="eureka">.*?</section>)(\s*</div>\s*(?:\n\s*)?<div class="group" id="core-concepts">)',
        lambda m: m.group(1) + "\n\n      " + section + m.group(2),
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError(f"Could not insert question map into {path}")

    path.write_text(new_text, encoding="utf-8")
    return True


def patch_md(path: Path, test: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    if "Question–Lesson Map" in text or "Question-Lesson Map" in text:
        return False

    section = build_md_section(test)

    if "### Eureka Math Correspondence" in text:
        text = re.sub(
            r"(### Eureka Math Correspondence.*?)(\n---\n)",
            r"\1\n\n" + section,
            text,
            count=1,
            flags=re.DOTALL,
        )
    elif "## Lesson Alignment" in text and "## Core Concepts" in text:
        text = re.sub(
            r"(## Lesson Alignment.*?)(\n---\n\n## Core Concepts)",
            lambda m: m.group(1) + "\n\n" + section + r"\2",
            text,
            count=1,
            flags=re.DOTALL,
        )
    elif "## Core Concepts" in text:
        text = text.replace("## Core Concepts", section + "## Core Concepts", 1)
    else:
        text = text.rstrip() + "\n\n" + section

    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    html_updated = []
    md_updated = []

    for test in TESTS:
        html_path = ROOT / test["html"]
        md_path = ROOT / test["md"]
        if patch_html(html_path, test):
            html_updated.append(test["html"])
        if md_path.exists() and patch_md(md_path, test):
            md_updated.append(test["md"])

    print(f"HTML updated: {len(html_updated)}")
    for item in html_updated:
        print(f"  {item}")
    print(f"Markdown updated: {len(md_updated)}")
    for item in md_updated:
        print(f"  {item}")


if __name__ == "__main__":
    main()
