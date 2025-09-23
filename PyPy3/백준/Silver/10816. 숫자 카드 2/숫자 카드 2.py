# list.count()를 사용할 경우 시간복잡도: O(n x m)
# dict을 사용할 경우 시간복잡도: O(n + m)

import sys

input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))
card = {}

for token in temp:
   card[token] = card.get(token, 0) + 1

# dict.get(key, default) => key가 없을 때 default 값을 반환
# 조회할 때만 동작함!!
print(' '.join(str(card.get(t, 0)) for t in target))