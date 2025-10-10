import sys

input = sys.stdin.readline

min_val, max_val = map(int, input().split())

is_prime = [True] * (max_val + 1)
is_prime[0] = False
is_prime[1] = False

def sieve(n: int):
    if n < 2:
        return []
    
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for mulp in range(p*p, max_val + 1, p):
                is_prime[mulp] = False
    
    return [i for i, val in enumerate(is_prime) if val]

result = sieve(max_val)

for val in result:
    if val >= min_val:
        print(val)