import sys

input = sys.stdin.readline

def streakCheck(streakCount, cnt):
    if streakCount >= 2:
        cnt += 1

    return streakCount, cnt

N = int(input().strip())

room = []
for _ in range(N):
    room.append(list(input()))

vert = 0
horz = 0

# print
# for i in range(N):
#     for j in range(N):
#         print(room[i][j], end = '')
#     print()

for i in range(N):
    streakCount = 0
    
    for j in range(N):
        if room[i][j] == 'X':
            streakCount, horz = streakCheck(streakCount, horz)
            streakCount = 0
        else:
            streakCount += 1
    streakCount, horz = streakCheck(streakCount, horz)

# column 수행
for i in range(N):
    streakCount = 0
    
    for j in range(N):
        if room[j][i] == 'X':
            streakCount, vert = streakCheck(streakCount, vert)
            streakCount = 0
        else:
            streakCount += 1
    streakCount, vert = streakCheck(streakCount, vert)

print(horz, vert)