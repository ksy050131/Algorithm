start, end = map(int, input().split())

numList = []
i = 1

while len(numList) < 1000:
    for j in range(i):
        numList.append(i)
    i += 1
    
print(sum(numList[start - 1:end]))