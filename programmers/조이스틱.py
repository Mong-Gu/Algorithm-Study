# 2차 코드

# 건드리지를 못하겠네...
# '질문하기'에서 임영선님 케이스를 참고하여 나중에 짜보자. 지금은 졸려서 못하겠엉.


# 1차 코드 : 테스트케이스 10번, 11번 실패.
def solution(name):
    # N  O  P  Q  R S T U V W X Y Z <- A -> B C D E F G H I J K  L  M
    # 13 12 11 10 9 8 7 6 5 4 3 2 1 <- 0 -> 1 2 3 4 5 6 7 8 9 10 11 12

    #  A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
    #  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    #                               13 12 11 10 9  8  7  6  5  4  3  2  1

    cnt = 0
    direction = ''

    # 진행방향 설정
    if name[1] == 'A' : direction = 'left'
    else : direction = 'right' # name[-1] == 'A' 이 꼭 아니어도 됨.

    if direction == 'right':
        print('방향은 right\n')
        for i in range(len(name)):
            # 알파벳 바꾸는 로직
            if name[i] == 'A':
                pass

            elif name[i] in 'BCDEFGHIJKLM': # 위쪽으로 이동
                cnt += (ord(name[i]) - ord('A'))
                print(i,'번째에서 위쪽으로 이동 -> cnt:', cnt)

            else: # 아래쪽으로 이동
                cnt += (ord('A') + 26 - ord(name[i]))
                print(i,'번째에서 아래쪽으로 이동 -> cnt:', cnt)

            cnt += 1 # 오른쪽으로 한 칸 이동
            print(i,'번째에서',i+1,'번째로 이동 후 cnt:', cnt, '\n')

        cnt -= 1 # 마지막 원소에선 오른쪽으로 움직이지 않았으므로 cnt 1 감소

    else:
        print('방향은 left\n')
        if name[0] == 'A':
            pass

        elif name[0] in 'BCDEFGHIJKLM': # 위쪽으로 이동
            cnt += (ord(name[0]) - ord('A'))
            print(0,'번째에서 위쪽으로 이동 -> cnt:', cnt)

        else: # 아래쪽으로 이동
            cnt += (ord('A') + 26 - ord(name[i]))
            print(0,'번째에서 아래쪽으로 이동 -> cnt:', cnt)
        
        cnt += 1 # 왼쪽으로 한 칸 이동
        print(0,'번째에서',len(name)-1,'번째로 이동 후 cnt:', cnt, '\n')



        for i in range(len(name)-1, 1, -1):
            # 알파벳 바꾸는 로직
            if name[i] == 'A':
                pass
            elif name[i] in 'BCDEFGHIJKLM': # 위쪽으로 이동
                cnt += (ord(name[i]) - ord('A'))
                print(i,'번째에서 위쪽으로 이동 -> cnt:', cnt)
            else:
                cnt += (ord('A') + 26 - ord(name[i]))
                print(i,'번째에서 아래쪽으로 이동 -> cnt:', cnt)
            cnt += 1 # 왼쪽으로 한 칸 이동

            print(i,'번째에서',i-1,'번째로 이동 후 cnt:', cnt, '\n')
        cnt -= 1 

    print('최종 cnt:', cnt)
    return cnt