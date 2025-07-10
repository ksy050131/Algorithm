import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1) 

dp[1] = 0

for i in range(2, N + 1):
    # 기본을 i - 1에서 1 더한 것으로 설정
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # elif이 아닌 if 쓰는 이유: 6 처럼 2, 3 둘 다 나누어지는 수일 때 둘 다 검사해야함
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])