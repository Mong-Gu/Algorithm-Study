n = int(input())
lst = sorted([list(map(int, input().split())) for i in range(n)], key = lambda x : (x[1], x[0]))
cnt = 1
result = [lst[0]]
for i in range(1, len(lst)):
    if lst[i][0] >= result[-1][1]:
        cnt += 1
        result.append(lst[i])
print(cnt)