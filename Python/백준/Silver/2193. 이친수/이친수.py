import sys

n = int(sys.stdin.readline())

# n은 최대 90이므로 충분히 크게 배열 준비
dp = [0] * (n + 1)
dp[1] = 1
if n >= 2:
    dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])