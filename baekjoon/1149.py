import sys
n = int(input())
cost = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]
result = [[0, 0, 0] for i in range(n)]
result[0] = cost[0]

for i in range(1, n):
    result[i][0] = min(result[i-1][1]+cost[i][0], result[i-1][2]+cost[i][0])
    result[i][1] = min(result[i-1][0]+cost[i][1], result[i-1][2]+cost[i][1])
    result[i][2] = min(result[i-1][0]+cost[i][2], result[i-1][1]+cost[i][2])

print(min(result[-1]))