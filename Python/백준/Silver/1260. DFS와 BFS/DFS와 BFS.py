import sys
from collections import defaultdict, deque

input = sys.stdin.readline

graph = defaultdict(list)

N, M, V = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 이므로

for node in graph:
    graph[node].sort() # 정점 번호가 작은 것부터 방문해야하니 sort

def dfs(v, visited):
    visited.add(v) # 방문한 정점 저장

    print(v, end = ' ')
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited)

def bfs(v, visited):
    queue = deque([v])
    visited.add(v)

    while queue:
        current = queue.popleft()
        print(current, end = ' ')

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

dfs(V, set())
print()

bfs(V, set())