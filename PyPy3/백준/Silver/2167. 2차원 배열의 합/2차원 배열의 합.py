import sys

row, col = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    startRow, startCol, endRow, endCol = map(int, sys.stdin.readline().split())

    sum = 0
    for i in range(startRow - 1, endRow):
        for j in range(startCol - 1, endCol):
            sum += arr[i][j]

    print(sum)