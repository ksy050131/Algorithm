import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = int(input())

    if num % 2 == 0:
        print("even")
    else:
        print("odd")