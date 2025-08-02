s = input()

count0 = 0
count1 = 0

# 첫 글자에 따라 초기값 설정
if s[0] == '0':
    count0 += 1
else:
    count1 += 1

# 연속이 끊길 때마다 새 묶음
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))