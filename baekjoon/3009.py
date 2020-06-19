lst = [input().split() for i in range(3)]
x_lst = sorted([lst[i][0] for i in range(3)])
y_lst = sorted([lst[i][1] for i in range(3)])
x = 0
y = 0

if x_lst.count(x_lst[0]) == 1 : 
    x = x_lst[0]
else: 
    x = x_lst[2]

if y_lst.count(y_lst[0]) == 1 : 
    y = y_lst[0]
else: 
    y = y_lst[2]

print(x, y)