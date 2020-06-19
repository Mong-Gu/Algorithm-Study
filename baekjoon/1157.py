s = input().upper()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
best = [-1, '']
second = [-2, '']
for k, i in dic.items():
    if i >= best[0]:
        second = best
        best = [i, k]
if best[0] == second[0]:
    print('?')
else:
    print(best[1])