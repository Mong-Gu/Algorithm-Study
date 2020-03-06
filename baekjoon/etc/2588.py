n = int(input())
m = input()
lst = []
for i in range(2, -1, -1):
    x = int(m[i]) * n
    print(x)
    lst.append(x * (pow(10, 2-i)))
print(sum(lst))
