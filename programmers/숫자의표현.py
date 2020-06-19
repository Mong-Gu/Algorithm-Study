def solution(n):
    cnt = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum = sum + j
            if n == sum:
                cnt += 1
            elif sum > n:
                break

    return cnt