n = int(input())
lst = [0] + list(map(int, (input().split())))
dp = [0] * (n+1)
dp[1] = lst[1]

ans = lst[1]

for i in range(2, n+1):
    M = 0
    # 나는 이 MAX값을 lst[j]로 생각했었는데
    # 만약 [5, 1, 2, 3, 6] 이 들어오면
    # 부분 증가 수열인 (1+2+3)에 6을 붙여야되는데
    # 원래 로직같았으면 5에다가 6을 붙이게 되었다
    
    for j in range(i-1, 0, -1):
        if lst[j] < lst[i] and dp[j] > M:
            M = dp[j]
    
    if M == 0:
        dp[i] = lst[i]
    else:
        dp[i] = M+lst[i]

    if ans < dp[i]:
        ans = dp[i]

print(ans)
