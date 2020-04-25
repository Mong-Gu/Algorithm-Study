# 파이썬으로는 포기...
""" 
시간 초과
import sys
s = sys.stdin.readline().strip()
bomb = input()

while len(s) > 0:
    if bomb in s:
        s = s.replace(bomb, '')
    else:
        break

if len(s) == 0:
    print('FRULA')
else:
    print(s) 
"""

""" 
시간 더 터짐
import sys
s = sys.stdin.readline().strip()
bomb = ','.join(input()).split(',')
res = []

for i in range(len(s)):
    res.append(s[i])
    if len(res) >= len(bomb) and res[-1] == bomb[-1]:
        if res[-len(bomb):] == bomb:
            res = res[:-len(bomb)]
if len(res) == 0:
    print('FRULA')
else:
    print(''.join(res)) 
"""