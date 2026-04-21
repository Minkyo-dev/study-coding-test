#!/usr/bin/env python3
"""
LeetCode Top Interview 150 문제 스캐폴드 생성 스크립트

문제 번호만 입력하면 LeetCode에서 제목/난이도/태그/본문(문제 설명,
제약조건, 예제)을 가져와서
problems/leetcode/top_interview_150/<problem_id>/ 아래에
README.md, solution.py, _test.py 를 생성한다.

사용법:
    python scripts/create_leetcode_top150.py <problem_id> [<problem_id> ...] [--force]
    python scripts/create_leetcode_top150.py 1 121 238
    python scripts/create_leetcode_top150.py 1 --force    # 이미 존재해도 덮어씀
"""

import html as html_lib
import json
import os
import re
import sys
import urllib.request
from urllib.error import HTTPError, URLError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, "problems", "leetcode", "top_interview_150")

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
LEETCODE_LIST = "https://leetcode.com/api/problems/all/"

DIFFICULTY_MAP = {1: "easy", 2: "medium", 3: "hard"}

README_TEMPLATE = """---
problem_id: {problem_id}
title: {title}
source: leetcode
url: {url}
difficulty: {difficulty}
algorithms: [{algorithms}]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# {title}

## 문제
{description}

## 입력
{constraints}

## 출력
<!-- 출력 형식 -->

## 예제

{examples}{followup}

## 풀이

### 접근
<!-- 문제 해결 전략 -->

### 시간 복잡도
<!-- 분석 -->

## 코드

```python
import sys
input = sys.stdin.readline

def solve():
    pass

if __name__ == "__main__":
    solve()
```

## 회고
<!-- 어려웠던 점, 배운 점 -->
"""

SOLUTION_TEMPLATE = """import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(BASE_DIR)

from utils.profiling import profile_time_memory


@profile_time_memory
def mysolution():
    pass


@profile_time_memory
def othersolution():
    pass


if __name__ == "__main__":
    mysolution()
    othersolution()
"""

TEST_TEMPLATE = """import pytest
from solution import mysolution, othersolution

args = "expected"
params = []


@pytest.mark.parametrize(args, params)
def test_mysolution(expected):
    assert mysolution() == expected


@pytest.mark.parametrize(args, params)
def test_othersolution(expected):
    assert othersolution() == expected
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
    topicTags { slug }
  }
}
"""


