n = int(input())
a = [int(input()) for i in range(n)]
num = sorted([i for i in range(1, n+1)], reverse = True)
stack = []
result = []

idx = 0
check = True

while idx < n:
    if not stack:
        if not num:
            check = False
            break
        else:
            stack.append(num.pop())
            result.append('+')
            continue

    if a[idx] != stack[-1]:
        if not num:
            check = False
            break
        else:
            stack.append(num.pop())
            result.append('+')
    else:
        stack.pop()
        result.append('-')
        idx += 1

if check:
    for i in result:
        print(i)
else:
    print('NO')