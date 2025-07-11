import sys

input = sys.stdin.readline

def checkpalin(S):
    length = len(S)
    
    for i in range(length // 2):
        if S[i] != S[length - i - 1]:
            return False

    return True

num_of_str = int(input())
cnt = 0

for _ in range(num_of_str):
    tmp = input().strip()

    if checkpalin(tmp):
        cnt += 1
        
print(cnt * (cnt - 1))