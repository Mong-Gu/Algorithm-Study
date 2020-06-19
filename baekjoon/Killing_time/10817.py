import sys
a, b, c = map(int, sys.stdin.readline().strip().split())
print(sorted([a, b, c])[1])