---
problem_id: 2943
title: Maximize Area of Square Hole in Grid
source: leetcode
url: https://leetcode.com/problems/2943
difficulty: medium
algorithms: [sort]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Maximize Area of Square Hole in Grid

## 문제
You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

당신에게 n, m 두개의 정수와 두개의 정수 배열 hBars, vBars가 주어진다. 그리드는 n + 2 의 가로와 m + 2의 세로 바가 있고, 1 x 1 단위의 셀을 가지고 있다. bars는 인덱스가 1부터 시작한다.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

당신은 hBars, vBars에서 각각 가로바와 세로바를 제거할 수 있다. 단 다른 bars는 고정되어 있고 제거할 수 없다.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

정수를 반환하는데 그리드 사각형의 가장 큰 너비를 가지는 정사각형의 너비를 반환하라, 몇개의 바를 제거한 후에.

## 입력
- 1 <= n <= 109
- 1 <= m <= 109
- 1 <= hBars.length <= 100
- 2 <= hBars[i] <= n + 1
- 1 <= vBars.length <= 100
- 2 <= vBars[i] <= m + 1
- All values in hBars are distinct.
- All values in vBars are distinct.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
<img src="./screenshot-from-2023-11-05-22-40-25.png" width="500px">

```python
n = 2
m = 1
hBars = [2,3]
vBars = [2]
```

### 출력 1
```python
4
# The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].
# One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.
```

### 입력 2
<img src="./screenshot-from-2023-11-04-17-01-02.png" width="500px">

```python
n = 1
m = 1
hBars = [2]
vBars = [2]
```

### 출력 2
```python
4
# To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.
```

### 입력 3
<img src="./unsaved-image-2.png" width="500px">

```python
n = 2
m = 3
hBars = [2,3]
vBars = [2,4]
```

### 출력 3
```python
4
# One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.
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
<!-- 어려웠던 점, 배운 점 -->
