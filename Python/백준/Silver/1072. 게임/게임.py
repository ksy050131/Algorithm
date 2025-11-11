# X: 총 게임 수
# Y: 이긴 게임 수
# Z = (Y * 100) // X  (현재 승률)
# => 새로운 게임을 계속 이겨서 승률이 바뀌는 최소 게임 수 K를 구하라.
#    단, 승률이 더 이상 바뀌지 않으면 -1 출력.

import sys
input = sys.stdin.readline

x, y = map(int, input().split())

# float 오차를 없애기 위해 (y * 100) // x 로 계산 (정수 나눗셈 사용)
def score(x, y):
    return (y * 100) // x


def binarysearch(low, high, target_z):
    global x
    global y

    # 새로 이길 게임 수(k)의 후보
    mid = (low + high) // 2

    # mid만큼 추가로 이겼을 때의 새로운 승률 계산
    new_z = score(x + mid, y + mid)

    # low > high가 되는 순간
    #  -> 현재 hi 구간은 아직 승률이 안 변함
    #  -> lo 구간은 승률이 바뀐 최초 지점
    #  -> 따라서 lo가 "최소 K값"이 된다.
    if low > high:
        return low

    # 승률이 이미 target_z보다 커졌으면 (변화가 생겼으면)
    # 더 작은 K에서 변하는지 확인해야 하므로 왼쪽(작은 쪽)으로 이동
    elif new_z > target_z:
        return binarysearch(low, mid - 1, target_z)
    # 승률이 아직 그대로라면 (변화 안 됨)
    # 더 많은 게임을 이겨야 하므로 오른쪽(큰 쪽)으로 이동
    else:
        return binarysearch(mid + 1, high, target_z)

# 승률이 99 이상이면 절대 다음 정수로 안 바뀜 → -1 출력
if score(x, y) >= 99:
    print(-1)
else:
    # 처음으로 승률이 오르는 최소 게임 수 K를 이분탐색으로 찾기
    print(binarysearch(1, 1000000000, score(x, y)))