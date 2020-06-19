import sys
N, K = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
i = 0
cnt = 0

while i < (N-1):
    i += (K-1)
    cnt += 1
    
print(cnt)