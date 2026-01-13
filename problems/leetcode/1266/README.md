---
problem_id: 1266
title: Minimum Time Visigin All Points
source: leetcode
url: https://leetcode.com/problems/1266
difficulty: Easy
algorithms: [Array,Math,Geometry]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Minimum Time Visigin All Points

## 문제
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
2차원 평면에, n 포인트가 정소 좌표 (xi, yi)로 주어진다. 가장 최소한의 시간을 사용하여 모든 포인트를 방문하는 시간을 반환하시오.

You can move according to these rules:
이동규칙

- In 1 second, you can either: 1초 동안 아래 동작중 하나를 선택할 수 있다.
    - move vertically by one unit,  수직으로 1칸 이동
    - move horizontally by one unit, or 수평으로 1칸 이동
    - move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
    - 대각선으로 1칸 이동 (수직으로 1칸 이동 후 수평으로 1칸 이동)
- You have to visit the points in the same order as they appear in the array.
    방문할 포인트의 순서는 배열에 주어진 순서대로 방문해야 한다.
- You are allowed to pass through points that appear later in the order, but these do not count as visits.
    배열에 나중에 나오는 포인트를 지나갈 수 있지만, 이는 방문으로 치지 않는다.

## 입력
- points.length == n
- 1 <= n <= 100
- points[i].length == 2
- -1000 <= points[i][0], points[i][1] <= 1000

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
<img src="./1626_example_1.png" width="500px">

```python
points = [[1,1],[3,4],[-1,0]]
```

### 출력 1
```python
7

# One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds
```

### 입력 2
```python
points = [[3,2],[-2,2]]
```

### 출력 2
```python
5
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
그리드에서 거리를 계산할 때 많이사용되는 거리 계산 방식이 있음
- 유클리드 거리 (euclid distance)
- 맨하탄 거리 (Menhatan distance)
- 체비셰프 거리 (Chebyshev Distance)
