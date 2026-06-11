---
problem_id: 238
title: Product of Array Except Self
source: leetcode
url: https://leetcode.com/problems/product-of-array-except-self
difficulty: medium
algorithms: [array, prefix-sum]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Product of Array Except Self

## 문제
Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

주어진 정수 배열 'nums'에 대해 'answer'을 반환하라. 'answer[i]'는 'nums[i]'를 제외한 'nums'의 모든 요소의 곱과 같다.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

앞에서든 뒤에서든 'nums'의 곱은 32비트 정수에 맞는다고 보장된다.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## 입력
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums = [1,2,3,4]
```

### 출력 1
```
[24,12,8,6]
```

### 입력 2
```
nums = [-1,1,0,-3,3]
```

### 출력 2
```
[0,0,9,0,0]
```

## Follow-up
Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## 풀이

### 접근
The main point of this problem is to calculate the product of all elements except the current element without using division. We can achieve this by calculating the prefix product and suffix product for each element.

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
