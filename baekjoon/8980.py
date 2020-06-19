""" import sys
n, c = map(int, input().split())
m = int(input())
lst = sorted([list(map(int, sys.stdin.readline().strip().split())) for i in range(m)], key = lambda x : (x[0],x[1]))
# for i in lst:
#     print(i)
cnt = 0
dic = {1:0}

prev = 0
for start, end, val in lst:
    if prev < start:
        print()
        print(start, '번 마을에 도착해서 여유공간 확보')
        prev = start
        c += dic[prev] # 다음 마을에서 내려야 할 물건을 내림
    #     print('현재 여유 공간:', c)

    # print(start,'번 마을에서',end,'번 마을로',val)
    # print('여유 공간:', c, end='')

    if c > 0:
        if c >= val:
            dic[end] = dic.get(end, 0) + val
            c -= val
            cnt += val
        elif c < val:
            dic[end] = dic.get(end, 0) + c
            cnt += c
            c = 0
        print('->', c)
    else:
        continue """

import sys
n, c = map(int, input().split())
m = int(input())
lst = sorted([list(map(int, sys.stdin.readline().strip().split())) for i in range(m)], key = lambda x : (x[1],x[0]))
for i in lst:
    print(i)
cnt = 0
dic = {1:0}

prev = 0
for start, end, val in lst:
    if prev < start:
        prev = start
        c += dic.get(prev, 0) # 다음 마을에서 내려야 할 물건을 내림
    if c > 0:
        if c >= val:
            dic[end] = dic.get(end, 0) + val
            c -= val
            cnt += val
        elif c < val:
            dic[end] = dic.get(end, 0) + c
            cnt += c
            c = 0
    else:
        continue
print(cnt)

# https://steadev.tistory.com/15 보고 공부하기 대박이다