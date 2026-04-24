---
problem_id: 26
title: Remove Duplicates from Sorted Array
source: leetcode
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array
difficulty: easy
algorithms: [array, two-pointers]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Remove Duplicates from Sorted Array

## 문제
Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of *unique elements* in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

## 입력
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums = [1,1,2]
```

### 출력 1
```
2, nums = [1,2,_]
```

> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
> It does not matter what you leave beyond the returned k (hence they are underscores).

### 입력 2
```
nums = [0,0,1,1,1,2,2,3,3,4]
```

### 출력 2
```
5, nums = [0,1,2,3,4,_,_,_,_,_]
```

> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
> It does not matter what you leave beyond the returned k (hence they are underscores).

## 풀이

### 접근
<!-- 문제 해결 전략 -->
The most important aspect is understanding what `k` represents: it is the number of unique elements in the array. You need to decide how to determine the value of `k` during the process.

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
