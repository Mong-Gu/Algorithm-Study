n = int(input())
lst = [0] + list(map(int, (input().split())))
dp = [0] * (n+1)
dp[1] = 1
ans = 1

for i in range(2, n+1):
    tmp = []
    for j in range(i-1, 0, -1):
        if lst[j] > lst[i]:
            tmp.append(dp[j])
    if tmp:
        dp[i] = max(tmp)+1
    else:
        dp[i] = 1

    if ans < dp[i]:
        ans = dp[i]

print(ans)