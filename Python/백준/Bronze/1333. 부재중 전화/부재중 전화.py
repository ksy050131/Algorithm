import sys
input = sys.stdin.readline

numOfSong, lengthOfSong, cycleOfBell = map(int, input().split())

# 노래 재생 구간: [start, start + lengthOfSong)
busy_intervals = []
for i in range(numOfSong):
    start = i * (lengthOfSong + 5)
    end = start + lengthOfSong
    busy_intervals.append((start, end))

time = 0
while True:
    can_receive = True
    for start, end in busy_intervals:
        if start <= time < end:
            can_receive = False
            break
    if can_receive:
        print(time)
        break
    time += cycleOfBell