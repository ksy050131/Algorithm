# 1 1 2 2 2 8
# 0 1 2 2 2 7
chess = [1, 1, 2, 2, 2, 8]
input = list(map(int, input().split()))
result = [chess[i] - input[i] for i in range(6)]

for j in range(6):
    print(result[j], end = ' ')