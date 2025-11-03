import sys

input = sys.stdin.readline

size, case = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(size)]

# 1-based로 누적합을 구하기 위해 한 칸씩 더 만듦
dp = [[0] * (size+1) for _ in range(size+1)] 

for i in range(1, size + 1):
    for j in range(1, size + 1):
        dp[i][j] = num[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(case):
    sx, sy, ex, ey = map(int, input().split())
    ans = dp[ex][ey] - dp[sx-1][ey] - dp[ex][sy-1] + dp[sx-1][sy-1]
    print(ans)