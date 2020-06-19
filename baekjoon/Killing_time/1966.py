from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    importance = sorted(lst)

    lst = deque(lst)
    idx = deque([i for i in range(n)])
    
    result = []

    while len(lst) != 0:
        if lst[0] != importance[-1]:
            lst.append(lst.popleft())
            idx.append(idx.popleft())
        else:
            lst.popleft()
            importance.pop()
            result.append(idx.popleft())

    print(result.index(m)+1)