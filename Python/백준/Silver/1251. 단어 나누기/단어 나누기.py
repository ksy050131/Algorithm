import sys

input = sys.stdin.readline

word = input().strip()
wordlist = []
# print(word)

for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
            
        w = word[:]
        
        w1 = word[:i][::-1]
        w2 = word[i:j][::-1]
        w3 = word[j:][::-1]
        
        sw = w1 + w2 + w3
        # print(sw)
        wordlist.append(sw)

print(sorted(wordlist)[0])