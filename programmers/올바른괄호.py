# 제출 코드
def solution(s):
    if s.count('(') != s.count(')'):
        return False

    lst = []
    i = 0
    while len(s) != 0:
        if i == len(s):
            break
            
        if len(lst) >= 1 and lst[-1] == '(' and s[i] == ')':
            lst.pop()
            i += 1
            continue
            
        lst.append(s[i])
        i+=1
        
    if len(lst) == 0: return True
    else: return False
'''
# 4차 코드
def solution(s):
    if s.count('(') != s.count(')'):
        return False

    lst = []
    i = 0
    while len(s) != 0:
        if i == len(s):
            break
        lst.append(s[i])
        if len(lst) > 1 and lst[-1] == ')' and lst[-2] == '(':
            lst.pop()
            lst.pop()
        i+=1
        
    if len(lst) == 0: return True
    else: return False
'''
'''
# 3차 코드
def solution(s): # 이것도 효율성 1번에서 시간초과 뜬다. 아마 len(s) = 10만 이면서 올바른 괄호인 것 같아.
    if s.count('(') != s.count(')'):
        return False
    
    while len(s) != 0:
        try :
            idx = s.index('()')
            s = s[:idx] + s[idx+2:]
        except ValueError :
            break
            
    if len(s) == 0: return True
    else: return False
'''
'''
# 2차 코드
def solution(s):
    i = 0
    if s.count('(') != s.count(')'): # 이거 넣었더니 효율성 테스트 2개 중 1개는 통과하게 됨
        return False
    
    while len(s) != 0:
        if i == len(s)-1:
            break
        if s[i] == '(' and s[i+1] == ')':
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    if len(s) == 0: return True
    else: return False
'''
'''
# 1차 코드
def solution(s):
    i = 0
    while len(s) != 0:
        if i == len(s)-1:
            break
        if s[i] == '(' and s[i+1] == ')':
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    if len(s) == 0: return True
    else: return False
'''