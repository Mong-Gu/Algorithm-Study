# 거스름돈

def change(n, cnt):
    lst = [500, 100, 50, 10, 5, 1]
    for money in lst:
        if n >= money:
            n -= money
            cnt += 1
            break
    return n, cnt

n = 1000 - int(input())
cnt = 0
while n != 0:
    n, cnt = change(n, cnt)
print(cnt)