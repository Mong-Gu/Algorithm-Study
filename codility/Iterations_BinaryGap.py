def solution(N):
    binary = bin(N)[2:]
    flag = 0
    cnt = 0
    max_cnt = 0
    for idx, val in enumerate(binary):
        if val == '1':
            if flag and cnt != 0:
                max_cnt = max(cnt, max_cnt)
                cnt = 0
            else:
                flag = 1
        else: # val == '0'
            if flag:
                cnt += 1
    return max_cnt
