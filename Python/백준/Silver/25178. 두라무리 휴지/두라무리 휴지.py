from collections import Counter

def remove_vowels(s):
    vowels = set("aeiou")
    return ''.join([c for c in s if c not in vowels])

def is_valid_transformation(A, B):
    if A[0] != B[0] or A[-1] != B[-1]:
        return False
    if remove_vowels(A) != remove_vowels(B):
        return False
    if Counter(A) != Counter(B):
        return False
    return True

n = int(input())
A = input().strip()
B = input().strip()

if is_valid_transformation(A, B):
    print("YES")
else:
    print("NO")