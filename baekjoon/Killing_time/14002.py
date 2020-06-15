n = int(input())
lst = [0] + list(map(int, (input().split())))
dp = [[0, 0] for i in range(n+1)]
dp[1] = [1, '%d' %lst[1]]
ans = [1, '%d' %lst[1]]

for i in range(2, n+1):
    tmp = []
    for j in range(i-1, 0, -1):
        if lst[j] < lst[i]:
            tmp.append(dp[j])
    
    if tmp:
        x = max(tmp, key = lambda x: x[0])
        dp[i][0] = x[0] + 1
        dp[i][1] = x[1] + ' %d' %lst[i]
    else:
        dp[i] = [1, '%d' %lst[i]]
    
    if dp[i][0] > ans[0]:
        ans = dp[i]

print(ans[0])
print(ans[1])