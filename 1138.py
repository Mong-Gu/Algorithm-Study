n = int(input())
p = [int(x) for x in input().split(' ')]

result = []
for i in range(len(p)-1, -1, -1):
    if len(result) == p[i]:
        result.append(i+1)
    else:
        result.insert(p[i], i+1)

x = [str(i) for i in result]
print(' '.join(x))