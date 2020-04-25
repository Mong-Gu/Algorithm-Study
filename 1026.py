n = int(input())
a = sorted(list(map(int, input().split(' '))))
b = sorted(list(map(int, input().split(' '))), reverse = True)
x = 0
for i in range(n):
    x += a[i]*b[i]
print(x)