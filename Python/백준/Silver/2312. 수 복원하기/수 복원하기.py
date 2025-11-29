import sys

input = sys.stdin.readline

def sieve(n: int):
    if n < 2: return

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p] == True:
            for mulp in range(p * p, n + 1, p):
                is_prime[mulp] = False

    result = [idx for idx, val in enumerate(is_prime) if val]
    return result

def prime_factorization(n: int, prime: list):
    for p in prime:
        if n == 1: return

        cnt = 0
        while (n % p == 0):
            n = n // p
            cnt += 1
        if cnt:
            print(p, cnt)

testcase = int(input())
target = list(int(input()) for _ in range(testcase))

prime = sieve(max(target))

for t in target:
    prime_factorization(t, prime)