n = input()
s = 'abcdefghijklmnopqrstuvwxyz'
cnt = [0 for i in range(len(s))]
for i in n:
    cnt[s.index(i)] += 1
for i in cnt:
    print(i, end=' ')