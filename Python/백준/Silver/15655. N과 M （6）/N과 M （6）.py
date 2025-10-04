import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numlist = list(map(int, input().split()))
numlist.sort()
elem = []
elemlist = []

# 매개변수 idx를 추가하여 idx 이후의 숫자만 list에 넣도록 제한함.
def dfs(depth: int, idx: int):
    if depth == m:
        elemlist.append(' '.join(map(str, elem)))
        return
    
    for i in range(idx, n):
        elem.append(numlist[i])
        dfs(depth + 1, i + 1)
        elem.pop()

dfs(0, 0)
print('\n'.join(elemlist))