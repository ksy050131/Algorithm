import sys
from collections import Counter

input = sys.stdin.readline

cards = [input().split() for _ in range(5)]
# cards: [['R', '1'], ['B', '2'], ...]

colors = [c for c, n in cards]
nums = [int(n) for c, n in cards]

nums.sort()

num_cnt = Counter(nums)    # 숫자별 개수
color_cnt = Counter(colors)  # 색깔별 개수

is_flush = (len(color_cnt) == 1)
is_straight = (len(num_cnt) == 5 and nums[-1] - nums[0] == 4)

score = 0

# 1. 스트레이트 플러시
if is_flush and is_straight:
    score = 900 + nums[-1]

# 2. 포카드 (같은 숫자 4장)
elif 4 in num_cnt.values():
    four_num = [num for num, cnt in num_cnt.items() if cnt == 4][0]
    score = 800 + four_num

# 3. 풀 하우스 (3장 + 2장)
elif sorted(num_cnt.values()) == [2, 3]:
    three_num = [num for num, cnt in num_cnt.items() if cnt == 3][0]
    pair_num = [num for num, cnt in num_cnt.items() if cnt == 2][0]
    score = 700 + three_num * 10 + pair_num

# 4. 플러시 (색깔만 같음)
elif is_flush:
    score = 600 + nums[-1]

# 5. 스트레이트 (연속 숫자)
elif is_straight:
    score = 500 + nums[-1]

# 6. 트리플 (같은 숫자 3장)
elif 3 in num_cnt.values():
    three_num = [num for num, cnt in num_cnt.items() if cnt == 3][0]
    score = 400 + three_num

# 7. 투 페어 (2장짜리 숫자가 2개)
elif list(num_cnt.values()).count(2) == 2:
    pair_nums = sorted([num for num, cnt in num_cnt.items() if cnt == 2])
    score = 300 + pair_nums[1] * 10 + pair_nums[0]

# 8. 원 페어
elif 2 in num_cnt.values():
    pair_num = [num for num, cnt in num_cnt.items() if cnt == 2][0]
    score = 200 + pair_num

# 9. 그 외 (하이 카드)
else:
    score = 100 + nums[-1]

print(score)