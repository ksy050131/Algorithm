# bfs
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maplist = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

# # print
# for i in range(n):
#     print(*maplist[i])

q = deque()

def bfs():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        r, c = q.popleft()

        for i, j in zip(dr, dc):
            nr = r + i
            nc = c + j

            # distance값이 -1 => 방문하지 않은 것
            if 0 <= nr < n and 0 <= nc < m:
                if maplist[nr][nc] != 0 and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1 
                    q.append((nr, nc))

# 2까지의 최단 거리를 측정하므로 2를 시작점으로 삼아서 계산      
for i in range(n):
    for j in range(m):
        if maplist[i][j] == 2:
            q.append((i, j))
            distance[i][j] = 0
bfs()

for i in range(n):
    for j in range(m):
        if maplist[i][j] == 0:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()