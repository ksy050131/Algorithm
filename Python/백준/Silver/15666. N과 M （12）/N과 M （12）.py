import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numlist = list(map(int, input().split()))
numlist.sort()

tmp = []
def dfs(start):
    if len(tmp) == m:
        print(*tmp)
        return
    
    prev = None
    
    for i in range(start, n):
        if numlist[i] == prev: continue

        tmp.append(numlist[i])
        dfs(i)
        tmp.pop()

        prev = numlist[i]

dfs(0)