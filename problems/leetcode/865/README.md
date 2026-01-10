---
problem_id: 865
title: Smallest Subtree with all the Deepest Nodes
source: leetcode
url: https://leetcode.com/problems/865
difficulty: Medium
algorithms: [bfs-dfs]
companies: []
solved: false
solved_date: null
retry_count: 0
time_complexity: ""
space_complexity: ""
---

# Smallest Subtree with all the Deepest Nodes

## 문제
Given the root of a binary tree, the depth of each node is the shortest distance to the root.
바이너리 트리가 주어진다. 각 노드의 깊이는 루트로부터 가장 짧은 거리를 의미한다.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.
반환하는 서브트리는 가장 깊은 노드를 모두 포함하는 가장 작은 서브트리이다.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.
가장 깊은 노드는 모든 노드 중에서 가장 깊은 노드이다.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
노드의 서브트리는 해당 노드와 모든 자손 노드로 구성된 트리이다.

## 입력
- The number of nodes in the tree will be in the range [1, 500].
- 0 <= Node.val <= 500
- The values of the nodes in the tree are unique.

## 출력
<!-- 출력 형식 -->

## 예제

### 입력 1
<img src="./sketch1.png" width="300px">

```python
root = [3,5,1,6,2,0,8,null,null,7,4]
```

### 출력 1
```python
[2,7,4]

# We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
```

### 입력 2
```python
root = [1]
```

### 출력 2
```python
[1]
# The root is the deepest node in the tree.
```

### 입력 3
```python
root = [0,1,3,null,2]
```

### 출력 3
```python
[2]
# The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
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
