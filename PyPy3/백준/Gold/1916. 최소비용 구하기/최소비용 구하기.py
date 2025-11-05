import sys
import heapq

input = sys.stdin.readline

city = int(input())
bus = int(input())
graph = [[] for _ in range(city+1)] # 1부터 시작하므로
distance = [float('inf')] * (city+1) # 무한의 값으로 초기화

for _ in range(bus):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # v: 도착 노드, w: 비용

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어감
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)가 나옴

        if distance[now] < dist: # 이미 입력되어있는 값이 현재 노드까지 거리보다 작으면 이미 방문한 노드임
                                # 그 전까지는 무한값이기 때문에 방문하면 당연히 거리가 작을 수밖에 없음
            continue
        
        for i in graph[now]: # graph에는 (도착 노드, 가중치) 튜플 형태로 저장되어 있음
            cost = dist + i[1]
            # 현재 노드를 거쳤을 때 이동 거리가 더 짧다 -> update
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])