# 에라토스테네스의 체로 소수 배열 생성
# 투 포인터로 구간 합 구하면서 타겟값 개수 세기

import sys

input = sys.stdin.readline

target = int(input())

def sieve(n: int):
    if n < 2: return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0 이랑 1은 소수가 아니므로

    # n ** 0.5 까지만 검사
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]: # 소수이면
            # p*p 부터 p씩 건너뛰며 배수 제거
            for mulp in range(p*p, n + 1, p):
                is_prime[mulp] = False

# if val => val이 True인 경우만 선택
    return [i for i, val in enumerate(is_prime) if val]

def findSum(n: int, prime: list):
    r = l = 0
    s = 0
    ans = 0
    end = len(prime)

    while True:
        if s >= n:
            if s == n:
                ans += 1
            s -= prime[l] # 왼쪽에 있는 값을 뺌
            l += 1
        else: # s < n
            if r == end: break
            s += prime[r]
            r += 1
        
    return ans

prime = sieve(target)
# print(prime)

print(findSum(target, prime))