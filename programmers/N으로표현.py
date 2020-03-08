# 잠만 너무 배고파서 참질 못하겠어

def solution(N, number):
    lst = [set() for i in range(8)] # [{}, {}, {}, {}, {}, {}, {}, {} ]
    for i in range(len(lst)):
        lst[i].add(int(str(N)*(i+1)))

    # for i, elem in enumerate(lst):



    if number in lst[i]:
        answer = i+1

    print(lst)
    # return answer

solution(5, 12)
# solution(2, 11)

# 0 : 0
# 1 : [5]
# 2 : 사칙연산 1 / [5+5, 5-5, 5x5, 5//5]
# 3 : 사칙연산 1 , 1 사칙연산 2 / []
# 4 : 사칙연산 1 , 2 사칙연산 2 , 1 사칙연산 3 / []