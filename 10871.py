import sys
a, b = map(int, sys.stdin.readline().strip().split())
lst = [x for x in map(int, sys.stdin.readline().strip().split())]
result = [str(x) for x in lst if x < b]
print(' '.join(result))