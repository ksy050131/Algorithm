target = int(input())

length = [2 ** i for i in range(6, -1, -1)]

cnt = 0
for i in range(len(length)):
    if target >= length[i]:
        cnt += 1
        target -= length[i]

    if target == 0:
        break
        
print(cnt)