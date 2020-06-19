n = int(input())
for i in range(n):
    sum = 0
    cnt = 0
    s = input()
    for j in range(len(s)):
        if s[j] == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)