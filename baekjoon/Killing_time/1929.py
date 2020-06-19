from math import sqrt

m, n = map(int, input().split()) # start, end

for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
    else:
        for j in range(2, int(sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            print(i)

# 에라토스테네스의 체로 풀라고 했는데, 구현 방법을 몰라서 걍 내 맘대로 풀었음.
# 성능에 문제가 없어서 통과해버림.