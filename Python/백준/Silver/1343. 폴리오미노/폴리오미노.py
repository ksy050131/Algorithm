import sys

input = sys.stdin.readline

s = input().strip()
s = s.replace("XXXX", "AAAA").replace("XX", "BB")


print(-1 if 'X' in s else s)

# 2번째 방법
import sys

input = sys.stdin.readline

line = input().strip()
# print(line)

token = line.split(".")
# print(token)

# ''.join() 은 리스트의 각 토큰, 요소들을 ' ' 안의 무언가에 연결한다는 의미
# ex) ' '.join(str) str의 요소들을 출력하되, 띄어쓰기를 함
# print('.'.join(token)) 

new = []
ok = True
for tok in token:
    if tok == "":
        new.append(tok)
        continue

    if len(tok) % 2 != 0:
        ok = False
        break
    
    num_a = len(tok) // 4
    rest = len(tok) % 4
    num_b = rest // 2

    new_str = "AAAA" * num_a + "BB" * num_b
    # print(new_str)
    new.append(new_str)

if ok:
    print('.'.join(new)) 
else: print(-1)
