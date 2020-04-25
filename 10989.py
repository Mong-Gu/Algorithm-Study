""" 
이거 왜 안됨?????????????????????????????????????
딕셔너리 이용해서 radix쓰면 시간복잡도 빠른거 아냐?
전혀 전혀 전혀 전혀 모르겠네!!!!!!!!!!!!!!!!????????????
import sys
n = int(input())
dic = {}
for i in range(n):
    x = int(sys.stdin.readline())
    dic[x] = dic.get(x, 0) + 1
# for i in sorted(dic.keys()):
#     print('{}\n'.format(i)*dic[i], end='')
for lst in sorted(dic.items()):
    for i in range(lst[1]):
        sys.stdout.write('{}\n'.format(lst[0]))
 """

import sys
n = int(input())
lst = [0 for i in range(10000)]
for i in range(n):
    x = int(sys.stdin.readline())
    lst[x-1] += 1
for idx, cnt in enumerate(lst):
    if cnt != 0:
        for i in range(cnt):
            sys.stdout.write('{}\n'.format(idx+1))
            

'''
혹시나해서 성공 코드에서 입출력에 대한 메서드를 input과 print로 바꿔봤는데
시간초과 떠버림. 입력값이 많을 경우에는 그냥 sys 써버리자.
n = int(input())
lst = [0 for i in range(10000)]
for i in range(n):
    x = int(input())
    lst[x-1] += 1
for idx, cnt in enumerate(lst):
    if cnt != 0:
        for i in range(cnt):
            print('{}'.format(idx+1))
'''