import sys
t = int(input())
for i in range(t):
    stack = []
    s = sys.stdin.readline().strip()
    for item in s:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0 or stack.pop() != '(':
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')