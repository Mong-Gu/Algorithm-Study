n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    lst = [0, 1, 2] + [0 for i in range(n-2)]
    for i in range(3, n+1):
        lst[i] = lst[i-2] + lst[i-1]
    print(lst[n] % 10007)
# 아니 이거 왜그래? 스트레스 받게 하네