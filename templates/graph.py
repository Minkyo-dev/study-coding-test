"""
그래프 템플릿
"""
from collections import deque, defaultdict

# 1. 인접 리스트 (기본)
n, m = 5, 6  # 노드 수, 간선 수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 2. 인접 리스트 (가중치)
graph_weighted = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph_weighted[a].append((b, cost))

# 3. 인접 행렬
INF = int(1e9)
adj_matrix = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    adj_matrix[i][i] = 0

# 4. DFS
def dfs(node, visited):
    visited[node] = True
    print(node, end=' ')
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited)

# 5. BFS
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

# 6. 최단 거리 BFS
def bfs_distance(start):
    distance = [-1] * (n + 1)
    queue = deque([start])
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                queue.append(next_node)

    return distance

