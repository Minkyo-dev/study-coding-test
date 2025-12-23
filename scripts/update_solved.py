#!/usr/bin/env python3
"""
문제 풀이 완료 업데이트 스크립트

사용법:
    python scripts/update_solved.py baekjoon 1000
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

def update_solved_status(source, problem_id):
    """문제 풀이 완료로 업데이트"""

    problem_path = Path(f'problems/{source}/{problem_id}/README.md')

    if not problem_path.exists():
        print(f"❌ 문제를 찾을 수 없습니다: {problem_path}")
        return False

    with open(problem_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # solved: false → true
    content = re.sub(r'solved:\s*false', 'solved: true', content)

    # solved_date 업데이트
    today = datetime.now().strftime('%Y-%m-%d')
    content = re.sub(r'solved_date:\s*null', f'solved_date: {today}', content)

    with open(problem_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 풀이 완료로 업데이트: {problem_path}")
    return True

def main():
    if len(sys.argv) < 3:
        print("사용법: python update_solved.py <source> <problem_id>")
        print("예시: python update_solved.py baekjoon 1000")
        sys.exit(1)

    source = sys.argv[1]
    problem_id = sys.argv[2]

    update_solved_status(source, problem_id)

if __name__ == "__main__":
    main()

