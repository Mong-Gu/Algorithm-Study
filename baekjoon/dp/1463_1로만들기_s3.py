# n = int(input())
# lst = [0, 0, 1, 1] + [0] * (n-3)
# idx = 4
# while idx <= n:
# 	if idx % 3 == 0 and idx % 2 == 0:
# 		lst[idx] = min(lst[idx//3]+1, lst[idx//2]+1, lst[idx-1]+1, lst[idx-2]+2, lst[idx-3]+3)
# 	elif idx % 3 == 0:
# 		lst[idx] = lst[idx//3] + 1
# 	elif idx % 2 == 0:
# 		lst[idx] = min(lst[idx//2]+1, lst[idx-1]+1, lst[idx-2]+2, lst[idx-3]+3)
# 	else:
# 		lst[idx] = min(lst[idx-1] + 1, lst[idx-2] + 2, lst[idx-3] + 3)
# 	idx += 1
# print(lst[n])

N = int(input())
dp = [0,0,1,1] + [0] * (N-3)
for i in range(4, N+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0 :
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[N])
