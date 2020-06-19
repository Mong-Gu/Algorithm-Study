import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().strip().split()))
print(min(lst), max(lst))