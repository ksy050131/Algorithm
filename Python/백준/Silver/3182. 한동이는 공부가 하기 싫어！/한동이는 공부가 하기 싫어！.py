import sys

input = sys.stdin.readline

n = int(input())

graph = [0]
result = [0]

for i in range(1, n + 1):
    graph.append(int(input()))
# print(graph)

def dfs(start):
    visit[start] = True

    if not visit[graph[start]]:
        dfs(graph[start]) # graph[start]의 visit이 False -> 아직 방문 X

for i in range(1, n + 1):
    visit = (n + 1) * [False] # 1부터 n까지 start -> 매번 visit 초기화
    dfs(i)
    result.append(visit.count(True)) # visit안의 True 개수 -> i번째 선배의 대답 개수

# result의 최댓값이 result 리스트에서 몇 번째 인덱스인지 출력
print(result.index(max(result)))