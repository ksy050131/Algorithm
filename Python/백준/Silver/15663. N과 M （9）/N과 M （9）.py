import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()

elem = []
elemlist = []
visited = n * [False]

# print(visited)

def dfs():
    if len(elem) == m:
        print(*elem)
        return

    prev = None

    for i in range(n):
        if visited[i]: continue
        if numlist[i] == prev: continue # 같은 깊이에서 중복 제거

        visited[i] = True
        
        elem.append(numlist[i])
        # print(f"index: {i}, visited: {visited[i]}") 디버깅
        dfs()
        elem.pop()

        visited[i] = False
        prev = numlist[i]

dfs()