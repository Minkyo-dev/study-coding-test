---
problem_id: 88
title: Merge Sorted Array
source: leetcode
url: https://leetcode.com/problems/merge-sorted-array
difficulty: easy
algorithms: [array, two-pointers, sorting]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Merge Sorted Array

## 문제
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be *stored inside the array *`nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## 입력
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
```

### 출력 1
```
[1,2,2,3,5,6]
```

> The arrays we are merging are [1,2,3] and [2,5,6].
> The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

### 입력 2
```
nums1 = [1], m = 1, nums2 = [], n = 0
```

### 출력 2
```
[1]
```

> The arrays we are merging are [1] and [].
> The result of the merge is [1].

### 입력 3
```
nums1 = [0], m = 0, nums2 = [1], n = 1
```

### 출력 3
```
[1]
```

> The arrays we are merging are [] and [1].
> The result of the merge is [1].
> Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

## Follow-up
Can you come up with an algorithm that runs in `O(m + n)` time?

## 풀이

### 접근
<!-- 문제 해결 전략 -->
- nums2를 뒤에서 부터 채워야 한다는 것을 처음에 생각하지 못했음.

### 시간 복잡도
<!-- 분석 -->
O(m + n)

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
