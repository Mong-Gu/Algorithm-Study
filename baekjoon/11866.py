from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
lst = []

while d:
    d.rotate(-(k-1))
    lst.append(d.popleft())

print('<', end = '')
for i in range(len(lst)):
    if i != len(lst)-1:
        print("%d, " %lst[i], end = '')
    else:
        print("%d>" %lst[i])