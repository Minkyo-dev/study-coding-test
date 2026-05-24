---
problem_id: 122
title: Best Time to Buy and Sell Stock II
source: leetcode
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
difficulty: medium
algorithms: [array, dynamic-programming, greedy]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Best Time to Buy and Sell Stock II

## 문제
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can sell and buy the stock multiple times on the **same day**, ensuring you never hold more than one share of the stock.

Find and return *the **maximum** profit you can achieve*.

## 입력
- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```
prices = [7,1,5,3,6,4]
```

### 출력 1
```
7
```

> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
> Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
> Total profit is 4 + 3 = 7.

### 입력 2
```
prices = [1,2,3,4,5]
```

### 출력 2
```
4
```

> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
> Total profit is 4.

### 입력 3
```
prices = [7,6,4,3,1]
```

### 출력 3
```
0
```

> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

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
