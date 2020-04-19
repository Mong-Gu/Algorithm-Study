# 시간초과뜬다.
# 내 생각에는 insert의 시간복잡도가 너무 커.
# 이걸 하려면 하나하나 새로운 리스트에 추가해서는 안되고 방향키의 개수만큼 글자들을 움직여줘야 할듯
""" import sys
n = int(input())
for _ in range(n):
    s = sys.stdin.readline().strip()
    result = []
    idx = 0
    for i, v in enumerate(s):
        # print(v, idx)
        if v == '<':
            if idx > 0:
                idx -= 1
        elif v == '>':
            if idx < len(result):
                idx += 1
        elif v == '-' and result:
            result.pop()
        else:
            result.insert(idx, v)
            idx += 1
        # print(idx)
    print(''.join(result))
 """

import sys
from collections import deque
n = int(input())
for _ in range(n):
    s = sys.stdin.readline().strip()
    l = deque()
    r = deque()
    for i in s:
        if i == '<':
            if l:
                r.appendleft(l.pop())
        elif i == '>':
            if r:
                l.append(r.popleft())
        elif i == '-':
            if l:
                l.pop()
        else:
            l.append(i)
    print(''.join(l+r))

# https://home-body.tistory.com/502
# 전적으로 이분 코드임