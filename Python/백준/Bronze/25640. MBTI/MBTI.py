target = input()

number_of_friends = int(input())

total = 0
for _ in range(number_of_friends):
    friend = input()

    if target == friend:
        total += 1

print(total)