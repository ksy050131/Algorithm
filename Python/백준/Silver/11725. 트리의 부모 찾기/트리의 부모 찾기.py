import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (N+1)
parent[1] = -1 # 임의로 (방문했다는 표시)

# print(tree)

q = deque([1]) # 1부터 시작하므로
while q:
    u = q.popleft()

    # print(parent[u])
    for v in tree[u]:
        if parent[v] == 0:
            parent[v] = u
            q.append(v)

print('\n'.join(map(str, parent[2:])))