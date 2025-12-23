#!/usr/bin/env python3
"""
문제 검색 스크립트

사용법:
    python scripts/search.py --algorithm dp
    python scripts/search.py --difficulty gold
    python scripts/search.py --source baekjoon
    python scripts/search.py --solved false
"""

import os
import re
import argparse
from pathlib import Path

def parse_frontmatter(content):
    """마크다운 frontmatter 파싱"""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter

def search_problems(algorithm=None, difficulty=None, source=None, solved=None):
    """문제 검색"""
    results = []
    problems_dir = Path('problems')

    # 모든 README.md 파일 찾기
    for readme in problems_dir.rglob('README.md'):
        try:
            with open(readme, 'r', encoding='utf-8') as f:
                content = f.read()

            meta = parse_frontmatter(content)
            if not meta:
                continue

            # 필터링
            if algorithm and algorithm not in meta.get('algorithms', ''):
                continue
            if difficulty and difficulty not in meta.get('difficulty', ''):
                continue
            if source and source != meta.get('source', ''):
                continue
            if solved is not None:
                is_solved = meta.get('solved', 'false') == 'true'
                if is_solved != solved:
                    continue

            results.append({
                'path': str(readme),
                'id': meta.get('problem_id', ''),
                'title': meta.get('title', ''),
                'source': meta.get('source', ''),
                'difficulty': meta.get('difficulty', ''),
                'algorithms': meta.get('algorithms', ''),
                'solved': meta.get('solved', 'false')
            })

        except Exception as e:
            print(f"⚠️  파싱 오류: {readme} - {e}")

    return results

def display_results(results):
    """검색 결과 출력"""
    if not results:
        print("❌ 검색 결과가 없습니다.")
        return

    print(f"\n📊 총 {len(results)}개의 문제를 찾았습니다.\n")

    for r in results:
        solved_icon = '✅' if r['solved'] == 'true' else '⬜'
        print(f"{solved_icon} [{r['source']}] {r['id']} - {r['title']}")
        print(f"   난이도: {r['difficulty']} | 알고리즘: {r['algorithms']}")
        print(f"   경로: {r['path']}\n")

def main():
    parser = argparse.ArgumentParser(description='문제 검색')
    parser.add_argument('--algorithm', '-a', help='알고리즘 (예: dp, graph)')
    parser.add_argument('--difficulty', '-d', help='난이도 (예: gold, silver)')
    parser.add_argument('--source', '-s', help='출처 (예: baekjoon, programmers)')
    parser.add_argument('--solved', type=lambda x: x.lower() == 'true', help='풀이 여부 (true/false)')

    args = parser.parse_args()

    results = search_problems(
        algorithm=args.algorithm,
        difficulty=args.difficulty,
        source=args.source,
        solved=args.solved
    )

    display_results(results)

if __name__ == "__main__":
    main()

