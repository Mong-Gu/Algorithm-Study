lst = []
for i in range(5):
    lst.append(int(input()))

if lst[3] >= lst[4]: print(min(lst[:2]) + lst[4] - 50)
else: print(min(lst[:2]) + lst[3] - 50)