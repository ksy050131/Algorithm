import sys

input = sys.stdin.readline
addressDict = {}

addressNum, targetAddressNum = map(int, input().split())

for _ in range(addressNum):
    address, password = input().split()
    addressDict[address] = password

# print(addressDict)

for _ in range(targetAddressNum):
    target = input().strip()

    if target in addressDict:
        print(addressDict[target])
