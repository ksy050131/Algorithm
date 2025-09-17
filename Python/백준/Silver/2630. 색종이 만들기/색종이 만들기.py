import sys

input = sys.stdin.readline

width = int(input())

square = []
for _ in range(width):
    line = list(map(int, input().split()))
    square.append(line)

# 칸 쪼개서 검사 -> 다 0 or 1이면 count += 1하고 끝내기
# 하나라도 다른 숫자가 있으면 다시 쪼개서 검사

b = 0 # 1
w = 0 # 0
def split_sq(width: int, x: int, y: int, sq):
    global w, b

    half = width // 2

    if width == 1:
        if sq[x][y] == 0: w += 1
        else: b += 1
        return
    
    base = sq[x][y] # 0 or 1

    for i in range(x, x + width):
        for j in range(y, y + width):
            if sq[i][j] != base:
                split_sq(half, x, y, sq)
                split_sq(half, x + half, y, sq)
                split_sq(half, x, y + half, sq)
                split_sq(half, x + half, y + half, sq)
                return # 분할했으면 그냥 끝내라

    if base == 0:
        w += 1
    else: b += 1
    return

split_sq(width, 0, 0, square)
print(f"{w}\n{b}")