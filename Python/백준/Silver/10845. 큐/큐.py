import sys

def isEmpty():
    global front, rear
    
    if front == rear:
        return 1
    else: return 0
        
queue = []
front = -1
rear = -1

commandNum = int(sys.stdin.readline())

for _ in range(commandNum):
    command = sys.stdin.readline().strip()
    
    # print(f"front: {front}, rear: {rear}")
    # print(command)
    
    if 'push' in command:
        commandBuf, num = command.split()
        queue.append(int(num))
        rear += 1
        
        # print(queue)
    
    elif command == 'pop':
        if isEmpty() == 1:
            print(-1)
        else:
            print(queue[front + 1])
            front += 1
    
    elif command == 'size':
        print(rear - front)
    
    elif command == 'empty':
        print(isEmpty())
    
    elif command == 'front':
        if isEmpty() == 1:
            print(-1)
        else:
            print(queue[front + 1])
    
    elif command == 'back':
        if isEmpty() == 1:
            print(-1)
        else:
            print(queue[rear])