import sys
input = sys.stdin.readline

n = int(input().strip())
tri = [list(map(int, input().split())) for _ in range(n)]

# 바닥 행을 기준으로 위로 올라가며 누적 최댓값 계산
for i in range(n - 2, -1, -1):          # i = n-2, ..., 0
    for j in range(len(tri[i])):        # j = 0..i
        tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1])

print(tri[0][0])  # 최댓값