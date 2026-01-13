---
problem_id: 3453
title: Separate Squares 1
source: leetcode
url: https://leetcode.com/problems/3453
difficulty: Medium
algorithms: [binary-search]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Separate Squares 1

## 문제
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.
너는 2차원의 숫자 배열 squares가 주어진다. 각 squares[i] = [xi, yi, li] 는 왼쪽 아래의 점과 x축에 평행한 정사각형 한변의 길이가 li인 정사각형의 좌표를 나타낸다.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.
동일한 라인 위 사각형의 전체 면적과 아래 사각형의 전체 면적이 같은 라인의 y좌표를 찾아서 반환하라.

Answers within 10-5 of the actual answer will be accepted.
정답의 오차범위는 10-5 이내로 허용된다.

Note: Squares may overlap. Overlapping areas should be counted multiple times.
정사각형은 겹칠 수 있다. 겹치는 부분은 여러번 계산되어야 한다.

## 입력
- 1 <= squares.length <= 5 * 104
- squares[i] = [xi, yi, li]
- squares[i].length == 3
- 0 <= xi, yi <= 109
- 1 <= li <= 109
- The total area of all the squares will not exceed 1012.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```python
squares = [[0,0,1],[2,2,1]]
```

### 출력 1
<img src="./4062example1drawio.png" width="500px">

```python
1.00000
# Any horizontal line between y = 1 and y = 2 will have 1 square unit above it and 1 square unit below it. The lowest option is 1.
```

### 입력 2
```python
squares = [[0,0,2],[1,1,1]]
```

### 출력 1
<img src="./4062example2drawio.png" width="500px">

```python
1.16667
# Below the line: 7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5.
# Above the line: 5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5.
# Since the areas above and below the line are equal, the output is 7/6 = 1.16667.
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
