# 2차 코드
def solution(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        x = (fibo[i-1] + fibo[i-2]) % 1234567
        fibo.append(x)
    return fibo[-1]

'''
# 1차 코드
# 테스트케이스 7, 10, 13, 14번 런타임 에러 발생
# IDLE에서 n을 아주 큰 값으로 두고 함수를 돌려보니
# RecursionError: maximum recursion depth exceeded 발생
# 재귀함수로는 구현 불가능할 듯

dic = {0:0, 1:1}
def solution(n):
    if n in dic:
        return dic[n]
    dic[n] = (solution(n-1) + solution(n-2)) % 1234567
    return dic[n]
'''

