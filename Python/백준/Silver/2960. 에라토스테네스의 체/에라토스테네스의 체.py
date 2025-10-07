import sys

input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
    
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False # 소수가 아니므로
remov_list = []

for p in range(2, n + 1):
    if is_prime[p]: # 소수이면
        remov_list.append(p)
        for mul in range(p*p, n + 1, p):
            if is_prime[mul] == False: continue
            is_prime[mul] = False
            remov_list.append(mul)

# print(remov_list)
print(remov_list[k-1])