k = int(input())
lst = []
for i in range(k):
    x = int(input())
    if x == 0 and len(lst) > 0:
        lst.pop()
    else:
        lst.append(x)
print(sum(lst))

