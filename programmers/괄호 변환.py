def separate_p_to_u_and_v(p):  # p를 u, v로 분리
    cnt_left = 0
    cnt_right = 0
    u = ''
    v = ''
    for i, v in enumerate(p):
        if v == '(':
            cnt_left += 1
        else:
            cnt_right += 1
        if cnt_left == cnt_right:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u, v

def valid_for_right(u): # u가 올바른 괄호 문자열인지 확인
    stack = []
    for i in u:
        stack.append(i)
        while len(stack) >= 2 and (stack[-2] == '(' and stack[-1] == ')'):
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def if_u_is_not_right(u, v): # 문자열 u가 올바르지 않을 때 동작
    tmp = '(' + solution(v) + ')'
    u = u[1:-1]
    new_u = ''
    for i in range(len(u)):
        if u[i] == '(':
            new_u += ')'
        else:
            new_u += '('
    return tmp + new_u

def solution(p):

    # step 1
    if len(p) == 0:
        return ''
    
    # step 2
    u, v = separate_p_to_u_and_v(p)

    # step 3
    if valid_for_right(u):
        return u + solution(v)
    else:
        return if_u_is_not_right(u, v)

# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))