# 회전 정사각형까지 고려해야함
# 네 점 사이의 거리는 4C2 = 6개가 나온다.
# 6개의 거리 중에서 작은 값(변의 길이 제곱) = 4번
# 더 큰 값(대각선 길이 제곱) = 2번 나오면 정사각형
# => 네 변이 모두 같고 대각선 길이가 같으면 정사각형이기 때문

import sys
input = sys.stdin.readline

def dist2(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def is_square(points):
    d = []
    for i in range(4):
        for j in range(i + 1, 4):
            d.append(dist2(points[i], points[j]))

    d.sort()

    # (1) 같은 점이 있으면 안 됨
    if d[0] == 0:
        return 0

    # (2) 제일 짧은 길이 4개(변), 나머지 2개(대각선)
    # d[0]~d[3] : 변^2, d[4], d[5] : 대각선^2
    if d[0] == d[1] == d[2] == d[3] and d[4] == d[5]:
        return 1
    else:
        return 0

t = int(input())
for _ in range(t):
    pts = [tuple(map(int, input().split())) for _ in range(4)]
    print(is_square(pts))