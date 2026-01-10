---
problem_id: 712
title: Minimum ASCII Delete Sum for Two Strings
source: leetcode
url: https://leetcode.com/problems/712
difficulty: Medium
algorithms: [dp]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Minimum ASCII Delete Sum for Two Strings

## 문제
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
주어진 두개의 문자열 s1, s2를 같게 만들기 위해 삭제해야 하는 문자의 ASCII 합의 최솟값을 반환하시오.

## 입력
- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of lowercase English letters.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
```python
s1 = "sea"
s2 = "eat"
```

### 출력 1
```python
231
# Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```

### 입력 2
```python
s1 = "delete"
s2 = "leet"
```

### 출력 2
```python
403
# Deleting "e" from "delete" adds the ASCII value of "e" (101) to the sum.
# Deleting "e" from "leet" adds the ASCII value of "e" (101) to the sum.
# At the end, both strings are equal, and 101 + 101 = 403 is the minimum sum possible to achieve this.

# Deleting "dee" from "delete" to turn the string into "let", adds 100[d] + 101[e] + 101[e] to the sum.
# 'delete'에서 'dee'를 삭제 문자열을 'let'으로 만들기위하여, 그리고 '100[d] + 101[e] + 101[e]'를 합하기 위해 추가한다.
# Deleting "e" from "leet" adds 101[e] to the sum.
# 'leet'에서 'e'를 삭제하고, 합하기 위해 101[e]를 추가한다.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# 결과적으로 두 문자열은 'let'으로 같아지고, 결과는 100+101+101+101 = 403이다.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
# 대신에 'lee'나 'eet'으로 만들면, 433, 417을 얻을 것이므로 더 높은 값을 얻을 것이다.
```

## 풀이

### 접근
두 문자열을 같게 만들기 위해 삭제해야 하는 문자의 ASCII 값의 합이 최소가 되도록 해야 한다.  
이는 두 문자열에서 공통 부분 수열(Longest Common Subsequence, LCS)을 찾아 그 부분은 남기고, 나머지 문자를 삭제하는 최소 비용을 계산하는 문제로 바꿀 수 있다.

- **동적 계획법(DP)**을 사용한다.
  - `dp[i][j]`를 s1의 i번째 문자까지, s2의 j번째 문자까지 고려했을 때 최소 삭제 ASCII 합이라고 정의한다.
  - `s1[i-1] == s2[j-1]`인 경우, 해당 문자를 삭제할 필요 없으므로 `dp[i][j] = dp[i-1][j-1]`가 된다.
  - 다를 경우, 각각 한 문자를 삭제하는 두 가지 경우 중 최소값을 선택한다.
    - `dp[i-1][j] + ord(s1[i-1])` : s1의 문자를 삭제
    - `dp[i][j-1] + ord(s2[j-1])` : s2의 문자를 삭제

- **초기화**
  - `dp[0][j]` : s1이 비어있으므로 s2의 앞 j개 문자를 모두 삭제해야 한다(ASCII 합 누적).
  - `dp[i][0]` : s2가 비어있으므로 s1의 앞 i개 문자를 모두 삭제해야 한다.

- **최적 부분 구조 및 중복 부분 문제**의 특성으로 DP가 적합하다.
- 시간복잡도는 O(N * M) (N, M은 문자열 길이).

**핵심 포인트**  
- LCS의 긴 버전(ASCII 비용 LCS)으로 볼 수 있음.
- 완전탐색은 비효율적이므로 DP가 반드시 필요하다.


### 시간 복잡도
<!-- 분석 -->

## 코드

```python
chr(97) # -> 'a'
ord('a') # -> 97
```

## 회고
<!-- 어려웠던 점, 배운 점 -->
