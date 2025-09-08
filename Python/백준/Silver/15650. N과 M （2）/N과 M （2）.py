import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    # 다음에 고를 숫자는 start 이상만 허용함 => 중복 생기지 않음
    for i in range(start, n + 1):
        if i not in arr:
            arr.append(i) # 선
            dfs(i + 1)
            arr.pop() # 되돌리기
            # 경우의 수 생성을 마친 뒤 pop()으로 방금 선택한 i 제거
            # => 같은 깊이에서 다음 후보(i + 1, i + 2)를 시도할 수 있도록
            # ex) 1 2 3 고른 뒤 3을 pop() -> 4도 넣어서 1 2 4 만들기

dfs(1)