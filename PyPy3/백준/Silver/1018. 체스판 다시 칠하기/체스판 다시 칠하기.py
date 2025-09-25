import sys

input = sys.stdin.readline

row, col = map(int, input().split())

chess = []

for _ in range(row):
    line = list(input().strip())
    chess.append(line)

 # i 부터 i + 8까지
# 왼쪽 위가 B라고 가정 => 불일치 개수 cntB
# 반대(왼쪽 위가 W라고 가정)는 다 계산한 뒤 64 - cntB
result = []

for i in range(row - 7):
    for j in range(col - 7):
        cntB = 0
        for r in range(8):
            for c in range(8):
                expected = 'B' if ((r + c) % 2 == 0) else 'W'
                if chess[i + r][j + c] != expected:
                    cntB += 1

        result.append(min(cntB, 64 - cntB))

print(min(result))