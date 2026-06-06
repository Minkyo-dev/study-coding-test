---
problem_id: 380
title: Insert Delete GetRandom O(1)
source: leetcode
url: https://leetcode.com/problems/insert-delete-getrandom-o1
difficulty: medium
algorithms: [array, hash-table, math, design, randomized]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Insert Delete GetRandom O(1)

## 문제
Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

## 입력
- `-2^31 <= val <= 2^31 - 1`
- At most `2 * ``10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when `getRandom` is called.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
```

### 출력 1
```
[null, true, false, true, 2, true, false, 2]
```

> RandomizedSet randomizedSet = new RandomizedSet();
> randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
> randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
> randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
> randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
> randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
> randomizedSet.insert(2); // 2 was already in the set, so return false.
> randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

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
