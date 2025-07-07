import sys

input = sys.stdin.readline

num, phase = map(int, input().split())
num_list = list(map(int, input().split()))

prefix_sum = [0] * (num + 1)

for i in range(1, num + 1):
        prefix_sum[i] = prefix_sum[i - 1] + num_list[i - 1]


for _ in range(phase):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])