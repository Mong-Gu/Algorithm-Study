# 제출코드 (아예 새로 2월 28일 도전)
def solution(s):
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            continue
        else:
            if idx % 2 == 0:
                s = s[:i] + s[i].upper() + s[i+1:]
                idx += 1
            else:
                s = s[:i] + s[i].lower() + s[i+1:]
                idx += 1
    return s

'''
# 3차 코드
def solution(s): # s = 'try hello world'
    lst = []
    cnt = 0
    last_space = 0
    for i in range(len(s)):
        if s[i] != ' ': # 공백이 아닌, 글자일 경우
            if cnt % 2 == 0:
                s = s[:i] + s[i].upper() + s[i+1:]
                cnt = cnt + 1
            else:
                s = s[:i] + s[i].lower() + s[i+1:]
                cnt = cnt + 1

        else: # 공백일 경우
            if i == 0: # 처음부터 공백일 경우
                lst.append(' ')


            if last_space == 0 and i != 0: # 첫 단어일 경우
                lst.append(s[:i])
                lst.append(' ')
            else: # 첫 단어가 아닐 경우
                lst.append(s[last_space+1:i])
            last_space = i
            cnt = 0


# 2차 코드
def solution(s):
    lst = s.split()
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j % 2 == 0:
                lst[i] = lst[i][:j] + lst[i][j].upper() + lst[i][j+1:]
            else:
                lst[i] = lst[i][:j] + lst[i][j].lower() + lst[i][j+1:]
    return ' '.join(lst)

# 1 차 코드

def solution(s):
    lst = s.split()
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j % 2 == 0:
                lst[i] = lst[i].replace(lst[i][j], lst[i][j].upper())
                print(lst)
    
    return ' '.join(lst)
'''