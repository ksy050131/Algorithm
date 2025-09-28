import sys

input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    k = min(k, n - k) # C(n, k) = C(n, n-k) 이므로

    if n == 0 and k == 0:
        break

    if k == 0: 
        print(1)
        continue

    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i # ex) C(5, 2) => 5 * 4 / 1 * 2

    print(res)