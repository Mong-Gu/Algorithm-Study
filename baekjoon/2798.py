n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
best = -1
for i in range(n-2):
    if lst[i]+lst[i+1]+lst[i+2] > m:
        break
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = lst[i] + lst[j] + lst[k]
            if sum > m:
                break
            if sum > best:
                best = sum
print(best)