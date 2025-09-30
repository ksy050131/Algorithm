# dp[i] = "i번째 원소로 끝나는 가장 긴 증가 부분수열 길이"

import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [1] * n # 자기자신만으로 길이 1짜리 증가 부분수열을 만들 수 있으므로

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))