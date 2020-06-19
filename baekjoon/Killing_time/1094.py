x = int(input())
lst = [64]
while sum(lst) > x:
    tmp = lst.pop()//2
    lst.extend([tmp, tmp])
    if sum(lst[:-1]) >= x:
        lst.pop()
print(len(lst))