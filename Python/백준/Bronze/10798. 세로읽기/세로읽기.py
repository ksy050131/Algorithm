mtx = []
maxlist = float("-inf")

for row in range(5):
    row = list(input())
    mtx.append(row)

    if len(row) > maxlist:
        maxlist = len(row)

for col in range(maxlist):
    for row in range(5):
        try:
            print(mtx[row][col], end = '')
        except IndexError:
            continue