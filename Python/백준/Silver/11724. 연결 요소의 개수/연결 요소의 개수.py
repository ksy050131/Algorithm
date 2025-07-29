import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(graph, visited, node):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)
            
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u) # 양방향이니까

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, visited, i)
        count += 1

print(count)