---
problem_id: 2512
title: 예산
source: baekjoon
url: https://www.acmicpc.net/problem/2512
difficulty: 3
algorithms: [binary-search]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# 예산

## 문제

국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 배정하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.

1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.

여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

one of the role of the country is to review the budget requests of various regions and allocate the national budget. The total amount of the national budget is pre-determined, so it may not be possible to allocate all the budget requests. So, the budget is allocated in the following way:

1. If all the requests can be allocated, the request amount is allocated.
2. If all the requests can't be allocated, a specific integer upper limit is calculated and the request amount is allocated up to the upper limit.

For example, the total amount of the national budget is 485 and the budget requests of 4 regions are 120, 110, 140, 150. If the upper limit is 127, the request amounts are allocated as 120, 110, 127, 127 and the sum is 484, which is the maximum possible.

## 입력

첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다.

## 출력

첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.

## 예제

### 입력 1
```
4
120 110 140 150
485
```

### 출력 1
```
127
```

## 풀이

### 접근

- **찾고자 하는 값** 찾기 : 최적의 상한액
- **탐색 범위**찾기 : [0, 지방 요청 금액 중 최댓값]
- 시뮬레이션
    - [0, 150] ((150 + 0) / 2 = 75)
    - -> [75, 150] ((150 + 75) / 2 = 112.5 = 112)
    - -> [112, 150] ((150 + 112) / 2 = 130)
    - -> [112, 130] ((112, 130) / 2 = 121)
    - ...
    - -> [127, 127] -> 정답

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
