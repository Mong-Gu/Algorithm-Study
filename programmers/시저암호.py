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
# 1차 코드 틀렸다는 걸 깨달은 다음 만든 코드 - 문자열에서 뜯어 고치는 것
def solution(s, n):
    small = 'abcdefghijklmnopqrstuvwxyz'
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in range(len(s)):
        if s[i] in small: # 소문자일 경우
            if small.index(s[i]) + n <= 25:
                if i != len(s)-1:
                    s = s[:i] + small[small.index(s[i])+n] + s[i+1:]
                else:
                    s = s[:i] + small[small.index(s[i])+n]
            else:
                if i != len(s)-1:
                    s = s[:i] + small[small.index(s[i])+n-26] + s[i+1:]
                else:
                    s = s[:i] + small[small.index(s[i])+n-26]

                
        elif s[i] in capital:
            if capital.index(s[i]) + n <= 25:
                if i != len(s)-1:
                    s = s[:i] + capital[capital.index(s[i])+n] + s[i+1:]
                else:
                    s = s[:i] + capital[capital.index(s[i])+n]
            else:
                if i != len(s)-1:
                    s = s[:i] + capital[capital.index(s[i])+n-26] + s[i+1:]
                else:
                    s = s[:i] + capital[capital.index(s[i])+n-26]
                
        else: # 공백일 경우
            continue
            
    return s


'''


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
