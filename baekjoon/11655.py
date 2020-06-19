import string 

s = input()
lower = string.ascii_lowercase
upper = string.ascii_uppercase
ans = ''

for i in s:
    if i in lower:
        tmp = lower.index(i)
        if tmp >= 13:
            tmp -= 13
        else:
            tmp += 13
        ans += lower[tmp]

    elif i in upper:
        tmp = upper.index(i)
        if tmp >= 13:
            tmp -= 13
        else:
            tmp += 13
        ans += upper[tmp]

    else:
        ans += i

print(ans)