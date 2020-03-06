import sys
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))