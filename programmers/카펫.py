from math import sqrt

# 전체 사각형의 경우의 수 구한 후 빨간색 사각형들이 들어올 수 있는 크기로 만들기
def Whole(n):
    lst = []
    for i in range(3, round(sqrt(n)) + 1): # 가로는 어차피 3 이상이어야 함
        if n % i == 0:
            lst.append([(n//i) - 2, i - 2]) # 빨간색 사각형이 들어올 수 있는 크기의 공간으로 조정
    return lst

# 빨간색 사각형의 경우의 수 구하기
def Red(n):
    lst = []
    for i in range(1, round(sqrt(n)) + 1):
        if n % i == 0:
            lst.append([n//i, i])
    return lst

def solution(brown, red):
# 갈색 사각형 개수 = 
# 빨간색 직사각형의 대각선으로 뻗어나가는 사각형 4개 +
# ( (빨간색 직사각형의 가로 길이) x 2 ) 개 +
# ( (빨간색 직사각형의 세로 길이) x 2 ) 개

    total_case = Whole(brown + red) # 전체 사각형의 [가로, 세로] 경우의 수 구하기
    red_case = Red(red) # 빨간색 사각형의 [가로, 세로] 경우의 수 구하기

    for i in total_case:
        for j in red_case:
                if i == j:
                    return [i[0]+ 2, i[1] + 2]



'''
깔끔하게 정리한 것

from math import sqrt

def Whole(n):
    lst = []
    for i in range(3, round(sqrt(n)) + 1):
        if n % i == 0:
            lst.append([(n//i) - 2, i - 2])
    return lst

def Red(n):
    lst = []
    for i in range(1, round(sqrt(n)) + 1):
        if n % i == 0:
            lst.append([n//i, i])
    return lst

def solution(brown, red):
    total_case = Whole(brown + red)
    red_case = Red(red)

    for i in total_case:
        for j in red_case:
                if i == j:
                    return [i[0]+ 2, i[1] + 2]
'''

'''
베스트 코드
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
'''