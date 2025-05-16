import sys

input = sys.stdin.readline

numOfConf = int(input())
meetings = []

for _ in range(numOfConf):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간 기준으로 정렬해야함.
# 끝나는 시간이 빠르면 더 많은 회의를 넣을 수 있음.
# 가장 빨리 끝나는 회의를 선택해야 전체 회의 수를 늘릴 수 있음

meetings.sort(key=lambda x: (x[1], x[0])) 

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)