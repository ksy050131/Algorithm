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
    global unriped_cnt
    max_day = 0
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        r, c = q.popleft()

        for i, j in zip(dr, dc):
            nr = r + i
            nc = c + j

            if 0 <= nr < height and 0 <= nc < width:
                if tomato[nr][nc] == 0:
                    unriped_cnt -= 1
                    tomato[nr][nc] = tomato[r][c] + 1
                    max_day = max(max_day, tomato[nr][nc]) # 매번 갱신
                    q.append((nr, nc))

unriped_cnt = 0
cnt = True

for i in range(height):
    for j in range(width):
        if tomato[i][j] == 1:
            q.append((i, j))
        elif tomato[i][j] == 0:
            unriped_cnt += 1
            cnt = False

# 다 익어있으므로 0          
if cnt:
    print(0)
else:
    bfs()

    if unriped_cnt > 0: # 안 익은 토마토가 남아있으므로
        print(-1)
    else:
        max_val = max(map(max, tomato))
        print(max_val - 1) # 1에서부터 시작했으므로 -1 해야함