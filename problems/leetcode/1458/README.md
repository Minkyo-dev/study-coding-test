---
problem_id: 1458
title: Max Dot Product of Two Subsequences
source: leetcode
url: https://leetcode.com/problems/1458
difficulty: Hard
algorithms: [dp]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Max Dot Product of Two Subsequences

## 문제
Given two arrays nums1 and nums2.
nums1, nums2 두개의 배열이 주어진다.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
비어있지 않은 nums1, nums2의 부분 수열(subsequence) 중에서, 점곱(dot product)의 최댓값을 반환하시오.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
배열의 부분 수열은 원래 배열에서 일부 원소를 제거하여 만들어진 새로운 배열이다. 관계를 유지하면서 순서를 유지하면서 제거한 배열이다. (예: [2,3,5]는 [1,2,3,4,5]의 부분 수열이지만, [1,5,3]는 부분 수열이 아니다.)


## 입력
- 1 <= nums1.length, nums2.length <= 500
- -1000 <= nums1[i], nums2[i] <= 1000

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```python
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
```

### 출력 1
```python
18
# Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
```

### 입력 2
```python
nums1 = [3,-2]
nums2 = [2,-6,7]
```

### 출력 2
```python
21
# Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
```

### 입력 3
```python
nums1 = [-1,-1]
nums2 = [1,1]
```

### 출력 3
```python
-1
# Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.
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
### 단어 정리
- dot product:
- product : 곱
- subsequence : 수열열

### Dot Product (내적) 정의

길이가 같은 두 수열(또는 벡터)

- `A = [a1, a2, ..., ak]`
- `B = [b1, b2, ..., bk]`

이 있을 때, **dot product**는 다음과 같이 계산됩니다.

$$
A \cdot B = a_1 b_1 + a_2 b_2 + \cdots + a_k b_k
$$

즉, **같은 인덱스에 있는 원소끼리 곱한 뒤, 그 결과를 모두 더한 값**을 의미합니다.

### 해설
https://github.com/doocs/leetcode/blob/main/solution/1400-1499/1458.Max%20Dot%20Product%20of%20Two%20Subsequences/README_EN.md