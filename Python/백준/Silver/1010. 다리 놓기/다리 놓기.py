import sys

input = sys.stdin.readline

# 0-30까지 인덱스 쓸 거니까 31로 초기화
dp = [[0] * 31 for _ in range(31)]

# 조합 미리 계산
for n in range(31):
    dp[n][0] = 1
    dp[n][n] = 1

    for k in range(1, n):
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k]
    
N = int(input())

for _ in range(N):
    left, right = map(int, input().split())
    print(dp[right][left])