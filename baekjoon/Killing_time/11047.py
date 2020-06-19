import sys

N, K = map(int, sys.stdin.readline().strip().split())
money = []
for i in range(N):
    money.append(int(sys.stdin.readline().strip()))

money.reverse()
cnt = 0

for i in money:
    while K >= i:
        K = K - i
        cnt += 1

print(cnt)