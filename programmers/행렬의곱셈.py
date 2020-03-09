import numpy as np
def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    return np.dot(a, b).tolist()


# 다른 사람 코드
'''
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]


이거 보고 공부하기. 내가 원래 시도하려던 거랑 똑같은 원린데 난 구현하지 못했어.
하지만 속도는 numpy 이용하는게 수 배에서 수십 배는 빠름.
아래는 내가 하던거.

def solution(arr1, arr2):
    # answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1[0]))]    
    # print(answer)
    
    # for i in range(len(arr1)):
    #     for j in range(len(arr2[0])):
    #         for k in range():
    #             arr1[i][j] * arr2[j][i]
'''
