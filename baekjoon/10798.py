lst = []
max = 0
for i in range(5):
    lst.append(input())
    if len(lst[-1]) > max:
        max = len(lst[-1])

for idx in range(max):
    for line in lst:
        try:
            print(line[idx], end = '')
        except:
            continue