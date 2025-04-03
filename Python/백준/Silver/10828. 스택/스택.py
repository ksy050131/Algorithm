import sys
# push X: 정수 X를 스택에 넣음
# pop: 젤 위에 있는 정수 빼고 그 수 출력. 없으면 -1
# size: 스택에 들어있는 정수의 개수
# empty: 스택이 비어있으면 1, 아니면 0
# top: 스택의 가장 위에 있는 정수 출력. 없으면 -1

def isEmpty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0

stack = []
top = -1

commandNum = sys.stdin.readline()

for i in range(int(commandNum)):
    command = sys.stdin.readline().strip()

    if "push" in command:
        commandBuf, num = command.split()

        stack.append(int(num))
        top += 1

    elif command == "pop":
        if isEmpty(stack):
            print(-1)
        else:
            print(stack[top])
            stack.pop()
            top -= 1

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        print(isEmpty(stack))

    elif command == "top":
        if top == -1:
            print(top)
        else:
            print(stack[top])