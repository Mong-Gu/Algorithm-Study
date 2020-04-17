import sys, collections
n = int(input())
queue = collections.deque()
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft() if len(queue) != 0 else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(int(len(queue) == 0))
    elif command[0] == 'front':
        print(queue[0] if len(queue) != 0 else -1)
    else:
        print(queue[-1] if len(queue) != 0 else -1)