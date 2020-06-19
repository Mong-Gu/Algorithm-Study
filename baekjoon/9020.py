from math import sqrt

lst = [2] # 소수 리스트
for i in range(3, 10001):
    for j in range(2, int(sqrt(i)+1)):
        if i % j == 0:
            break
    else:
        lst.append(i)

T = int(input())
for i in range(T):
    tmp = []
    n = int(input())
    for j in lst:
        if j < n//2 + 1:
            if n-j in lst:
                tmp.append([j, n-j])
        else:
            break

    if len(tmp) == 1:
        print(tmp[0][0], tmp[0][1])
    else:
        min = 9999
        min_lst = [9999, 9999]
        for k in tmp:
            if min > k[1] - k[0]:
                min = k[1] - k[0]
                min_lst = [k[0], k[1]]
        print(min_lst[0], min_lst[1])