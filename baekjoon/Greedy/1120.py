a, b = input().split()

if len(a) == len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)

else: # len(a) < len(b)
    min_gap = 9999
    for i in range(len(b)-len(a)+1): 
    # 문자열 a를 문자열 b의 특정 부분과 비교하며 a를 어느 곳에 먼저 위치시킬지 결정
        tmp_cnt = 0
        for j in range(len(a)):
            if a[j] != b[j+i]:
                tmp_cnt += 1
        if min_gap > tmp_cnt:
            min_gap = tmp_cnt
    print(min_gap)