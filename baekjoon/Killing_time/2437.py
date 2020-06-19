import sys
n = int(input())
lst = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse = True)
# print(lst)
for i in range(1, sum(lst)+1):
    # print('i=', i)
    if i in lst:
        continue
    ans = 0
    check = False
    # print('ans', ans)
    for j in range(len(lst)):
        if ans + lst[j] > i:
            continue
        elif ans + lst[j] == i:
            check = True
            break
        else: # ans + lst[j] < i
            ans += lst[j]
            # print('ans', ans)
            continue
    if not check:
        print(i)
        break