day, night, length = map(int, input().split())
totalMove = day - night

# 한 번에 다 올라갈 때
if length <= day:
    print(1)
else:
    if (length - day) % totalMove == 0:
        print(((length - day) // totalMove) + 1)
    else:
        print(((length - day) // totalMove) + 2)