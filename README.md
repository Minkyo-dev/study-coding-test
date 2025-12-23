# 코딩 테스트 준비 📚

> 알고리즘 문제 풀이 및 학습 저장소

## 📊 진행 현황

- **총 풀이 문제**: 2 / ∞
- **백준**: 2문제
- **프로그래머스**: 0문제
- **LeetCode**: 0문제

## 🎯 목표

- [ ] 카카오 기출 전부 풀기 (0/30)
- [ ] 삼성 A형 대비 (0/20)
- [ ] 백준 골드 달성
- [ ] 주 5문제 이상 풀이

## 📈 난이도별 현황

| 난이도 | 풀이 수 |
|--------|---------|
| 🟢 Easy/Bronze | 2 |
| 🟡 Medium/Silver | 0 |
| 🔴 Hard/Gold | 0 |

## 🔥 최근 풀이

- 2025-12-18: [백준 2557] Hello World
- 2025-12-18: [백준 1000] A+B

## 📚 알고리즘별 학습

| 알고리즘 | 진행률 | 링크 |
|----------|--------|------|
| 그래프 | 0/30 | [바로가기](algorithms/graph/) |
| DP | 0/40 | [바로가기](algorithms/dp/) |
| 그리디 | 0/25 | [바로가기](algorithms/greedy/) |
| BFS/DFS | 0/30 | [바로가기](algorithms/bfs-dfs/) |
| 이분 탐색 | 0/20 | [바로가기](algorithms/binary-search/) |
| 투 포인터 | 0/15 | [바로가기](algorithms/two-pointer/) |

## 🏢 회사별 기출

- [카카오](companies/kakao/problems.md)
- [삼성](companies/samsung/problems.md)
- [네이버](companies/naver/problems.md)
- [라인](companies/line/problems.md)

## 📂 디렉토리 구조

```
study-coding-test/
├── problems/              # 문제별 풀이 (출처/문제번호)
│   ├── baekjoon/
│   ├── programmers/
│   └── leetcode/
├── algorithms/            # 알고리즘별 정리
│   ├── graph/
│   ├── dp/
│   └── ...
├── companies/             # 회사별 기출 문제
├── templates/             # 코드 템플릿
├── notes/                 # 학습 노트
└── scripts/               # 자동화 스크립트
```

## 🛠️ 사용법

### 새 문제 생성
- 난이도 순서
bronze5 ~ brons1 -> silver5 ~ silver1 -> gold5 ~ gold1 -> platinum5 ~ platinum1 -> diamond5 ~ diamond1 -> ruby5 ~ ruby1

```bash
python scripts/create_problem.py baekjoon 1234 "문제제목" gold5 "dp,graph"
```

### 문제 검색

```bash
# 알고리즘별
python scripts/search.py --algorithm dp

# 난이도별
python scripts/search.py --difficulty gold

# 출처별
python scripts/search.py --source baekjoon

# 미해결 문제
python scripts/search.py --solved false
```

### 통계 확인

```bash
python scripts/stats.py
```

### 풀이 완료 표시

```bash
python scripts/update_solved.py baekjoon 1234
```

## 📝 문제 파일 구조

각 문제는 마크다운 frontmatter를 사용해서 메타데이터를 관리합니다:

```markdown
---
problem_id: "1000"
title: "A+B"
source: baekjoon
url: https://www.acmicpc.net/problem/1000
difficulty: bronze5
algorithms: [implementation, math]
solved: true
solved_date: 2025-12-18
---

# 문제 내용
...
```

## 💡 학습 자료

- [시간 복잡도 가이드](notes/time-complexity.md)
- [자주 쓰는 트릭](notes/tricks.md)
- [실수 노트](notes/mistakes.md)

## 🎨 템플릿

자주 사용하는 알고리즘 템플릿을 [templates/](templates/) 폴더에 정리:

- [빠른 입력](templates/input_fast.py)
- [그래프 탐색](templates/graph.py)
- [다익스트라](templates/dijkstra.py)
- [이분 탐색](templates/binary_search.py)
- [동적 계획법](templates/dp.py)
- [격자 BFS/DFS](templates/grid_bfs.py)

## 📌 공부 전략

1. **매일 꾸준히**: 하루 1~2문제씩
2. **복습**: 어려웠던 문제는 일주일 후 다시 풀기
3. **유형별 학습**: 비슷한 유형 연속으로 풀어서 패턴 익히기
4. **시간 측정**: 실전처럼 시간 제한 두고 풀기
5. **회고**: 풀이 후 더 나은 방법 고민

## 🔗 추천 사이트

- [백준](https://www.acmicpc.net/)
- [프로그래머스](https://programmers.co.kr/)
- [LeetCode](https://leetcode.com/)
- [solved.ac](https://solved.ac/) - 백준 난이도 및 통계

---

**시작일**: 2025-12-18
**목표**: 6개월 내 300문제 달성
