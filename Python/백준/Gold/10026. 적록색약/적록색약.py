import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(m, x, y, target):
    max_x = len(m)
    max_y = len(m[0])
    
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return

    if m[x][y] != target:
        return
        
    m[x][y] = '0' # 방문 표시

    dfs(m, x, y-1, target)
    dfs(m, x+1, y, target)
    dfs(m, x, y+1, target)
    dfs(m, x-1, y, target)
    
N = int(input())

area = []

for i in range(N):
        s = input().strip()
        area.append(list(s))

# 색약용 복사 맵
color_b_area = [row[:] for row in area] 

for i in range(N):
    for j in range(N):
        if color_b_area[i][j] == 'G':
            color_b_area[i][j] = 'R'

normal = 0
color_b = 0

for i in range(N):
    for j in range(N):
        if area[i][j] != '0':
            dfs(area, i, j, area[i][j])
            normal += 1

for i in range(N):
    for j in range(N):
        # 적록색약
        if color_b_area[i][j] != '0':
            dfs(color_b_area, i, j, color_b_area[i][j])
            color_b += 1
        
print(normal, color_b)