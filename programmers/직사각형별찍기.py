a, b = map(int, input().strip().split(' '))
# 가로의 길이 a
# 세로의 길이 b

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')