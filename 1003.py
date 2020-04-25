dic = {0:[1, 0], 1:[0, 1]}
for i in range(2, 41):
    dic[i] = [dic[i-2][0]+dic[i-1][0], dic[i-2][1]+dic[i-1][1]]
n = int(input())
for i in range(n):
    x = int(input())
    print(dic[x][0], dic[x][1])