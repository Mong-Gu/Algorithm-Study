from math import sqrt

m = int(input()) # start
n = int(input()) # end
sum = 0
min = 0

for i in range(m, n+1):
    if i == 1:
        continue
    elif i == 2:
        sum += i
        min = i
    else:
        for j in range(2, int(sqrt(i)+1)):
            if i % j == 0:
                break
        else:
            if sum == 0:
                min = i
            sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)

""" 
고려해야 될 것
1. 소수 판별 알고리즘의 성능
2. m이 1로 주어질 경우 1은 걸러낼 수 있어야 하며
3. m이 2일 경우에는 소수를 판별하는 알고리즘(15~17 line)에서 체크가 안되므로
   임의로 sum에 넣어줘야 함
"""