import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()

elem = []
elemlist = []
def dfs(depth: int):
    if depth == m:
        elemlist.append(' '.join(map(str, elem)))
        return
    
    prev = None
    for i in range(n):
        if numlist[i] == prev: continue
        
        elem.append(numlist[i])
        prev = numlist[i]
        dfs(depth + 1)
        elem.pop()

dfs(0)
print('\n'.join(elemlist))