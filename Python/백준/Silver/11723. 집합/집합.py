# 0부터 20까지 리스트로 집합 만들기

import sys

S = [0] * 21
phase = int(sys.stdin.readline())

for _ in range(phase):
    command = sys.stdin.readline().strip()
    # print(command)
    
    if command == "all":
        S = [1] * 21
    elif command == "empty":
        S = [0] * 21
    else:
        command, num = command.split()
        num = int(num)
    
        if command == "add":
            S[num] = 1
        elif command == "remove":
            S[num] = 0
        elif command == "check":
            print(S[num])
        elif command == "toggle":
            S[num] ^= 1