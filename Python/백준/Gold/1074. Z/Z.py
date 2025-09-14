# 2^(N - 1) = half로 나눠서 x, y의 범위를 탐색
# 인덱스 기준으로 봐야지...
# 인덱스 기준으로 1 2 3 4 분면 나누기(z모양)

# 1 = 2^N * 0 (N은 half)
# 2 = 2^N * 1
# 3 = 2^N * 2
# 4 = 2^N * 3

# 전역변수 세우고 매 턴마다 더하기
# 좌표가 바뀌어야함!!! 상대적이므로

import sys

input = sys.stdin.readline

N, row, col = map(int, input().split())

width = 2 ** N
# print(width)

num = 0

def zfunc(r: int, c: int, width: int):
    global num

    if width == 1: return 

    half = width // 2
    plus_value = half ** 2
    # print(plus_value)

    # 1
    if 0 <= r < half and 0 <= c < half:
        num += plus_value * 0
        # 좌표 변화 없음
    # 2
    elif 0 <= r < half and half <= c < width:
        num += plus_value * 1
        c -= half
    # 3
    elif half <= r < width and 0 <= c < half:
        num += plus_value * 2
        r -= half
    # 4
    elif half <= r < width and half <= c < width:
        num += plus_value * 3
        r -= half
        c -= half
    
    # print(f"width: {width}, num: {num}, row: {r}, col: {c}")
    zfunc(r, c, half)

zfunc(row, col, width)
print(num)