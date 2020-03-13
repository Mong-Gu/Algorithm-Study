# 제출 코드
def solution(n):
    if n == 2: return 1 # [2]
    elif n == 3 or n == 4: return 2 #[2, 3]

    count = 2 # [2, 3]은 미리 포함
    check = False

    for i in range(5, n+1, 2):
        if i % 3 == 0:
            continue
        
        X = round(i ** 0.5) + 1
        for j in range(2, X):
            if i % j == 0:
                check = True # 소수가 아님을 확인
                break
        if check == False:
            count += 1
        else: # check = True
            check = False
    
    return count

'''
# 2차 코드
def solution(n):
    if n == 2: return 1 # [2]
    elif n == 3 or n == 4: return 2 #[2, 3]

    count = 2 # [2, 3]은 미리 포함
    check = False

    for i in range(5, n+1, 2):
        X = round(i ** 0.5) + 1
        for j in range(2, X):
            if i % j == 0:
                check = True # 소수가 아님을 확인
                break
        if check == False:
            count += 1
        else: # check = True
            check = False
    
    return count




# 1차 코드 :  시간초과 많이 뜸
def solution(n):
    if n == 2: return 1
    elif n == 3: return 2
    
    count = 2 # 2,3은 자동 포함
    check = False
    for i in range(4, n+1):
        if i % 2 == 0:
            continue
        
        for j in range(2, i):
            if i % j == 0:
                check = True
                break
        if check == False:
            count = count + 1
        else:
            check = False

    print(count)
    return count

n = 10
solution(n)
'''

# -------------------------------------------------------------

'''
# 프로그래머스 1등 답안 : 에레토스테네스의 체. 보고 공부하자...
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''
