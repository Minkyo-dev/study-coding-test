---
problem_id: 135
title: Candy
source: leetcode
url: https://leetcode.com/problems/candy
difficulty: hard
algorithms: [array, greedy]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Candy

## 문제
There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return *the minimum number of candies you need to have to distribute the candies to the children*.

## 입력
- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
ratings = [1,0,2]
```

### 출력 1
```
5
```

> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

### 입력 2
```
ratings = [1,2,2]
```

### 출력 2
```
4
```

> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
> The third child gets 1 candy because it satisfies the above two conditions.

### 임력 3
```
ratings = [1,3,2,2,1]
```

### 출력 3
```
7
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
I couldn't identify I need to use two pass.
