---
problem_id: 55
title: Jump Game
source: leetcode
url: https://leetcode.com/problems/jump-game
difficulty: medium
algorithms: [array, dynamic-programming, greedy]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Jump Game

## 문제
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`* if you can reach the last index, or *`false`* otherwise*.

## 입력
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums = [2,3,1,1,4]
```

### 출력 1
```
true
```

> Jump 1 step from index 0 to 1, then 3 steps to the last index.

### 입력 2
```
nums = [3,2,1,0,4]
```

### 출력 2
```
false
```

> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

## 풀이

### 접근
- initial approach
```python
last_idx = len(nums) - 1
    cur_idx = 0
    is_reached = False
    while True:
        if last_idx <= cur_idx :
            is_reached = True
            break
        elif nums[cur_idx] == 0 :
            break
        else:
            cur_idx += nums[cur_idx]
    return is_reached
```

- second approach
```python
if len(nums) == 1:
        return True
    last_idx = len(nums) - 1
    for idx, n in enumerate(nums):
        if n == 0:
            return False
        if (n + idx) >= last_idx:
            return True
    return False
```

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
