import sys

T = int(input())

for i in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(n+m)