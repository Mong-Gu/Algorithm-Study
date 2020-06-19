n = input()
if len(n) == 1:
    n = '0'+n
target = n
cnt = 0
while True:
    cnt += 1
    tmp = str(int(n[0]) + int(n[1]))
    n = n[-1] + tmp[-1]
    if target == n:
        break
print(cnt)