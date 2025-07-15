import sys

input = sys.stdin.readline

N = int(input())
N = list(str(N))
N.reverse()
new = []

for i in range(len(N)):
    new.append(N[i])
    if i != len(N) - 1 and i % 3 == 2:
        new.append(',')

new.reverse()
for i in range(len(new)):
    print(new[i], end = '')