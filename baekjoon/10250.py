T = int(input())
for i in range(T):
    h, w, n = map(int, input().split())
    YY = 0
    XX = 1
    while n != 0:
        YY += 1
        if YY > h and XX != w:
            YY = 1
            XX += 1
        n -= 1
    if XX < 10:
        print('{}0{}'.format(YY, XX))
    else:
        print('{}{}'.format(YY, XX))