def _http_get_json(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (scaffold)"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def _http_post_json(url, payload):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (scaffold)",
            "Referer": "https://leetcode.com",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_problem_index():
    """frontend_question_id -> {title, slug, difficulty_level} 매핑."""
    data = _http_get_json(LEETCODE_LIST)
    index = {}
    for item in data.get("stat_status_pairs", []):
        fid = item["stat"]["frontend_question_id"]
        index[int(fid)] = {
            "title": item["stat"]["question__title"],
            "slug": item["stat"]["question__title_slug"],
            "difficulty_level": item["difficulty"]["level"],
        }
    return index


def fetch_question_detail(slug):
    """GraphQL 로 content + topicTags 조회. 실패하면 (None, [])."""
    try:
        data = _http_post_json(
            LEETCODE_GRAPHQL,
            {"query": QUESTION_QUERY, "variables": {"titleSlug": slug}},
        )
    except (URLError, HTTPError, TimeoutError):
        return None, []
    question = (data.get("data") or {}).get("question") or {}
    content = question.get("content") or ""
    tags = [t["slug"] for t in (question.get("topicTags") or []) if t.get("slug")]
    return content, tags


def html_to_markdown(content):
    """LeetCode 의 HTML content 를 최소한의 마크다운으로 변환."""
    if not content:
        return ""
    s = content.replace("\r\n", "\n")

    # <br> → 개행
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.IGNORECASE)

    # <pre>...</pre> → 펜스드 코드 블록 (내부 <strong>/<em> 는 유지)
    def pre_repl(match):
        inner = match.group(1)
        inner = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", inner, flags=re.DOTALL | re.IGNORECASE)
        inner = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", inner, flags=re.DOTALL | re.IGNORECASE)
        inner = re.sub(r"<[^>]+>", "", inner)
        inner = html_lib.unescape(inner)
        return "\n```\n" + inner.strip("\n") + "\n```\n"

    s = re.sub(r"<pre[^>]*>(.*?)</pre>", pre_repl, s, flags=re.DOTALL | re.IGNORECASE)

    # 블록 레벨 태그 사이의 공백/개행은 의미 없음 (리스트 인덴트 등) → 제거.
    # 인라인 태그(<em>, <code>, <strong>) 사이 공백은 단어 분리용이라 유지해야 함.
    block_tags = "p|ul|ol|li|pre|div|h[1-6]|blockquote"
    s = re.sub(
        rf"(</(?:{block_tags})>)\s+(<(?:{block_tags})[^>]*>)",
        r"\1\2",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(rf"(<(?:{block_tags})[^>]*>)\s+(<(?:{block_tags})[^>]*>)", r"\1\2", s, flags=re.IGNORECASE)
    s = re.sub(rf"(</(?:{block_tags})>)\s+(</(?:{block_tags})>)", r"\1\2", s, flags=re.IGNORECASE)

    # 인라인 태그
    s = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r"<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>", r"**\1**", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r"<(?:em|i)[^>]*>(.*?)</(?:em|i)>", r"*\1*", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r"<sup[^>]*>(.*?)</sup>", r"^\1", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r"<sub[^>]*>(.*?)</sub>", r"_\1", s, flags=re.DOTALL | re.IGNORECASE)

    # 리스트
    s = re.sub(r"<li[^>]*>\s*(.*?)\s*</li>", r"- \1\n", s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r"</?(?:ul|ol)[^>]*>", "\n", s, flags=re.IGNORECASE)

    # 문단
    s = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", s, flags=re.DOTALL | re.IGNORECASE)

    # 나머지 태그 제거
    s = re.sub(r"<[^>]+>", "", s)

    # HTML 엔티티 디코드
    s = html_lib.unescape(s)

    # 공백 정리
    s = s.replace("\u00a0", " ")
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


# Example/Constraints/Follow-up 헤더는 줄 가운데에 걸쳐 있는 경우도 있어서
# 앵커 없이 매치한다. 예) "<p><strong>Follow-up: </strong>Can you ...</p>"
_HEADER_RE = re.compile(
    r"\*\*\s*(?P<name>Example\s*\d+|Constraints|Follow[\s\-]?up)\s*[:：]?\s*\*\*",
    re.IGNORECASE,
)


def _parse_example_body(body):
    """예제 섹션 본문에서 Input / Output / Explanation 추출."""
    body = body.strip()
    # 선행 코드 펜스 제거
    if body.startswith("```"):
        body = re.sub(r"^```[a-zA-Z]*\n?", "", body)
        body = re.sub(r"\n?```\s*$", "", body)
    body = body.strip()

    labels = ("Input", "Output", "Explanation")
    result = {"input": "", "output": "", "explanation": ""}
    for label in labels:
        pattern = re.compile(
            rf"\*\*\s*{label}\s*[:：]?\s*\*\*\s*(.*?)(?=\*\*\s*(?:{'|'.join(labels)})\s*[:：]?\s*\*\*|\Z)",
            re.IGNORECASE | re.DOTALL,
        )
        match = pattern.search(body)
        if match:
            result[label.lower()] = match.group(1).strip()
    return result


def parse_leetcode_markdown(md):
    """마크다운을 description / examples / constraints / followup 으로 분리."""
    empty = {"description": "", "examples": [], "constraints": "", "followup": ""}
    if not md:
        return empty

    matches = list(_HEADER_RE.finditer(md))
    if not matches:
        return {**empty, "description": md.strip()}

    description = md[: matches[0].start()].strip()
    examples, constraints, followup = [], "", ""

    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        body = md[start:end].strip()
        name = match.group("name").lower()
        if name.startswith("example"):
            examples.append(_parse_example_body(body))
        elif name.startswith("constraints"):
            constraints = body
        elif "follow" in name:
            followup = body

    return {
        "description": description,
        "examples": examples,
        "constraints": constraints,
        "followup": followup,
    }


