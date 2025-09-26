import sys
from decimal import Decimal, ROUND_HALF_UP

input = sys.stdin.readline

n = int(input())

def normal_round(x):
    return int(Decimal(x).to_integral_value(rounding=ROUND_HALF_UP))

if n == 0:
    print(0)
else:
    level_list= []

    for _ in range(n):
        level_list.append(int(input()))
    level_list.sort()

    cut = normal_round(n * 0.15)
    level_list = level_list[cut: -cut or None] # cut = 0일때 None으로 바뀌어 [0:]이 됨

    level = normal_round(sum(level_list) / (n - cut * 2))
    print(level)