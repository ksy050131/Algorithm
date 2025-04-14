def rev(X):
    X = list(str(X))
    X.reverse()

    # 앞부분의 0만 제거
    while X and X[0] == '0':
        X.pop(0)  # 앞부분의 '0' 제거
            
    X = int(''.join(X))
    return X
        

X, Y = map(int, input().split())
 
result = rev(X) + rev(Y)
print(rev(result))