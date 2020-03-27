n = int(input())

if n % 5 == 0:
    print(n//5)

elif n < 5:
    if n == 3:
        print(1)
    else:
        print(-1)

else:
    lst = []
    i = 1

    while n >= 3: # 이걸 처음엔 n > 0 이라고 생각했는데 아니었네
        n -= 3
        if n % 5 == 0:
            lst.append(i + n//5)
        i += 1

    if len(lst) == 0:
        print(-1)
    else:
        print(min(lst))