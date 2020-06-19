lst = [[0]*10 for i in range(101)]
# 결과 리턴할 때 sum(행) - 1 해줘야 함. 0으로 시작하는 경우는 없지만 계산을 위해 1로 임의 배정 했기 때문.
lst[1] = [1]*10
for i in range(2, 101):
    lst[i][0] = lst[i-1][1]
    lst[i][9] = lst[i-1][8]
    for j in range(1, 9):
        lst[i][j] = lst[i-1][j-1] + lst[i-1][j+1]

n = int(input())
print((sum(lst[n])-lst[n][0])%1000000000)