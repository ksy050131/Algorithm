import sys

input = sys.stdin.readline

n, m = map(int, input().split())
listen = set(input().strip() for _ in range(n))
see = set(input().strip() for _ in range(m))

# 듣도 보도 못한 사람: 교집합
common = sorted(listen & see)

# 결과 출력
print(len(common))
for name in common:
    print(name)
