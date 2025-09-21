# 이진 탐색으로 높이 조정
# 나무 잘라서 합 만드는 함수도 만들기

import sys

input = sys.stdin.readline

n, target = map(int, input().split())
tree = list(map(int, input().split()))

def cut_tree(h: int):
    remain = 0

    for t in tree:
        if t > h:
            remain += (t - h)

    return remain

def binary_search(low: int, high: int) -> int:
    # low > high가 되는 순간 high는 "마지막으로 정답이 될 수 있었던 값"이므로 return함
    if low > high: 
        return high
    
    mid = (low + high) // 2
    result = cut_tree(mid)
    
    # 적어도 target보다 많이 가져가는 높이를 구해야함
    if result >= target: 
        return binary_search(mid + 1, high)
    else: return binary_search(low, mid - 1)

print(binary_search(0, max(tree)))