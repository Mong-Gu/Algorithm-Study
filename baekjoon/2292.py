n = int(input())

i = 0
j = 0 # 계속 1씩 증가
cnt = 1
while n > 6 * (i + j) + 1:
    cnt += 1
    i += j
    j += 1
print(cnt)