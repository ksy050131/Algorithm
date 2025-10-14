import sys
from collections import defaultdict

input = sys.stdin.readline

numA, numB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mapA = defaultdict(lambda: False)
mapB = defaultdict(lambda: False)

for i in A:
    mapA[i] = True
for i in B:
    mapB[i] = True

def difference(a_list, b_map):
    result = []
    for i in a_list:
        if not b_map[i]:   # B에 없는 경우만 추가
            result.append(i)
    return result

print(len(difference(A, mapB)) + len(difference(B, mapA)))