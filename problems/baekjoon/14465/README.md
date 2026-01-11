---
problem_id: 14465
title: 소가 길을 건너간 이유 5
source: baekjoon
url: https://www.acmicpc.net/problem/14465
difficulty: silver2
algorithms: [Prefix Sum, Sliding Window]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# 소가 길을 건너간 이유 5

## 문제
농부 존의 농장에 원형 길이 있다고 했지만, 길은 그뿐만이 아니다. 그 옆에 일자형 길이 있는데, 1번부터 N번까지의 번호가 붙은 횡단보도 N (1 ≤ N ≤ 100,000)개로 이루어져 있다. 교통사고를 방지하기 위해 존은 각 횡단보도에 신호등을 설치해 놓았다. 그러던 어느 날, 강력한 뇌우로 인해 몇몇 신호등이 망가졌다. 존은 연속한 K개의 신호등이 존재하도록 신호등을 수리하고 싶다. 이번에도 우리가 존을 도와주자.

## 입력
첫 줄에 N, K, B (1 ≤ B,K ≤ N)가 주어진다. 그 다음 B줄에는 고장난 신호등의 번호가 하나씩 주어진다.

## 출력
정상적으로 작동하는 연속 K개의 신호등이 존재하려면 최소 몇 개의 신호등을 수리해야 하는지 출력한다.

## 예제

### 입력 1
```
10 6 5
2
10
1
5
9
```

### 출력 1
```
1
```

### 입력 2
```
```

### 출력 2
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
- 누적합에서 세어야 할 개수를 잘 생각 해야 한다.
- 처음에 누적합을 만들 때 고장난 횡단보도를 1이 아닌 0으로 만들어서 틀렸었다.
