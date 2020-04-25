# ATM기

n = int(input())
p = [int(x) for x in input().split(' ')]
sum = 0
p.sort()
for i in range(len(p)):
    for j in range(0, i+1):
        sum = sum + p[j]
print(sum)