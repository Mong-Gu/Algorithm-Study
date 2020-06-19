n, k = map(int, input().split())
c = [int(input()) for i in range(n)] # 코인의 종류
dp = [0 for i in range(k+1)] # 사이즈 k만큼의 배열 선언
dp[0] = 1 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언

for idx, i in enumerate(c):
    print('\n{}원을 썼을 때'.format(c[0:idx+1]))
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
            print('합이 %2d원일 때 변경 ->' %j, dp[1:])

print();print(dp[k])