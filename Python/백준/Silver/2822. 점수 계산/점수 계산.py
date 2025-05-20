import sys

input = sys.stdin.readline

score = {}

# 1. 점수를 입력받고 딕셔너리에 저장
for i in range(1, 9):
    score[i] = int(input().strip())  # 숫자로 변환 필수!

# 2. 점수 기준 내림차순 정렬
sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)

# 3. 상위 5개 문제 번호와 점수
top_5 = sorted_scores[:5]

# 4. 총점 계산
total = sum([s[1] for s in top_5])

# 5. 문제 번호만 추출해서 정렬
problems = sorted([s[0] for s in top_5])

# 6. 출력
print(total)
print(' '.join(map(str, problems)))
