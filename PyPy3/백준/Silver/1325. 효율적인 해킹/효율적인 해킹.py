import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# graph[b] = b를 해킹했을 때 직접적으로 해킹 가능한 컴퓨터들 (b -> a)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    # B를 해킹하면 A도 해킹 가능 → B -> A
    graph[B].append(A)

# start에서 시작했을 때 해킹 가능한 컴퓨터 수를 반환
def bfs(start: int) -> int:
    visited = [False] * (N + 1)
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 1  # 자기 자신 포함

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)
    return cnt

max_cnt = 0
answer = []

# 1번부터 N번 컴퓨터까지 각각 시작점으로 BFS 수행
for i in range(1, N + 1):
    cnt = bfs(i)

    if cnt > max_cnt:
        max_cnt = cnt
        answer = [i]       # 새로 최대가 되면 배열 초기화
    elif cnt == max_cnt:
        answer.append(i)   # 기존 최대와 같으면 같이 저장

# 오름차순으로 출력
print(*answer)