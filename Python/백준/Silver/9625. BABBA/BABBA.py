import sys

input = sys.stdin.readline

# 규칙 확인용
# def change_AB(prev):
#     new = ''
#     for text in prev:
#         if text == 'A':
#             new = new + 'B'
#         elif text == 'B':
#             new = new + "BA"
#     print(new)
#     return new

num_of_AB = [[0, 0] for _ in range(46)]

num_of_AB[0][0] = 0
num_of_AB[0][1] = 0

num_of_AB[1][0] = 0
num_of_AB[1][1] = 1

for i in range(2, 46):
    num_of_AB[i][0] = num_of_AB[i - 1][1]
    num_of_AB[i][1] = num_of_AB[i - 1][0] + num_of_AB[i - 1][1]

idx = int(input())
print(num_of_AB[idx][0], num_of_AB[idx][1])