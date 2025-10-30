import sys
input = sys.stdin.readline

n = int(input())

serials = [input().strip() for _ in range(n)]

def digit_sum(s):
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total

# 정렬 기준:
# (1) 길이 -> (2) 자리수합 -> (3) 사전순
serials.sort(key=lambda x: (len(x), digit_sum(x), x))

print(*serials, sep='\n')