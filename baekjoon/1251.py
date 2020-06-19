s = input()
best = 'z'*50
for i in range(len(s)-3):
    for j in range(i+1, len(s)-1):
        a = list(s[:i+1]); b = list(s[i+1:j+1]); c = list(s[j+1:])
        a.reverse(), b.reverse(); c.reverse()
        target = (''.join(a) + ''.join(b) + ''.join(c))

        if best > target:
            best = target
print(best)