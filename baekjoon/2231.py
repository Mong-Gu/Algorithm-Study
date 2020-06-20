n = int(input())
for i in range(1, n):
    sum = i
    for j in str(i):
        sum += int(j)
    if n == sum:
        print(i)
        break
else:
    print(0)