for x in range(10):
    length = int(input()) # 건물들의 개수
    lst = list(map(int, input().split())) # 각 건물의 높이
    cnt = 0
    for i in range(2, length-2): # 각 건물 비교
        for j in range(1, lst[i]+1): # i번째 건물의 층마다 확인
            if lst[i-2] < j and lst[i-1] < j and lst[i+1] < j and lst[i+2] < j:
                cnt += 1
    print('#{} {}'.format(x+1, cnt))