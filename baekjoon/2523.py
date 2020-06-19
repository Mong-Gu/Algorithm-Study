n = int(input())
for i in range(1, 2*n):
    if i <= n:
        print('*'*i)
    else:
        print('*'*(-i+2*n))