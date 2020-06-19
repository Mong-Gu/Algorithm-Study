n = int(input())
lst = [0] + [int(input()) for i in range(n)]
dp = [0] * (n+1)

if n == 1:
    print(lst[1])
elif n == 2:
    print(lst[1]+lst[2])
else:
    dp[1] = lst[1]
    dp[2] = lst[1] + lst[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], lst[i]+lst[i-1]+dp[i-3], lst[i]+dp[i-2])

    print(dp[n])