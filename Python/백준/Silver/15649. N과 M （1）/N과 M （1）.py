import sys

input = sys.stdin.readline

n, m = map(int, input().split())

elem = []
visited = (n + 1) * [False]

def dfs(depth: int):
    if depth == m:
        print(*elem)
        return

    for i in range(1, n + 1):
        if visited[i]: continue

        visited[i] = True
        elem.append(i)
        dfs(depth + 1)
        elem.pop()

        visited[i] = False

dfs(0)