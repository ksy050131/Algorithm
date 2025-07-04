pStack = []

def checkVPS(ps):
    for item in ps:
        if item == "(":
            pStack.append(")")
        elif item == ")":
            if len(pStack) == 0:
                print("NO")
                return
            else: pStack.pop()
    
    if len(pStack) > 0: # 아직 stack에 남아있으면 괄호 완성 X
        print("NO")
    else: print("YES")

    return

phase = int(input())

for _ in range(phase):
    ps = input()
    checkVPS(ps)
    pStack.clear()