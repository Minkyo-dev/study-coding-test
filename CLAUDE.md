# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Personal coding-test study repo (Korean). Problems are organized by source/id and cross-indexed by algorithm. Commentary, commit messages, and problem write-ups are in Korean — follow that convention when editing or adding content.

## Common commands

Create a new problem (scaffolds `README.md`, `solution.py`, `_test.py` under `problems/<source>/<id>/`, and appends a link in `algorithms/<algo>/README.md` if the algo folder exists):

```bash
python scripts/create_problem.py <source> <problem_id> "<title>" <difficulty> "<algo1,algo2>"
# e.g. python scripts/create_problem.py baekjoon 1000 "A+B" bronze5 "implementation,math"
```

Mark a problem solved (flips frontmatter `solved: false → true` and sets `solved_date` to today):

```bash
python scripts/update_solved.py <source> <problem_id>
```

Scaffold a LeetCode Top Interview 150 problem by number only — fetches title / difficulty / topic tags from LeetCode (REST `/api/problems/all/` for the ID→slug map + GraphQL for tags) and writes `README.md`, `solution.py`, `_test.py` under `problems/leetcode/top_interview_150/<id>/`. Skips files that already exist.

```bash
python scripts/create_leetcode_top150.py <problem_id> [<problem_id> ...]
# e.g. python scripts/create_leetcode_top150.py 1 121 238
```

Note: this path is one level deeper than regular `problems/<source>/<id>/`, so the generated `solution.py` uses **5** `dirname` calls (not 4) to reach the repo root. Keep that header intact when editing.

Search / stats (read README.md frontmatter across `problems/`):

```bash
python scripts/search.py --algorithm dp --difficulty gold --source baekjoon --solved false
python scripts/stats.py
```

Run tests for a single problem — `_test.py` uses a bare `from solution import ...`, so pytest must be run from inside the problem directory:

```bash
cd problems/<source>/<id> && pytest _test.py -v
# single param case:
cd problems/<source>/<id> && pytest _test.py::test_mysolution -v
```

Supported `<source>` values (URL-prefixed in `create_problem.py`): `baekjoon`, `programmers`, `leetcode`, `swea`, `codeforces`.

Difficulty ordering (Baekjoon-style): `bronze5 → bronze1 → silver5 → silver1 → gold5 → gold1 → platinum5 → platinum1 → diamond5 → diamond1 → ruby5 → ruby1`.

## Problem file conventions

Each `problems/<source>/<id>/` directory follows a fixed layout that the scripts depend on:

- `README.md` — starts with YAML-ish frontmatter (`problem_id`, `title`, `source`, `url`, `difficulty`, `algorithms`, `solved`, `solved_date`, `retry_count`, `time_complexity`, `space_complexity`). `search.py` and `stats.py` parse this frontmatter directly — keep field names and the `---` delimiters intact or those tools break.
- `solution.py` — contains two functions, `mysolution(...)` (own attempt) and `othersolution(...)` (reference / improved solution), both decorated with `@profile_time_memory`. The top of the file adds the repo root to `sys.path` via a 4-level `dirname` chain so `from utils.profiling import profile_time_memory` resolves. Preserve that header exactly when adding new problems; it depends on the fixed 4-level nesting `problems/<source>/<id>/solution.py`.
- `_test.py` — pytest file using `@pytest.mark.parametrize` against `mysolution` / `othersolution` imported from `solution`. Because of the bare import, tests must be run from the problem directory (see above).

When `create_problem.py` is given algorithm tags, it appends a checklist line to `algorithms/<tag>/README.md` **only if that directory already exists** — so adding a brand-new algorithm category requires creating the folder first.

## Repo structure (big picture)

- `problems/` — actual problem solutions, grouped by source (`baekjoon/`, `leetcode/`, `programmers/`).
- `algorithms/` — one folder per algorithm category (`dp/`, `graph/`, `bfs-dfs/`, …); each `README.md` is an auto-appended index of problems tagged with that algorithm.
- `companies/` — company-tagged problems (`kakao/`, `naver/`, `samsung/`).
- `templates/` — reusable Python snippets (`input_fast.py`, `graph.py`, `dijkstra.py`, `dp.py`, `grid_bfs.py`) to copy into new solutions.
- `data_structure/` and `notes/` — Korean study notes (trees, prefix sums, time complexity, tricks, mistakes).
- `utils/profiling.py` — the `@profile_time_memory` decorator; prints wall time, Python tracemalloc peak, and RSS delta. All solutions import from here.
- `scripts/` — the four CLI tools listed above; they are the intended interface for adding, updating, and querying problems.
