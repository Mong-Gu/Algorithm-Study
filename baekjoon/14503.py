import sys
n, m = map(int, input().split())
# n = 세로 길이, m = 가로 길이
r, c, d = map(int, input().split())
# r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수
lst = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]

"""
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1] lst[0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1] lst[1]
[1, 0, 0, 0, 1, 1, 1, 1, 0, 1] lst[2]
[1, 0, 0, 1, 1, 0, 0, 0, 0, 1] lst[3]
[1, 0, 1, 1, 0, 0, 0, 0, 0, 1] .
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1] .
[1, 0, 0, _, 0, 0, 0, 1, 0, 1] .
[1, 0, 0, 0, 0, 0, 1, 1, 0, 1] .
[1, 0, 0, 0, 0, 0, 1, 1, 0, 1] .
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1] .
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1] lst[10]
"""
cnt = 0 # 청소하는 영역의 개수
# for i in lst:
#         print(i)

while True:
    # 1. 현재 위치를 청소
    if lst[r][c] == 0:
        cnt += 1
        lst[r][c] = 2 # 상태가 2인 것은 벽은 아니고 청소가 된 영역
    check = False

    while True:
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행
    # d : 0->북쪽, 1->동쪽, 2->남쪽, 3->서쪽

        cond = lst[r][c-1] != 0 and lst[r-1][c] != 0 and lst[r][c+1] != 0 and lst[r+1][c] != 0

        if d == 0:
            if lst[r][c-1] == 0: # 2-a. 왼쪽 방향에 청소할 공간이 있으면
                c -= 1
                d = 3
                break
            else: # 왼쪽 방향에 청소할 공간이 없을 경우
                # 2-d. 네 방향 모두 청소를 할 수 없고, 뒤쪽이 벽인 경우
                if cond and lst[r+1][c] == 1:
                    check = True
                    break
                elif cond: # 2-c. 네 방향 모두 청소를 할 수 없기만 한 경우
                    r += 1
                    continue
                else: # 2-b. 단순히 왼쪽 방향에 청소할 공간이 없는 경우
                    d = 3
                    continue    

        elif d == 1:
            if lst[r-1][c] == 0: # 2-a. 왼쪽 방향에 청소할 공간이 있으면
                r -= 1
                d = 0
                break
            else: # 왼쪽 방향에 청소할 공간이 없을 경우
                # 2-d. 네 방향 모두 청소를 할 수 없고, 뒤쪽이 벽인 경우
                if cond and lst[r][c-1] == 1:
                    check = True
                    break
                elif cond: # 2-c. 네 방향 모두 청소를 할 수 없기만 한 경우
                    c -= 1
                    continue
                else: # 2-b. 단순히 왼쪽 방향에 청소할 공간이 없는 경우
                    d = 0
                    continue    
                
        elif d == 2:
            if lst[r][c+1] == 0: # 2-a. 왼쪽 방향에 청소할 공간이 있으면
                c += 1
                d = 1
                break
            else: # 왼쪽 방향에 청소할 공간이 없을 경우
                # 2-d. 네 방향 모두 청소를 할 수 없고, 뒤쪽이 벽인 경우
                if cond and lst[r-1][c] == 1:
                    check = True
                    break
                elif cond: # 2-c. 네 방향 모두 청소를 할 수 없기만 한 경우
                    r -= 1
                    continue
                else: # 2-b. 단순히 왼쪽 방향에 청소할 공간이 없는 경우
                    d = 1
                    continue

        else: # d == 3
            if lst[r+1][c] == 0: # 2-a. 왼쪽 방향에 청소할 공간이 있으면
                r += 1
                d = 2
                break
            else: # 왼쪽 방향에 청소할 공간이 없을 경우
                # 2-d. 네 방향 모두 청소를 할 수 없고, 뒤쪽이 벽인 경우
                if cond and lst[r][c+1] == 1:
                    check = True
                    break
                elif cond: # 2-c. 네 방향 모두 청소를 할 수 없기만 한 경우
                    c += 1
                    continue
                else: # 2-b. 단순히 왼쪽 방향에 청소할 공간이 없는 경우
                    d = 2
                    continue
    # print()
    # for i in lst:
    #     print(i)

    if check == True:
        break

print(cnt)