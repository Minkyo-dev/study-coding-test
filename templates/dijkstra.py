"""
다익스트라 최단 경로 알고리즘
"""
import heapq

def dijkstra(start, graph, n):
    """
    시작 노드에서 모든 노드까지의 최단 거리
    graph: [[(노드, 비용), ...], ...]
    """
    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[start] = 0

    heap = [(0, start)]  # (거리, 노드)

    while heap:
        dist, node = heapq.heappop(heap)

        # 이미 처리된 노드
        if distance[node] < dist:
            continue

        for next_node, cost in graph[node]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return distance

# 사용 예시
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = dijkstra(start, graph, n)
print(result)

