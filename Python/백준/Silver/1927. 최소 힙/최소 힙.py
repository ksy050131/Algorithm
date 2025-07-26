import sys, heapq

input = sys.stdin.readline

heap = []

phase = int(input())

for _ in range(phase):
    command = int(input())

    if command != 0:
        heapq.heappush(heap, command)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)