---
problem_id: 2003
title: sum of numbers 2
source: baekjoon
url: https://www.acmicpc.net/problem/2003
difficulty: silver4
algorithms: [two-pointer]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# sum of numbers

## 문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

## 출력
첫째 줄에 경우의 수를 출력한다.

## 예제

### 입력 1
```
4 2
1 1 1 1
```

### 출력 1
```
3
```

### 입력 2
```
10 5
1 2 3 4 2 5 3 1 1 2
```

### 출력 2
```
3
```

## 풀이

### 접근
<!-- 문제 해결 전략 -->
1. 시작점을 고정하고, 끝점을 한칸씩 옮긴다.
2. 합 >= M 이면 시작점을 옮긴다.
3. 합 < M 이면 끝점을 옮긴다.

### 시간 복잡도
<!-- 분석 -->
- 시간복잡도는 연산의 횟수를 세는 것
- 시작점 또는 끝점이 움직일 때 1번 연산이 됨 
- 시작점 연산 최대 N회, 끝점 연산 최대 N회 -> 시간 복잡도는 2N -> O(N) 인 알고리즘이 됨

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
