import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().strip().split()))
M = max(lst)
lst = [score / M * 100 for score in lst]
print(sum(lst)/len(lst))