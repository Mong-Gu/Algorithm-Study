n = int(input())
cnt = 0
for i in range(n):
    s = input()
    lst = []
    for idx, alphabet in enumerate(s):
        if alphabet not in lst:
            lst.append(alphabet)
        else:
            if s[idx-1] == alphabet:
                pass
            else:
                break
    else:
        cnt += 1
print(cnt)