# 동전 값 나오면 리스트에 저장
# 리스트 돌면서 값 나누고 나머지 다시 나누고... 반복
# coinCnt로 동전 개수 계산

import sys

input = sys.stdin.readline
coin = []

coinType, value = map(int, input().split())

for _ in range(coinType):
    temp = int(input())
    coin.append(temp)
    
coin.reverse() # 큰 값부터 계산하기 위해
coin_cnt = 0

for item in coin:
    if item <= value:
        coin_cnt += value // item
        value = value % item

print(coin_cnt)