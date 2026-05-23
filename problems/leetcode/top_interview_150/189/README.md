---
problem_id: 189
title: Rotate Array
source: leetcode
url: https://leetcode.com/problems/rotate-array
difficulty: medium
algorithms: [array, math, two-pointers]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Rotate Array

## 문제
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## 입력
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums = [1,2,3,4,5,6,7], k = 3
```

### 출력 1
```
[5,6,7,1,2,3,4]
```

> rotate 1 steps to the right: [7,1,2,3,4,5,6]
> rotate 2 steps to the right: [6,7,1,2,3,4,5]
> rotate 3 steps to the right: [5,6,7,1,2,3,4]

### 입력 2
```
nums = [-1,-100,3,99], k = 2
```

### 출력 2
```
[3,99,-1,-100]
```

> rotate 1 steps to the right: [99,-1,-100,3]
> rotate 2 steps to the right: [3,99,-1,-100]

## Follow-up
- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

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
