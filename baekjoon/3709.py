t = int(input())

for x in range(t):
    n, r = map(int, input().split())
    board = [[0 for i in range(n+2)] for j in range(n+2)] # 테두리까지 반영한 보드
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = 1 # 실제 보드 크기
    for i in range(r):
        a, b = map(int, input().split())
        board[a][b] = 2 # 거울 위치
    
    x, y = map(int, input().split())
    board[x][y] = 3 # 레이저 위치. 굳이 필요 없음.

    # # 동-남-서-북
    # # 1: 동, 2:서, 3:남, 4:북
    if y == 0:
        direction = 1
    elif x == 0:
        direction = 3
    elif y == n+1:
        direction = 2
    else:
        direction = 4

    dir_lst = [1, 3, 2, 4]
    loc = 3
    
    while loc != 0:
        if loc == 2:
            if direction == 4:
                direction = 1
            else:
                direction = dir_lst[dir_lst.index(direction)+1]

        if direction == 1:
            y += 1
        elif direction == 3:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1

        loc = board[x][y]

    print(x, y)

# ???????????????????? 왜 런타임에러야 이게???????? 잘만 돌아가는데요...
# 일단 포기
