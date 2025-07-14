import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    numlist = list(map(int, input().split()))

    even = 0
    odd = 0
    for i in range(1, len(numlist)):
        num = numlist[i]
    
        if num % 2 == 0:
            even += num
        else:
            odd += num

    if even > odd:
        print("EVEN")
    elif even < odd:
        print("ODD")
    else: print("TIE")