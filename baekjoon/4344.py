import sys
n = int(input())
for i in range(n):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    avg = sum(lst[1:])/lst[0]
    cnt = 0
    for score in lst[1:]:
        if score > avg:
            cnt += 1
    print('%.3f%%' % (cnt/lst[0]*100))