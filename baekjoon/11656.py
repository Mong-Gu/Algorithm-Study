s = input()
lst = sorted([s[i:] for i in range(len(s))])
for i in lst:
    print(i)