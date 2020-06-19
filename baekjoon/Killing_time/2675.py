T = int(input())
for i in range(T):
    n, s = input().split()
    new_s = ''
    for j in range(len(s)):
        new_s += s[j]*int(n)
    print(new_s)