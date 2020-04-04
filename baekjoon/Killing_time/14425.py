""" 
시간 터짐
import sys
n, m = map(int, input().split())
S = [sys.stdin.readline().strip() for i in range(n)]
cnt = 0
for i in range(m):
    if sys.stdin.readline().strip() in S:
        cnt += 1
        if cnt == len(S):
            break
print(cnt) 
"""

""" 
틀렸음. 내 생각에는 M개의 줄 안에 중복되는 문자열이 주어질 수 있음.
import sys
n, m = map(int, input().split())
A = set([sys.stdin.readline().strip() for i in range(n)])
B = set([sys.stdin.readline().strip() for i in range(m)])
print(A&B)
print(len(A & B)) 
"""

import sys, collections
n, m = map(int, input().split())
A = [sys.stdin.readline().strip() for i in range(n)]
B = collections.Counter([sys.stdin.readline().strip() for i in range(m)])
cnt = 0
for k, c in B.items():
    if k in A:
        cnt += c
print(cnt)

