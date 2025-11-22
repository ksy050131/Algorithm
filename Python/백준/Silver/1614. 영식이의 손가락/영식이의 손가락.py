import sys

data = sys.stdin.read().split()
hurt = int(data[0])      # 다친 손가락 번호 (1~5)
cnt = int(data[1])       # 다친 손가락 사용 가능 횟수 (0 이상, 매우 클 수 있음)

# 규칙 요약:
# 1번 손가락: 8씩 증가
# 5번 손가락: 8씩 증가 + 항상 4 더해짐
# 2,3,4번 손가락: 4씩 증가 + 짝/홀에 따라 마지막 위치 보정
if hurt == 1:
    answer = 8 * cnt
elif hurt == 5:
    answer = 8 * cnt + 4
else:
    if cnt % 2 == 0:   # 짝수 번 사용 -> 왼쪽에서 오른쪽 방향
        answer = 4 * cnt + (hurt - 1)
    else:              # 홀수 번 사용 -> 오른쪽에서 왼쪽 방향
        answer = 4 * cnt + (5 - hurt)

print(answer)
