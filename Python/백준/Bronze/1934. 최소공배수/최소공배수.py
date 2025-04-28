def gcd(x, y):
    while(y):
        x,y = y, (x % y)
    return x

testCase = int(input())

for _ in range(testCase):
    a, b = map(int, input().split())
    gcdVal = gcd(a, b)
    ans = (a * b) // gcdVal
    print(ans)