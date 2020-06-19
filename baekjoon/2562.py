best = -9999
idx = -1
for i in range(9):
    n = int(input())
    if n > best:
        best = n
        idx = i
print(best);print(idx+1)
