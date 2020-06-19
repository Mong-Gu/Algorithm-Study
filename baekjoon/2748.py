n = int(input())
if n == 1:
    print(1)
else:
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-2]+lst[i-1])
    print(lst[-1])