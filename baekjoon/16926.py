import sys
n, m, r = map(int, input().split())
lst = [list(sys.stdin.readline().strip().split()) for i in range(n)]

for i in lst:
    print(i)

for i in range(r):
    tmp_1 = ''
    tmp_2 = ''
# 일단 여기까지 하고 집에 가기