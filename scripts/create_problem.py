#!/usr/bin/env python3
"""
새 문제 파일 생성 스크립트

사용법:
    python scripts/create_problem.py baekjoon 1000 "A+B" bronze5 implementation,math
"""

import os
import sys
from datetime import datetime

TEMPLATE = """---
problem_id: {problem_id}
title: {title}
source: {source}
url: {url}
difficulty: {difficulty}
algorithms: {algorithms}
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# {title}

## 문제
<!-- 문제 설명 -->

## 입력
<!-- 입력 형식 -->

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
```

### 출력 1
```
```

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

SOURCE_URLS = {
    'baekjoon': 'https://www.acmicpc.net/problem/',
    'programmers': 'https://school.programmers.co.kr/learn/courses/30/lessons/',
    'leetcode': 'https://leetcode.com/problems/',
    'swea': 'https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=',
    'codeforces': 'https://codeforces.com/problemset/problem/'
}

def create_problem(source, problem_id, title, difficulty='', algorithms=''):
    """문제 파일 생성"""

    # 디렉토리 생성
    problem_dir = os.path.join('problems', source, problem_id)
    os.makedirs(problem_dir, exist_ok=True)

    # URL 생성
    base_url = SOURCE_URLS.get(source, '')
    url = f"{base_url}{problem_id}" if base_url else ''

    # 알고리즘 리스트 포맷
    algo_list = f"[{algorithms}]" if algorithms else "[]"

    # 파일 내용 생성
    content = TEMPLATE.format(
        problem_id=problem_id,
        title=title,
        source=source,
        url=url,
        difficulty=difficulty,
        algorithms=algo_list
    )

    # 파일 저장
    file_path = os.path.join(problem_dir, 'README.md')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 문제 파일 생성 완료: {file_path}")

    # 정답 코드 파일 생성
    file_path = os.path.join(problem_dir, "solution.py")
    content = """import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(BASE_DIR)
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
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 정답 코드 파일 생성 완료: {file_path}")

    # 테스트 코드 파일 생성
    file_path = os.path.join(problem_dir, "_test.py")
    content = """import pytest
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
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 테스트 코드 파일 생성 완료: {file_path}")

    algorithms_folder = os.listdir("algorithms")
    for algo in algorithms.split(","):
        if algo in algorithms_folder:
            file_path = os.path.join("algorithms", algo, 'README.md')
            content = f"- [ ] [{source} {problem_id}](../../problems/{source}/{problem_id}/) - {title}"
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(content)

            print(f"✅ 알고리즘 문제 추가 완료: {file_path}")


def main():
    if len(sys.argv) < 4:
        print("사용법: python create_problem.py <source> <problem_id> <title> [difficulty] [algorithms]")
        print("예시: python create_problem.py baekjoon 1000 'A+B' bronze5 'implementation,math'")
        sys.exit(1)

    source = sys.argv[1]
    problem_id = sys.argv[2]
    title = sys.argv[3]
    difficulty = sys.argv[4] if len(sys.argv) > 4 else ''
    algorithms = sys.argv[5] if len(sys.argv) > 5 else ''

    create_problem(source, problem_id, title, difficulty, algorithms)

if __name__ == "__main__":
    main()

