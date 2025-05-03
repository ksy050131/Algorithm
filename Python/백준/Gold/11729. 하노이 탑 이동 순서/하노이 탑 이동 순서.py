import sys

def hanoi(n, src, tmp, dst):
    if n == 1:
        print(src, dst)
        return
        
    else:
        hanoi(n - 1, src, dst, tmp)
        hanoi(1, src, tmp, dst)
        hanoi(n - 1, tmp, src, dst)

n = int(sys.stdin.readline())
cnt = 2 ** n - 1
print(cnt)
hanoi(n, 1, 2, 3)