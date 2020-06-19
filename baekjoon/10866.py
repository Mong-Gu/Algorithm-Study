import sys, collections
n = int(input())
dequeue = collections.deque()
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push_front':
        dequeue.appendleft(command[1])
    elif command[0] == 'push_back':
        dequeue.append(command[1])
    elif command[0] == 'pop_front':
        print(dequeue.popleft() if len(dequeue) != 0 else -1)
    elif command[0] == 'pop_back':
        print(dequeue.pop() if len(dequeue) != 0 else -1)
    elif command[0] == 'size':
        print(len(dequeue))
    elif command[0] == 'empty':
        print(int(len(dequeue) == 0))
    elif command[0] == 'front':
        print(dequeue[0] if len(dequeue) != 0 else -1)
    else:
        print(dequeue[-1] if len(dequeue) != 0 else -1)