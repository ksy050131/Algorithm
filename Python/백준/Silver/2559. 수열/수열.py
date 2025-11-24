import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

temp_sum = sum(temp[:k])
max_sum = temp_sum

# 시작
l = 0
r = k - 1
while (r < len(temp) - 1):
    temp_sum -= temp[l]
    l += 1
    r += 1
    temp_sum += temp[r]

    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)