def _render_examples(examples):
    if not examples:
        return "### 입력 1\n```\n```\n\n### 출력 1\n```\n```"
    blocks = []
    for i, ex in enumerate(examples, start=1):
        lines = [
            f"### 입력 {i}",
            "```",
            ex["input"] or "",
            "```",
            "",
            f"### 출력 {i}",
            "```",
            ex["output"] or "",
            "```",
        ]
        if ex["explanation"]:
            lines.append("")
            for line in ex["explanation"].splitlines():
                lines.append(f"> {line}" if line.strip() else ">")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def render_readme(problem_id, meta, tags, parsed):
    difficulty = DIFFICULTY_MAP.get(meta["difficulty_level"], "")
    url = f"https://leetcode.com/problems/{meta['slug']}"
    algorithms = ", ".join(tags)

    description = parsed["description"] or "<!-- 문제 설명 -->"
    constraints = parsed["constraints"] or "<!-- 입력 형식 -->"
    examples = _render_examples(parsed["examples"])
    followup = f"\n\n## Follow-up\n{parsed['followup']}" if parsed["followup"] else ""

    return README_TEMPLATE.format(
        problem_id=problem_id,
        title=meta["title"],
        url=url,
        difficulty=difficulty,
        algorithms=algorithms,
        description=description,
        constraints=constraints,
        examples=examples,
        followup=followup,
    )


def create_files(problem_id, meta, tags, parsed, force=False):
    problem_dir = os.path.join(TARGET_DIR, str(problem_id))
    os.makedirs(problem_dir, exist_ok=True)

    readme_path = os.path.join(problem_dir, "README.md")
    solution_path = os.path.join(problem_dir, "solution.py")
    test_path = os.path.join(problem_dir, "_test.py")

    targets = [
        (readme_path, render_readme(problem_id, meta, tags, parsed)),
        (solution_path, SOLUTION_TEMPLATE),
        (test_path, TEST_TEMPLATE),
    ]

    for path, content in targets:
        rel = os.path.relpath(path, BASE_DIR)
        if os.path.exists(path) and not force:
            print(f"  ⏭  이미 존재 (건너뜀): {rel}")
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ 생성: {rel}")


def parse_argv(argv):
    force = False
    ids = []
    for arg in argv:
        if arg in ("-f", "--force"):
            force = True
            continue
        try:
            ids.append(int(arg))
        except ValueError:
            print(f"⚠️  숫자가 아닌 인자 무시: {arg}")
    return force, ids


def main():
    if len(sys.argv) < 2:
        print("사용법: python scripts/create_leetcode_top150.py <problem_id> [<problem_id> ...] [--force]")
        print("예시: python scripts/create_leetcode_top150.py 1 121 238")
        sys.exit(1)

    force, ids = parse_argv(sys.argv[1:])
    if not ids:
        print("❌ 유효한 문제 번호가 없습니다.")
        sys.exit(1)

    print("📥 LeetCode 문제 목록 조회 중...")
    try:
        index = fetch_problem_index()
    except (URLError, HTTPError, TimeoutError) as e:
        print(f"❌ LeetCode 목록 조회 실패: {e}")
        sys.exit(1)

    for pid in ids:
        meta = index.get(pid)
        if not meta:
            print(f"\n❌ 문제 번호 {pid} 을(를) 찾지 못했습니다.")
            continue
        diff = DIFFICULTY_MAP.get(meta["difficulty_level"], "?")
        print(f"\n▶ {pid} - {meta['title']} ({diff})")

        content_html, tags = fetch_question_detail(meta["slug"])
        if tags:
            print(f"  🏷  tags: {', '.join(tags)}")
        if content_html:
            markdown = html_to_markdown(content_html)
            parsed = parse_leetcode_markdown(markdown)
            ex_count = len(parsed["examples"])
            cons = "✓" if parsed["constraints"] else "✗"
            print(f"  📄 본문 파싱: examples={ex_count}, constraints={cons}")
        else:
            parsed = {"description": "", "examples": [], "constraints": "", "followup": ""}
            print("  ⚠️  본문을 가져오지 못했습니다 (프리미엄 문제일 수 있음).")

        create_files(pid, meta, tags, parsed, force=force)

    print("\n✨ 완료")


if __name__ == "__main__":
    main()
