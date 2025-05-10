import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결 수

adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # 무방향 그래프

count = 0

def dfs(v):
    global count
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            count += 1
            dfs(neighbor)

dfs(1)
print(count)