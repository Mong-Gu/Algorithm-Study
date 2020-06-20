n = int(input())
lst = [list(map(int, input().split())) for i in range(n)]
ans = [1 for i in range(n)]
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    ans[i] += cnt

for i in ans:
    print(i, end = ' ')