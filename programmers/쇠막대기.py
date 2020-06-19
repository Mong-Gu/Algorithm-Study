def solution(arr):
    cnt = 0
    stick_cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            stick_cnt += 1
        if arr[i] == ')':
            if arr[i-1] == '(':
                stick_cnt -= 1
                cnt += stick_cnt
            elif arr[i-1] == ')':
                stick_cnt -= 1
                cnt += 1
    
    return cnt