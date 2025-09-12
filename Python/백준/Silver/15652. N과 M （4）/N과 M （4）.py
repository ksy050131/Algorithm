import sys

input = sys.stdin.readline

# 1부터 n까지 자연수 중에서 m개를 고른 수열
n, m = map(int, input().split())

tmp = []

def dfs(start):
    if len(tmp) == m:
        print(*tmp)
        return

    for i in range(start, n + 1):
        if i == 0: continue
        tmp.append(i)
        dfs(i) # 중복을 허용함!! i 부터 다시 탐색하도록
        tmp.pop()

dfs(1)