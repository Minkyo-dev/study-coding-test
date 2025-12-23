---
problem_id: "43165"
title: "타겟 넘버"
source: programmers
url: https://school.programmers.co.kr/learn/courses/30/lessons/43165
difficulty: level2
algorithms: [dfs, bfs, backtracking]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# 타겟 넘버

## 문제

n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.

예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음과 같이 5가지 방법을 쓸 수 있습니다.

```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한사항

- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

## 입출력 예

| numbers | target | return |
|---------|--------|--------|
| [1, 1, 1, 1, 1] | 3 | 5 |
| [4, 1, 2, 1] | 4 | 2 |

## 풀이

### 접근

각 숫자마다 +와 -를 선택할 수 있으므로 DFS나 BFS로 모든 경우를 탐색한다.

**방법 1: DFS**
- 현재 인덱스와 현재까지의 합을 인자로 재귀 호출
- 마지막 인덱스에 도달했을 때 target과 같으면 카운트

**방법 2: BFS**
- 큐에 (인덱스, 현재 합)을 저장
- 각 단계에서 +, - 두 가지 경우를 큐에 추가

**방법 3: DP**
- dp[i][sum] = i번째까지 사용해서 sum을 만드는 경우의 수

### 시간 복잡도

- DFS/BFS: O(2^N) - 각 숫자마다 2가지 선택
- N ≤ 20이므로 2^20 = 1,048,576으로 충분히 가능

## 코드

### DFS 풀이

```python
def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer

        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return

        # 더하기
        dfs(index + 1, current_sum + numbers[index])
        # 빼기
        dfs(index + 1, current_sum - numbers[index])

    dfs(0, 0)
    return answer
```

### BFS 풀이

```python
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])  # (인덱스, 합)

    while queue:
        index, current_sum = queue.popleft()

        if index == len(numbers):
            if current_sum == target:
                answer += 1
            continue

        # 더하기와 빼기 두 경우 추가
        queue.append((index + 1, current_sum + numbers[index]))
        queue.append((index + 1, current_sum - numbers[index]))

    return answer
```

## 회고

DFS/BFS의 기본 문제. 완전 탐색이지만 N이 작아서 시간 내에 해결 가능.

