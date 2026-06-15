---
problem_id: 134
title: Gas Station
source: leetcode
url: https://leetcode.com/problems/gas-station
difficulty: medium
algorithms: [array, greedy]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Gas Station

## 문제
There are `n` gas stations along a circular route, where the amount of gas at the `i^th` station is `gas[i]`.

둥근 경로에 n개의 주유소가 있다. i번째의 주유소에 있는 기름의 양은 gas[i]이다.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i^th` station to its next `(i + 1)^th` station. You begin the journey with an empty tank at one of the gas stations.

당신의 차는 한계가 없는 기름 탱크를 가지고 있고, i번째 주유소에서 다음 (i + 1) 번째 주유소로 이동하는데 cost[i]의 기름이 필요하다. 당신은 빈 탱크로 주유소 중 하나에서 여행을 시작한다.

Given two integer arrays `gas` and `cost`, return *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return* `-1`. If there exists a solution, it is **guaranteed** to be **unique**.

주어진 두개의 array gas와 cost, 시작하는 주유소의 인덱스를 반환하라. 만약 당신이 시계방향으로 한바퀴 돌 수 있다면, 그렇지 않다면 -1을 반환하라. 만약 해결책이 존재한다면, 그것은 유일하다고 보장된다.

## 입력
- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
- The input is generated such that the answer is unique.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
gas = [1,2,3,4,5], cost = [3,4,5,1,2]
```

### 출력 1
```
3
```

> Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
> Travel to station 4. Your tank = 4 - 1 + 5 = 8
> Travel to station 0. Your tank = 8 - 2 + 1 = 7
> Travel to station 1. Your tank = 7 - 3 + 2 = 6
> Travel to station 2. Your tank = 6 - 4 + 3 = 5
> Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
> Therefore, return 3 as the starting index.

### 입력 2
```
gas = [2,3,4], cost = [3,4,3]
```

### 출력 2
```
-1
```

> You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
> Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
> Travel to station 0. Your tank = 4 - 3 + 2 = 3
> Travel to station 1. Your tank = 3 - 3 + 3 = 3
> You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
> Therefore, you can't travel around the circuit once no matter where you start.

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
