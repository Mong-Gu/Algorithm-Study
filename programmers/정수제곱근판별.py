# 제출 코드
import math

def solution(n):
    for i in range(1, round(math.sqrt(50000000000000))):
        if i*i == n:
            return pow(i+1, 2)
    return -1


# 1차 코드
import math

def solution(n):
    num = math.sqrt(n)
    if n / num == num:
        return pow(num+1, 2)
    else:
        return -1

