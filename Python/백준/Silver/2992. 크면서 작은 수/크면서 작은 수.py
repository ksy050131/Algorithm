import sys
import itertools

input = sys.stdin.readline
x = int(input())
numlist = list(str(x))
length = len(numlist)
nPr = itertools.permutations(numlist, length)
# print(list(nPr))

expect = []
for i in list(nPr):
    expect.append(int(''.join(i)))

expect.sort()
# print(expect)

new_expect = []
for e in expect:
    if len(str(e)) == length and e > x and e not in new_expect:
        new_expect.append(e)

# print(new_expect)
if not new_expect: print(0)
else: print(new_expect[0])