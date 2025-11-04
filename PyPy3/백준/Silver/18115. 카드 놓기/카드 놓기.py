import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
skill = list(map(int, input().split()))
skill.reverse()
origin = deque()

# 1 = card에서 맨 밑(오른쪽) pop -> origin 왼쪽에 append
# 2 = card에서 맨 밑(오른쪽) pop -> origin 맨 왼쪽 pop(저장해놓기) -> origin 왼쪽에 append
#     -> 저장해놓은 거 다시 왼쪽에 append
# 3 = card에서 맨 밑(오른쪽) pop -> origin 오른쪽에 append

for i in range(n):
    if skill[i] == 1:
        origin.appendleft(i+1)

    elif skill[i] == 2:
        origin.insert(1, i+1)

    elif skill[i] == 3:
        origin.append(i+1)

print(*origin)