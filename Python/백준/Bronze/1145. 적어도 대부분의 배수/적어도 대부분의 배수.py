# 다섯 개의 자연수 입력 받기
nums = list(map(int, input().split()))

# 1부터 시작하여 가장 작은 적어도 대부분의 배수를 찾기
n = 1
while True:
    count = 0
    for num in nums:
        if n % num == 0:
            count += 1
    if count >= 3:
        print(n)
        break
    n += 1
