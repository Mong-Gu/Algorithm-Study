n = int(input())
s = input()
alpha = ' abcdefghijklmnopqrstuvwxyz'
sum = 0
for i in range(n):
    sum += (alpha.index(s[i]) * pow(31, i))
print(sum % 1234567891)