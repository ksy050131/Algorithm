import sys

num = sys.stdin.readline().strip()
str_list = list(num)
str_list.sort(reverse = True)

print(''.join(str_list))