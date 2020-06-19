n, k = map(int, input().split())
c = sorted([int(input()) for i in range(n)])
dp = [k+1 for i in range(k+1)] # 아무리 많은 동전이 쓰여도 k+1개 미만임.
dp[0] = 0 # 0원을 만들 수 있는 동전의 개수는 0. 즉, 없음.

for i in range(n):
    # print('{}원 차례'.format(c[i]))
    for j in range(c[i], k+1):
        if dp[j-c[i]] + 1 < dp[j]:
            dp[j] = dp[j-c[i]]+1
            # print(dp)
    # print()

print(dp[-1] if dp[-1] != k+1 else -1)
""" 
시간 터짐.
두 번 터지고 깨달은 것은 DP문제는 함수쓰지말고 리스트 선언 후 덮어씌우는 형식으로 ㄱㄱ

n, k = map(int, input().split())
lst = sorted([int(input()) for i in range(n)], reverse = True) # 동전 종류
print(lst)
min = k+1

def dp(cnt, sum):
    global min
    if sum > k or min < cnt:
        return
    elif sum == k:
        if min > cnt:
            min = cnt
            return
    else:
        for i in lst:
            dp(cnt+1, sum+i)

dp(0, 0)

if min == k+1:
    print(-1)
else:
    print(min) 
"""