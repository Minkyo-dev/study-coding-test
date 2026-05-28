---
problem_id: 274
title: H-Index
source: leetcode
url: https://leetcode.com/problems/h-index
difficulty: medium
algorithms: [array, sorting, counting-sort]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# H-Index

## 문제
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i^th` paper, return *the researcher's h-index*.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

## 입력
- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
citations = [3,0,6,1,5]
```

### 출력 1
```
3
```

> [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
> Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

### 입력 2
```
citations = [1,3,1]
```

### 출력 2
```
1
```

## 풀이

### 접근
The Rule of Thumb

An H-index of $H$ means a researcher has published at least $H$ papers that have each been cited at least $H$ times.

To find it, the easiest trick is to sort the papers from the highest number of citations to the lowest:

Example Breakdown (From LeetCode Example 1)

Imagine a researcher has 5 papers with these citation counts: [3, 0, 6, 1, 5]

1. Sort them in descending order: [6, 5, 3, 1, 0]
2. Match them against their position (1st paper, 2nd paper, etc.):
    - Paper 1: 6 citations $\rightarrow$ (6 is $\ge$ 1) $\rightarrow$ Keep going!
    - Paper 2: 5 citations $\rightarrow$ (5 is $\ge$ 2) $\rightarrow$ Keep going!
    - Paper 3: 3 citations $\rightarrow$ (3 is $\ge$ 3) $\rightarrow$ Keep going!
    - Paper 4: 1 citation $\rightarrow$ (1 is not $\ge$ 4) $\rightarrow$ Stop here.

Because the researcher has 3 papers that have at least 3 citations, their H-index is 3.

The remaining papers don't qualify because they haven't reached that threshold of 4 citations for 4 papers.

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
