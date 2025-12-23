#!/usr/bin/env python3
"""
통계 생성 스크립트

사용법:
    python scripts/stats.py
"""

import os
import re
from pathlib import Path
from collections import Counter, defaultdict

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

def collect_stats():
    """통계 수집"""
    stats = {
        'total': 0,
        'solved': 0,
        'by_source': Counter(),
        'by_difficulty': Counter(),
        'by_algorithm': Counter(),
        'recent': []
    }

    problems_dir = Path('problems')

    for readme in problems_dir.rglob('README.md'):
        try:
            with open(readme, 'r', encoding='utf-8') as f:
                content = f.read()

            meta = parse_frontmatter(content)
            if not meta:
                continue

            stats['total'] += 1

            source = meta.get('source', 'unknown')
            stats['by_source'][source] += 1

            if meta.get('solved', 'false') == 'true':
                stats['solved'] += 1

                difficulty = meta.get('difficulty', 'unknown')
                stats['by_difficulty'][difficulty] += 1

                # 알고리즘 파싱
                algorithms = meta.get('algorithms', '[]')
                algorithms = algorithms.strip('[]').split(',')
                for algo in algorithms:
                    algo = algo.strip()
                    if algo:
                        stats['by_algorithm'][algo] += 1

                # 최근 풀이
                solved_date = meta.get('solved_date', '')
                if solved_date and solved_date != 'null':
                    stats['recent'].append({
                        'date': solved_date,
                        'title': meta.get('title', ''),
                        'source': source,
                        'id': meta.get('problem_id', '')
                    })

        except Exception as e:
            print(f"⚠️  파싱 오류: {readme} - {e}")

    # 최근 풀이 정렬
    stats['recent'].sort(key=lambda x: x['date'], reverse=True)
    stats['recent'] = stats['recent'][:10]

    return stats

def display_stats(stats):
    """통계 출력"""
    print("\n" + "="*50)
    print("📊 코딩 테스트 통계")
    print("="*50 + "\n")

    # 전체 현황
    print(f"✅ 풀이 완료: {stats['solved']} / {stats['total']} 문제")
    if stats['total'] > 0:
        percentage = (stats['solved'] / stats['total']) * 100
        print(f"📈 진행률: {percentage:.1f}%\n")

    # 출처별
    print("📚 출처별 현황:")
    for source, count in stats['by_source'].most_common():
        print(f"  - {source}: {count}문제")
    print()

    # 난이도별
    if stats['by_difficulty']:
        print("🎯 난이도별 풀이:")
        for diff, count in sorted(stats['by_difficulty'].items()):
            print(f"  - {diff}: {count}문제")
        print()

    # 알고리즘별
    if stats['by_algorithm']:
        print("🔥 알고리즘별 풀이 (Top 10):")
        for algo, count in stats['by_algorithm'].most_common(10):
            print(f"  - {algo}: {count}문제")
        print()

    # 최근 풀이
    if stats['recent']:
        print("🕐 최근 풀이:")
        for item in stats['recent']:
            print(f"  - {item['date']}: [{item['source']}] {item['id']} - {item['title']}")
        print()

def main():
    stats = collect_stats()
    display_stats(stats)

if __name__ == "__main__":
    main()

