s = list(input())

cnt = 0
while True:
    cnt += 1
    lst = ['%s' %i for i in range(10)]
    for i in lst:
        if i in s:
            s.remove(i)
        elif i == '6' and '9' in s:
            s.remove('9')
        elif i == '9' and '6' in s:
            s.remove('6')
    if len(s) == 0:
        break
print(cnt)