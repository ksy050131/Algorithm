import sys

input = sys.stdin.readline
phase = int(input())

money_list = []

for _ in range(phase):
    money = int(input())
    
    if money == 0:
        money_list.pop()
    else:
        money_list.append(money)

print(sum(money_list))