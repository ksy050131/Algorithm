import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()

elem = []
elemlist = []

def dfs(depth: int, idx: int):
    if depth == m:
        elemlist.append(' '.join(map(str, elem)))
        return
    
    for i in range(idx, n):
        elem.append(numlist[i])
        dfs(depth + 1, i)
        elem.pop()

dfs(0, 0)
print('\n'.join(elemlist))