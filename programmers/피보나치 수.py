# 2차 코드

# 아니 문제 현기증나네;;; 질문하기 봐도 이상한거같아 ㅏ아아아아아아아아아아 내일 하자 머리식히고

# 1차 코드 : 대체 왜 런타임 에러가 뜨지 몇 몇 케이스에서?  
dic = {0:0, 1:1}

def solution(n):
    if n in dic:
        return dic[n] % 1234567
    
    output = solution(n-1) + solution(n-2)
    dic[n] = output
    
    return dic[n] % 1234567


