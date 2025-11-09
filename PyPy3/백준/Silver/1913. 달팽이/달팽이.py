import sys

input = sys.stdin.readline

n = int(input())
target = int(input())

maplist = [[0] * n for _ in range(n)]

def find(target, elem):
    if target == elem: return True
    else: return False
    
# start
num = n * n
x, y = 0, 0
t_x, t_y = 0, 0

# 가로로 움직이기 -> 4부터
# 세로로 움직이기 -> 5부터 
# 세로 -> 가로
row = n

while (num > 0):
    # 홀수
    if row % 2 != 0:
        for i in range(row):
            maplist[x][y] = num
            if find(target, num): t_x, t_y = x, y
            x += 1
            num -= 1
        x -= 1
        y += 1

        for j in range(row - 1):
            maplist[x][y] = num
            if find(target, num): t_x, t_y = x, y
            y += 1
            num -= 1

        x -= 1
        y -= 1

    else:
        for i in range(row):
            maplist[x][y] = num
            if find(target, num): t_x, t_y = x, y
            x -= 1
            num -= 1
        x += 1
        y -= 1

        for j in range(row-1):
            maplist[x][y] = num
            if find(target, num): t_x, t_y = x, y
            y -= 1
            num -= 1
        
        x += 1
        y += 1

    row -= 1


for l in range(n):
    print(*maplist[l])
print(t_x + 1, t_y + 1)