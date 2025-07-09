import sys

input = sys.stdin.readline

def encodeprint(binary, index):
    for num in binary[index]:
        if num == '1':
            print("딸기", end = '')
        else:
            print('V', end = '')
    print()

binary = ['0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '1110', '1101', '1100', '1011', '1010', '1001', '1000', '0111', '0110', '0101', '0100', '0011', '0010']

phase = int(input())

for _ in range(phase):
    num = int(input())
    idx = num % 28 - 1
    encodeprint(binary, idx)