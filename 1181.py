n = int(input())
lst = sorted(list(set(input() for i in range(n))), key = lambda x: (len(x), x))
for i in lst:
    print(i)
