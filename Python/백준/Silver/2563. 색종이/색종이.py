n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())

    for tx in range(x, x + 10):
        for ty in range(y, y + 10):
            if tx >= 100 or ty >= 100: break

            paper[tx][ty] = 1

sum = 0
for row in range(100):
    sum += paper[row].count(1)

print(sum)