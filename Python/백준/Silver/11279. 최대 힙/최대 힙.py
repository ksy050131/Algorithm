import sys, heapq

input = sys.stdin.readline

max_heap = []

phase = int(input())

for _ in range(phase):
    command = int(input())

    if command != 0:
        heapq.heappush(max_heap, -command)

    else:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else: print(0)