# bfs

import sys
from collections import deque

input = sys.stdin.readline

width, height = map(int, input().split())

tomato = []
for _ in range(height):
    line = list(map(int, input().split()))
    tomato.append(line)

# # print
# for i in range(height):
#     print(*tomato[i])

q = deque()

def bfs():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        r, c = q.popleft()

        for i, j in zip(dr, dc):
            nr = r + i
            nc = c + j

            if 0 <= nr < height and 0 <= nc < width:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = tomato[r][c] + 1
                    q.append((nr, nc))

cnt = True
for i in range(height):
    for j in range(width):
        if tomato[i][j] == 1:
            q.append((i, j))
        elif tomato[i][j] == 0:
            cnt = False

# 다 익어있으므로 0          
if cnt:
    print(0)
else:
    bfs()

    any_zero = any(0 in row for row in tomato)
    if any_zero:
        print(-1)
    else:
        max_val = max(map(max, tomato))
        print(max_val - 1) # 1에서부터 시작했으므로 -1 해야함