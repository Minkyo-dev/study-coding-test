---
problem_id: 27
title: Remove Element
source: leetcode
url: https://leetcode.com/problems/remove-element
difficulty: easy
algorithms: [array, two-pointers]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Remove Element

## 문제
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return *the number of elements in *`nums`* which are not equal to *`val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

## 입력
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums = [3,2,2,3], val = 3
```

### 출력 1
```
2, nums = [2,2,_,_]
```

> Your function should return k = 2, with the first two elements of nums being 2.
> It does not matter what you leave beyond the returned k (hence they are underscores).

### 입력 2
```
nums = [0,1,2,2,3,0,4,2], val = 2
```

### 출력 2
```
5, nums = [0,1,4,0,3,_,_,_]
```

> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
> Note that the five elements can be returned in any order.
> It does not matter what you leave beyond the returned k (hence they are underscores).

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
