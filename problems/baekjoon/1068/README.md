---
problem_id: 1068
title: 트리
source: baekjoon
url: https://www.acmicpc.net/problem/1068
difficulty: gold5
algorithms: [bfs-dfs,tree]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# 트리

## 문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.

<img src="https://upload.acmicpc.net/560de878-d961-475e-ada4-e1f0774e5a84/-/preview/" width="300" />

현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.

<img src="https://upload.acmicpc.net/d46ddf4e-1b82-44cc-8c90-12f76e5bf88f/-/preview/" width="300" />

이제 리프 노드의 개수는 1개이다.


## 입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

## 출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

## 예제

### 입력 1
```
5
-1 0 0 1 1
2
```

### 출력 1
```
2
```

### 입력 2
```
5
-1 0 0 1 1
1
```

### 출력 2
```
1
```

### 입력 3
```
5
-1 0 0 1 1
0
```

### 출력 3
```
0
```

### 입력 4
```
9
-1 0 0 2 2 4 4 6 6
4
```

### 출력 4
```
2
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
