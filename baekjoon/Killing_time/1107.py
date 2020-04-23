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