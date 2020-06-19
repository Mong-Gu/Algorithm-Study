from collections import deque
n = int(input())
lst = [input()]
for i in range(n-1):
    tmp = deque(input())
    for j in range(len(tmp)):
        tmp.rotate(1)
        if ''.join(tmp) in lst:
            break
    else:
        lst.append(''.join(tmp))
print(len(lst))