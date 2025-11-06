import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [float('inf')] * (v+1)

# 간선 입력 받기
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# print(*graph)

def dijkstra(start: int): # (cost, node)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작 노드와의 거리는 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue # 원래 값: inf인데 더 작으면 방문을 했다는 뜻

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for item in distance[1:]:
    if item == float('inf'): print('INF')
    else: print(item)