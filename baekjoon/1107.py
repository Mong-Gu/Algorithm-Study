""" n = input()
target = int(n)
m = int(input())
error = input().split()
now = 100

if target == 100: # 이동할 필요가 없는 경우
    print(0)

elif abs(target-now) <= m: # +, - 만으로 이동해도 되는 경우
    print(abs(target-now))

else: # 채널을 눌러야 하는 경우
    check = True
    for i in error:
        if i in set(n):
            check = False
            break
    if check: # 가야 할 채널의 번호를 다 누를 수 있는 경우
        print(len(n)) # 채널을 누른 수만큼 출력

    else: # 가야 할 채널의 번호 중 고장난 것이 있을 경우
        # 최대한 가까운 수로 이동하여 + 혹은 -를 한다
        # 최대한 가까운 수를 고르는 기준도 두 가지여야 한다
            # 1. +를 더 적게 할 수 있는 target보다 작은 수
            # 2. -를 더 적게 할 수 있는 target보다 큰 수
            # 1과 2를 비교해서 target과의 차이가 더 적은 수를 채택  
            # 하다 보니 느꼈는데, 가장 첫 번째 자리는 따로 정해줘야 한다

        def less_function(n, less):
            global target, error
            if str(target-1)[0] != n[0]: # 1만 빠져도 자릿수가 바뀌는 경우
                n = str(target-1)
            for i in range(len(n)):
                if n[i] not in error:
                    less += n[i]
                else:
                    m = [-1, 10] # MIN, target과의 거리
                    for j in range(10):
                        if str(j) not in error:
                            if abs(j-int(n[i])) <= m[1] and j > m[0]:
                                m = [j, abs(j-int(n[i]))]
                    less += str(m[0])
            return less

        def more_function(n, more):
            global target, error
            if str(target+1)[0] != n[0]: # 1만 빠져도 자릿수가 바뀌는 경우
                n = str(target+1)
            for i in range(len(n)):
                if n[i] not in error:
                    more += n[i]
                else:
                    M = [-1, 10] # MAX, target과의 거리
                    for j in range(10):
                        if str(j) not in error:
                            if abs(j-int(n[i])) <= M[1] and j > M[0]:
                                M = [j, abs(j-int(n[i]))]
                    more += str(M[0])
            return more

        a = less_function(n, '')
        b = more_function(n, '')
        print(a, b)
        print(len(n) + min(target-int(a), int(b)-target)) """

    # 조졌다


# https://hwiyong.tistory.com/232

""" 
enable_btn_set = {str(x) for x in range(11)}

N = int(input())
break_button_num = int(input())
if(break_button_num == 0):
    pass
else:    
    break_button = set(input().split())
    enable_btn_set -= break_button
    # 이렇게 하면 if not in ~ 이거 안 써도 된다.

result = abs(N - 100)
# 먼저 최악의 경우를 result에 저장한다. 단순히 + 혹은 - 만으로 움직인 경우임.

for i in range(1000001):
    # 일단 반복문의 범위가 100만 1이라는 것을 어떻게 생각했을까 신기하다.
    # 지금 머리가 띵해서 그런지 왜 이런지는 상상이 가질 않는다.
    is_enable = True
    for div_num in str(i):
        if(div_num not in enable_btn_set):
            is_enable = False
    if(is_enable):
        result = min(result, abs(N - i) + len(str(i)))
        # 오아. 채널을 len(str(i))번 누르고 i번에서 N까지 + 혹은 -로 움직인 횟수랑 result랑 비교했네 계속.
        
print(result) 
"""