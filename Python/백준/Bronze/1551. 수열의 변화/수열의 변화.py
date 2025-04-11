def fnc(a):
    b = []

    for i in range(len(a) - 1):
        b.append(a[i+1] - a[i])

    return b

n, k = map(int, input().split())

a = list(map(int, input().split(',')))

for i in range(k):
    a = fnc(a)

print(','.join(map(str, a)))