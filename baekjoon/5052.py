import sys
t = int(input())
for i in range(t):
    lst = sorted([sys.stdin.readline().strip() for i in range(int(input()))])
    print(lst)
    for j in range(len(lst)-1):
        if lst[j] in lst[j+1]:
            print('NO')
            break
    else:
        print('YES')

# 문자열 간의 대소비교가 이루어질 때의 특성을 명확히 이해하라.