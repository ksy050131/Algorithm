# dp[i] = "i번째 원소로 끝나는 가장 긴 감소 부분수열 길이"

import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [1] * n 

for i in range(n):
    for j in range(i):
        if seq[j] > seq[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))