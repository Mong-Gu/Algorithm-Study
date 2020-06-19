lst = [0 for i in range(10)]
x = 1

for i in range(3):
    x *= int(input())

x = str(x)

for i in range(len(x)):
    lst[(int(x[i]))] += 1

for i in range(10):
    print(lst[i])