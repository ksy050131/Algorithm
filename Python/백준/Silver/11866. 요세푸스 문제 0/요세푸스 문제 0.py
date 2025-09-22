import sys

input = sys.stdin.readline

n, k = map(int, input().split())
queue = [i for i in range(1, n + 1)]

result = []
idx = 0

for _ in range(n):
    idx = (idx + k - 1) % len(queue) # pop으로 queue크기는 변함
    result.append(queue.pop(idx))
    # print(f"queue: {queue}")
    # print(f"result: {result}")

print("<" + ", ".join(map(str, result)) + ">")