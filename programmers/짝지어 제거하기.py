# 2차 코드
def solution(s):
    if len(s) % 2 != 0: return 0
    
    lst = ','.join(s).split(',')
    i = 0
    while i != len(lst)-1:
        if lst[i] == lst[i+1]:
            if len(s) == 2:
                return 1
            lst.remove(lst[i])
            lst.remove(lst[i])
            print(lst)
            i = 0
        else:
            i += 1

    return 0


# 1차 코드 : 효율성에서 박살남
def solution(s):
    if len(s) % 2 != 0: return 0
    
    i = 0
    while i != len(s)-1:
        if s[i] == s[i+1]:
            if len(s) == 2:
                return 1
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1

    return 0