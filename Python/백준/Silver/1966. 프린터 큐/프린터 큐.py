import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))

    t_importance = deque()

    for i in range(n):
        t_importance.append((i, importance[i]))

    # print(t_importance)
    importance.sort(reverse=True)
    # print(importance)

    i = 0
    cnt = 0
    while True:
        max_imp = importance[i]

        idx, imp = t_importance.popleft()
        # 더 중요한 중요도가 있으므로 뒤로 넘김
        if imp < max_imp:
            t_importance.append((idx, imp))
        elif imp == max_imp:
            i += 1
            cnt += 1
            if m == idx:
                print(cnt)
                break