# 1
# 00, 11
# 001, 111 2에서 1만 붙임, 100 
# 0000, 1100 2에서 00 붙임, 0011, 1111, 1001, 3에서 1붙임

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

if n > 1:
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])