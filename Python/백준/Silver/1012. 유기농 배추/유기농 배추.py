import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def print_cab(cabbage):
    for i in range(len(cabbage)):
        for j in range(len(cabbage[0])):
            print(cabbage[i][j], end = ' ')
        print()

# 인접한 곳이 1이면 그 곳을 기준으로 또 체크를 해야함.
# dfs 사용 -> 방문 처리
def dfs (cab, x, y):
    max_x = len(cab)
    max_y = len(cab[0])
    
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return
    if cab[x][y] == 0:
        return

    cab[x][y] = 0 # 방문 처리

    dfs(cab, x, y-1)
    dfs(cab, x+1, y)
    dfs(cab, x, y+1)
    dfs(cab, x-1, y)

phase = int(input())

for _ in range(phase):
    x, y, num_of_cabbage = map(int, input().split())
    
    cabbage = [[0 for _ in range(y)] for _ in range(x)]
    
    for _ in range(num_of_cabbage):
        cx, cy = map(int, input().split())
        cabbage[cx][cy] = 1
    
    worms = 0
    # print_cab(cabbage)
    for i in range(x):
        for j in range(y):
            if cabbage[i][j] == 1:
                dfs(cabbage, i, j)
                worms += 1
    
    print(worms)