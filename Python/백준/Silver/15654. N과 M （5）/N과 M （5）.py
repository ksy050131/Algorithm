import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numlist = list(map(int, input().split()))
numlist = sorted(numlist)
# print(numlist)

l = []
visited = [False] * n

def dfs(start_idx: int):
    if len(l) == m:
        print(*l)
        return

    for i in range(n):
        if numlist[i] not in l:
            l.append(numlist[i])
            dfs(i + 1)
            l.pop()

dfs(0)