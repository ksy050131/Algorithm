import sys

input = sys.stdin.readline

def returnTimeSchedule(timeList):
    listArr = []
    
    for i in range(len(timeList)):
        listArr.append(sum(timeList[:i + 1]))

    return listArr

numOfPeople = int(input())
timeList = list(map(int, input().split()))
# print(timeList)

timeSchedule = returnTimeSchedule(sorted(timeList))
# print(timeSchedule)
print(sum(timeSchedule))