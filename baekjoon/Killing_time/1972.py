import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '*':
        break
    
    if len(s) == 1:
        print(s,'is surprising.')
        continue
    
    else:
        lst = [[] for i in range(len(s)-1)]
        check = False
        for i in range(1, len(s)): # i는 D-쌍을 의미
            for j in range(0, len(s)-i): # D-쌍이 D-유일인지 검증
                x = s[j]+s[j+i]
                if x in lst[i-1]:
                    check = True
                    break
                else:
                    lst[i-1].append(x)

            if check == True:
                print(s,'is NOT surprising.')
                break
            
        else:
            print(s,'is surprising.')