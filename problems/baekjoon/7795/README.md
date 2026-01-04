---
problem_id: 7795
title: 먹을 것인가 먹힐 것인가
source: baekjoon
url: https://www.acmicpc.net/problem/7795
difficulty: silver3
algorithms: [two-pointer]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# 먹을 것인가 먹힐 것인가

## 문제
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.

![diagram](2026-01-03%20175806.png)

두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000)

## 출력
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.

## 예제

### 입력 1
```
2
5 3
8 1 7 3 1
3 6 1
3 4
2 13 7
103 11 290 215
```

### 출력 1
```
7
1
```

## 풀이

### 접근
- 정렬 먼저
- main, sub pointer를 옮기면서 비교
- 인덱스= 자기 앞에 있는 원소의 개수와 같음
1. 만약 a > b 이면 sub를 움직임
2. a <= b 이면 main을 움직임, 답에 sub의 index를 더해줌

### 시간 복잡도
- A, B 의 모든 경우를 비교했을 경우
    - M x N = MN = O(n^2)
    - 비효율적임
        1. B종이 더 큰게 명백함에도 계속 비교해야 함.

- 정렬 후에 투 포인터를 사용했을 경우
    - 움직임의 횟수를 세면 됨
    - M + N 회 -> O(N)



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
