import sys

# 생각해낸 첫 번째: Counter 이용 -> 시간 안 터져서 일단 ㅇㅋ. 제출.
from collections import Counter

n = int(input())
target = Counter(list(map(int, sys.stdin.readline().strip().split())))
m = int(input())
lst = list(map(int, sys.stdin.readline().strip().split()))

for i in lst:
    print(target.get(i, 0), end = ' ')