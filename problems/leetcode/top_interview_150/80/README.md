---
problem_id: 80
title: Remove Duplicates from Sorted Array II
source: leetcode
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
difficulty: medium
algorithms: [array, two-pointers]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Remove Duplicates from Sorted Array II

## 문제
Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k`* after placing the final result in the first *`k`* slots of *`nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array in-place** with O(1) extra memory.

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
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing** order.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
nums = [1,1,1,2,2,3]
```

### 출력 1
```
5, nums = [1,1,2,2,3,_]
```

> Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
> It does not matter what you leave beyond the returned k (hence they are underscores).

### 입력 2
```
nums = [0,0,1,1,1,1,2,3,3]
```

### 출력 2
```
7, nums = [0,0,1,1,2,3,3,_,_]
```

> Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
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
This is a pointer problem. I need to use two pointers to solve this problem. The first pointer is the writer pointer, which is used to write the next unique element. The second pointer is the scanner pointer, which is used to scan the array. When I solve this problem, I couldn't think about the counter variable. 
