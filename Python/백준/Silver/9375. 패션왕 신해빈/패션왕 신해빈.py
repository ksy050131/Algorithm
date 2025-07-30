import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    phase = int(input())
    clothes = {}
    
    for _ in range(phase):
        name, category = input().split()
        # print(name, category)
    
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
    result = 1
    for count in clothes.values():
        result *= (count + 1)
        
    print(result - 1)