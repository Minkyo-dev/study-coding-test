---
problem_id: 1161
title: Maximum Level Sum of a Binary Tree
source: leetcode
url: https://leetcode.com/problems/1161
difficulty: Medium
algorithms: []
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Maximum Level Sum of a Binary Tree

## 문제
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

## 입력
<!-- 입력 형식 -->

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```python
root = [1,7,0,7,-8,null,null]
```

### 출력 1
```python
2

# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
```

### 입력 2
```python 
root = [989,null,10250,98693,-89388,null,null,null,-32127]
```

### 출력 2
```python
2
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
