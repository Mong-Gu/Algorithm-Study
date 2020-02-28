# 제출코드
def solution(s, n):
    small = ','.join('abcdefghijklmnopqrstuvwxyz').split(',')
    capital = ','.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ').split(',')
    s = ','.join(s).split(',')
    
    for i in range(len(s)):
        if s[i] in small: # 소문자일 경우
            if small.index(s[i]) + n <= 25:
                s[i] = small[small.index(s[i])+n]
            else:
                s[i] = small[small.index(s[i])+n-26]

        elif s[i] in capital:
            if capital.index(s[i]) + n <= 25:
                s[i] = capital[capital.index(s[i])+n]
            else:
                s[i] = capital[capital.index(s[i])+n-26]
                
        else: # 공백일 경우
            continue

    return ''.join(s)

'''
# 1차 코드
def solution(s, n):
    small = ','.join('abcdefghijklmnopqrstuvwxyz').split(',')
    capital = ','.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ').split(',')
    
    for i in range(len(s)):
        if s[i] in small: # 소문자일 경우
            if small.index(s[i]) + n <= 25:
	            s = s.replace(s[i], small[small.index(s[i])+n])
            else:
                s = s.replace(s[i], small[small.index(s[i])+n]-26)

                
        elif s[i] in capital:
            if capital.index(s[i]) + n <= 25:
                s = s.replace(s[i], capital[capital.index(s[i])+n])
            else:
                s = s.replace(s[i], capital[capital.index(s[i])+n]-26)
                
        else: # 공백일 경우
            continue
            
    return s
'''
