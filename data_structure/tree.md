# 트리 (Tree)

## 개념
<img src="https://velog.velcdn.com/images/stresszero/post/9b30760e-e855-456e-a0a1-af2dcba0f2cf/image.png" width="500">
<img src="https://velog.velcdn.com/images/stresszero/post/bee4a4b6-0741-4c6a-a9db-d38455858414/image.webp" width="500">

- 계층적 구조를 표현하는 자료구조
- 노드(Node)와 간선(Edge)로 구성
- 루트(Root) 노드를 시작으로 하여 계층적 구조를 표현
- 노드의 최상위 노드를 루트 노드(Root Node)라고 함
- 루트 노드를 제외한 노드를 내부 노드(Internal Node)라고 함
- 루트 노드를 제외한 노드를 외부 노드(External Node)라고 함
- 노드의 최하위 노드를 리프 노드(Leaf Node)라고 함
- 노드의 최상위 노드를 루트 노드(Root Node)라고 함
- 루트 노드를 제외한 노드를 내부 노드(Internal Node)라고 함
- 루트 노드를 제외한 노드를 외부 노드(External Node)라고 함

## 트리 자료구조 2가지 대응법
- 문제를 풀 때에는 아래 부모, 자식 두 개의 트리구조를 모두 만들어두고 풀면 편리하다.
```
       0           # 루트노드 레벨 0
    /  |  \        # 간선
   1   2    5      # 레벨 1
  / \  |  /  | \   # 간선
 3  4  6  7  8  9  # 리프노드 레벨 2
```
### 1. 부모를 저장
```python
# 배열 하나에 트리를 저장
#          0  1  2  3  4  5  6  7  8  9
parent = [-1, 0, 0, 1, 1, 0, 2, 5, 5, 5]
```
### 2. 자식을 저장
```python
# 배열의 배열
children = [
    [1, 2, 5], # 0번 노드의 자식들
    [3, 4], # 1번 노드의 자식들
    [6], # 2번 노드의 자식들
    [], # 3번 노드의 자식들
    [], # 4번 노드의 자식들
    [7, 8, 9], # 5번 노드의 자식들
    [], # 6번 노드의 자식들
    [], # 7번 노드의 자식들
    [], # 8번 노드의 자식들
    [], # 9번 노드의 자식들
]
```

## 트리 순회
### 1. 전위 순회 (Pre-order Traversal)
```python
def pre_order(node):
    if node == -1:
        return
    print(node, end=' ')
    pre_order(children[node][0])
    pre_order(children[node][1])
```

### 2. 중위 순회 (In-order Traversal)
```python
def in_order(node):
    if node == -1:
        return
    in_order(children[node][0])
    print(node, end=' ')
    in_order(children[node][1])
```

### 3. 후위 순회 (Post-order Traversal)
```python
def post_order(node):
    if node == -1:
        return
    post_order(children[node][0])
    post_order(children[node][1])
    print(node, end=' ')
```