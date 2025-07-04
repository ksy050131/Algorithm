import time

def bst(start, end, target, num_list):
    if start > end:
        return 0
        
    mid = (start + end) // 2

    if target == num_list[mid]:
        return 1
    elif target > num_list[mid]:
        return bst(mid + 1, end, target, num_list)
    else:
        return bst(start, mid - 1, target, num_list)

num = int(input())
num_list = list(map(int, input().split(" ")))
num_list.sort()
# print(num_list)

target_num = int(input())
target_list = list(map(int, input().split(" ")))

for target in target_list:
    print(bst(0, len(num_list) - 1, target, num_list))