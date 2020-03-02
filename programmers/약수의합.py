# 제출 코드
def solution(n):
    if n == 0 or n == 1: return n
    lst = []
    
    for i in range(1, n+1):
        if n//i < i: break # 이걸 안쓰고 그냥 range를 sqrt쓸 걸 그랬다
        if n % i == 0:
            if i in lst:
                continue
            lst.append(i)
            if n//i != i: # 제곱근이 아닐 경우에만!
                lst.append(n//i)
    
    return sum(lst)

'''
# 1차 코드
def solution(n):
    lst = []
    if n == 0 or n == 1:
        return n

    for i in range(1, (n+1)//2):
        if n % i == 0:
            if i in lst:
                continue
            lst.append(i)
            print(lst)
            if n//i != i:
                lst.append(n//i)
            print(lst)

    print(sum(lst))
    return sum(lst)

'''

'''
# 2차 코드
def solution(n):
    lst = []
    if n == 0:
        return sum([i for i in range(3001)])
    elif n == 1:
        return 1

    for i in range(1, n+1):
        if n//i < i: break
        if n % i == 0:
            if i in lst:
                continue
            lst.append(i)
            lst.append(n//i)
    
    print(lst)
    return sum(lst)
'''