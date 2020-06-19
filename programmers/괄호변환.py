'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''
def translation(p):
    if len(p) == 0: return p # 1번 요구사항 겸 재귀함수의 탈출 조건

    cnt_left = 0
    cnt_right = 0
    answer = ''

    for i in range(len(p)): # 2번 요구 사항
        if p[i] == '(': cnt_left += 1
        elif p[i] == ')' : cnt_right += 1

        if (cnt_left != 0 and cnt_right != 0) and cnt_left == cnt_right:
            u = list(p[:i+1])
            v = list(p[i+1:])
            break

    tmp = u[:]
    i = 0
    while len(tmp) != 0:
        if i == len(tmp)-1: # "올바른 괄호 문자열"이 아닐 때 탈출 조건
            break
        if tmp[i] == '(' and tmp[i+1] == ')':
            tmp.pop(i)
            tmp.pop(i)
            i = 0
        else:
            i += 1

    # print(tmp)
    # print(u)
    # print(v)

    if len(tmp) == 0: # 3번 요구사항이 만족된다면
        answer = answer + ''.join(u)
        print('answer:', answer)
        translation(v)

    else: # 3번 요구사항이 만족되지 않아 4번으로 내려온다면
        return

#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.

    print(answer)

#translation("(()())()")
#translation(")(")
translation("()))((()")
    # "( ( ) ( ) ) ( )" ->	"( ( ) ( ) ) ( )"
    # ") (" => "( )"
    # "( ) ) ) ( ( ( )" -> "( ) ( ( ) ) ( )"



# 중도 포기...