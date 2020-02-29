# 제출 코드 : 다른 사람들 힌트 보고 영감얻음
def solution(citations):
    cnt = 0
    citations.sort(reverse = True)
    h = citations[0]

    while h != 0 :
        if citations.count(h): 
            cnt += citations.count(h)
        
        if cnt >= h: 
            return h
        else: 
            h -= 1
            
    return 0
'''
# 2차 코드
def solution(citations):
    n = len(citations)
    cnt = 0
    citations.sort(reverse = True) # 6, 5, 3, 1, 0
    h = citations[0]

    while h != 0 :
        if citations.count(h): 
            cnt += citations.count(h)
        
        if cnt >= h: 
            return h
        else: 
            h -= 1
'''
'''
# 1차 코드
def solution(citations):
    n = len(citations)
    h = 0
    cnt = 0
    citations.sort(reverse = True) # 6, 5, 3, 1, 0

    i = 0
    while i != n-1 :
        h = citations[i]
        tmp = citations.count(h)
        cnt += tmp
        if cnt >= h:
            return h
        else:
            i += tmp
            continue
'''