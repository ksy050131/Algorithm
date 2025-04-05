def binom(n, k):
    arr = [0 for _ in range(k + 1)]
    arr[0] = 1
    
    for i in range(n + 1):
        for j in range(min(i, k), 0, -1):
            arr[j] = arr[j - 1] + arr[j]
    return arr[k]

n, k = map(int, input().split())
print(binom(n, k))