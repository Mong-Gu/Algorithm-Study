n, m = map(int, input().split())
lst = [input() for i in range(n)]

best = 999999
for i in range(m-7): # 8*8 사각형의 왼쪽 제일 위가 되는 기준점
    for j in range(n-7): # 8*8 사각형이 아래로 내려갈 수 있는 거리
        cnt_a = 0
        cnt_b = 0
        for a in range(j, j+8):
            for b in range(i, i+8):
                if (a+b) % 2 == 0:
                    if lst[a][b] != 'W':
                        cnt_a += 1
                    else:
                        cnt_b += 1
                else:
                    if lst[a][b] != 'B':
                        cnt_a += 1
                    else:
                        cnt_b += 1
        x = min(cnt_a, cnt_b)
        if best > x:
            best = x
print(best)