import sys
n = int(input())
stack = []
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop() if len(stack) != 0 else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(int(len(stack) == 0))
    else:
        print(stack[-1] if len(stack) != 0 else -1)