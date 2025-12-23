"""
격자(2D) BFS/DFS 템플릿
"""
from collections import deque

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 8방향 이동 (대각선 포함)
dx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
dy8 = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs_grid(start_x, start_y, graph, n, m):
    """
    격자에서 BFS
    """
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return visited

def bfs_distance(start_x, start_y, graph, n, m):
    """
    시작점에서 모든 칸까지의 최단 거리
    """
    distance = [[-1] * m for _ in range(n)]
    queue = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if distance[nx][ny] == -1 and graph[nx][ny] != 0:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance

def dfs_grid(x, y, graph, visited, n, m):
    """
    격자에서 DFS
    """
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] != 0:
                dfs_grid(nx, ny, graph, visited, n, m)

# 사용 예시
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 연결 요소 개수 세기
visited = [[False] * m for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            dfs_grid(i, j, graph, visited, n, m)
            count += 1

print(count)

