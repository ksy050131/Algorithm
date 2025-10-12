import sys

input = sys.stdin.readline

th = int(input())

is_prime = [True] * 200001
is_prime[0] = is_prime[1] = False

def sieve(n):
    if n < 2:
        return []
    
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p] == True:
            for mulp in range(p*p, n + 1, p):
                is_prime[mulp] = False

    return [i for i, val in enumerate(is_prime) if val]

result = sieve(200000)
print(result[th - 1])