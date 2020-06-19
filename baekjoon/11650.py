n = int(input())
lst = sorted([list(map(int, input().split())) for i in range(n)], key = lambda x: (x[0], x[1]))
for i in lst:
    print(i[0], i[1])