n = int(input())
if n < 99:
    print(n)

else:
    cnt = 99
    for num in range(100, n+1):
        num = str(num)
        gap = int(num[1]) - int(num[0])
        for j in range(1, len(num)-1):
            if gap != int(num[j+1]) - int(num[j]):
                break
        else:
            cnt += 1
    print(cnt)            