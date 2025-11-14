import sys
from collections import deque

n, m = map(int, input().split())
queue = deque([i + 1 for i in range(n)])
target = list(map(int, input().split()))

t_idx = 0
cnt = 0
while True:
    pos = queue.index(target[t_idx])
    # 왼쪽으로 돌렸을 때와 오른쪽으로 돌렸을 때를 비교
    left = pos
    right = len(queue) - pos

    # 더 작은 쪽 + cnt 하고 돌림
    if left < right:
        queue.rotate(-pos)
        cnt += left

    else:
        queue.rotate(len(queue)-pos)
        cnt += right
    
    if queue[0] == target[t_idx]:
        queue.popleft()
        t_idx += 1

    if t_idx == m: break

print(cnt)