import sys

input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    level_list= []

    for _ in range(n):
        level_list.append(int(input()))
    level_list.sort()

    cut = (n * 15 + 50) // 100 # 정수식으로 표현. 50은 +0.5와 같은 역할
    level_list = level_list[cut: -cut or None] # cut = 0일때 None으로 바뀌어 [0:]이 됨

    level = (sum(level_list) + len(level_list) // 2) // len(level_list)
    print(level)