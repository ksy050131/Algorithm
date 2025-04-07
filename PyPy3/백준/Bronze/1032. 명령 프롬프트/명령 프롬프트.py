fileCnt = int(input())

file = list(input())
if fileCnt == 1:
    print(''.join(file))
else:
    for _ in range(fileCnt - 1):
        compareFile = list(input())
      
        # file 하고 compareFile 비교 -> 다른 부분 ?으로 바꾸기
        for idx in range(len(file)):
            if file[idx] != compareFile[idx]:
                file[idx] = "?"
    
    print(''.join(file))