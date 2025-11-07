import sys
import heapq

input = sys.stdin.readline

city, m, targetDist, start = map(int, input().split())

graph = [[] for _ in range(city + 1)]
distance = [float('inf')] * (city + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append((v, 1))

def find_city(start: int):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

find_city(start)
# print(distance)

flag = 1
for idx, val in enumerate(distance):
    if val == targetDist:
        flag = 0
        print(idx)
if flag == 1:
    print(-1)