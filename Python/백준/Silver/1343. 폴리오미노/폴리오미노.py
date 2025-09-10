import sys

input = sys.stdin.readline

s = input().strip()
s = s.replace("XXXX", "AAAA").replace("XX", "BB")

print(-1 if 'X' in s else s)