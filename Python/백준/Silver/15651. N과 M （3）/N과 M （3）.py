import sys

input = sys.stdin.readline

n, m = map(int, input().split())

visited = (n + 1) * [False]
elem = []
elemlist = []

def dfs(depth: int):
    if depth == m:
        elemlist.append(' '.join(map(str, elem)))
        return

    for i in range(1, n + 1):
        elem.append(i)
        dfs(depth + 1)
        elem.pop()

dfs(0)
print('\n'.join(elemlist))