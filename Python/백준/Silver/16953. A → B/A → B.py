# 개념: A에서 시작해서 두 가지 연산을 통해 B로 도달할 수 있는 최소 횟수를 구한다.
# 연산:
#   1) X * 2
#   2) X * 10 + 1
#
# 접근 방식:
#   각 숫자를 '노드'로 생각하고,
#   가능한 다음 숫자들을 '간선'으로 연결한 그래프로 탐색한다.
#   BFS(너비 우선 탐색)는 가장 가까운 곳부터 탐색하므로
#   처음 B에 도착하는 순간의 단계 수가 곧 '최소 연산 횟수'이다.

import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

def bfs(a, b):
    # queue에 (현재 숫자, 단계 수) 저장
    # 단계 수는 시작 숫자 A를 포함하므로 1부터 시작함

    q = deque()
    q.append((a, 1))

    while q:
        x, steps = q.popleft()

        if x == b:
            return steps
    
        # 두 가지 경우의 수
        next1 = x * 2
        next2 = x * 10 + 1

        # B 이하일 때만 탐색하도록
        if next1 <= b:
            q.append((next1, steps + 1))
        if next2 <= b:
            q.append((next2, steps + 1))

    return -1 # B에 도달하지 못하면 불가능하므로 -1 반환

print(bfs(A, B))