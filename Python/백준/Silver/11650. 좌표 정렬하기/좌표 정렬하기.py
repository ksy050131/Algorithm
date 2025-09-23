import sys

input = sys.stdin.readline

n = int(input())
coord = []

for _ in range(n):
    token = tuple(map(int, input().split()))
    coord.append(token)

coord.sort(key=lambda x: (x[0], x[1]))

for t in coord:
    print(*t)