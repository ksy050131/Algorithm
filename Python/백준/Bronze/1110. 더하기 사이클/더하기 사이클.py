def plusCycle(num):
    if 0 <= num < 10:
        num = '0' + str(num)
        num = int(num)
        
    first = num // 10
    last = num % 10
    
    sum = first + last
    result = str(last) + str(sum)[-1]
    
    return int(result)

target = int(input())
cnt = 0

result = plusCycle(target)
while(1):
    cnt += 1

    if result == target:
        break
    else: result = plusCycle(result)

print(cnt)