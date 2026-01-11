---
problem_id: 85
title: Maximal Rectangle
source: baekjoon
url: https://www.acmicpc.net/problem/85
difficulty: hard
algorithms: [dp]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Maximal Rectangle

## 문제
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
rows and cols로 이루어진 0과 1의 바이너리 매트릭스가 주어진다. 1로 이루어진 가장 큰 직사각형의 넓이를 구하라

## 입력
- rows == matrix.length
- cols == matrix[i].length
- 1 <= rows, cols <= 200
- matrix[i][j] is '0' or '1'.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```python
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
```

### 출력 1
```python
6
```

### 입력 2
```python
matrix = [["0"]]
```

### 출력 2
```python
0
```

### 입력 3
```python
matrix = [["1"]]
```

### 출력 3
```python
1
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
