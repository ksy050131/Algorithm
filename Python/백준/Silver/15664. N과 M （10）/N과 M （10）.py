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
    
    prev = None
    for i in range(idx, n):
        if prev == numlist[i]: continue
    
        elem.append(numlist[i])
        prev = numlist[i] # numlist[i]를 prev에 저장하여 중복된 값이 들어가지 않도록

        dfs(depth+1, i+1)
        elem.pop()

dfs(0, 0)
print('\n'.join(elemlist))