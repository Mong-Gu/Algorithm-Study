# 1차 코드
# def solution(s):
#     num = ['0','1','2','3','4','5','6','7','8','9','10']
#     arr = []
#     start = 0
#     answer = 0

#     for i in range(2, len(s)+1):
#         if i == len(s):
#             arr.append(s[start:])
#             break
#         if s[i] in num:
#             arr.append(s[start:i])
#             start = i

#     for i in range(3):
#         if len(arr[i]) == 2:
#             arr[i] += '_'
            
#         tmp = int(arr[i][0])

#         if arr[i][1] == 'D':
#             tmp = pow(tmp, 2)
#         elif arr[i][1] == 'T':
#             tmp = pow(tmp, 3)
        
#         if arr[i][2] == '*':
#             if i == 0:
#                 tmp *= 2
#             else:
#                 tmp *= 2
#                 answer *= 2
#         elif arr[i][2] == '#':
#             tmp = -tmp

#         answer += tmp
    
#     print(answer)
#     return answer

# # 2차 코드
# def solution(s):
#     num = ['0','1','2','3','4','5','6','7','8','9']
#     area = ['S', 'D', 'T']
#     option = ['*', '#']

#     arr = []
#     start = 0
#     answer = []
#     cnt = 1

#     # s를 round별로 해체
#     for i in range(2, len(s)+1):
#         if i == len(s): # 마지막 round에 대한 처리
#             arr.append(s[start:])
#             break
#         if s[i] in num:
#             cnt += 1
#             arr.append(s[start:i])
#             if cnt == 3: # 10점에 대한 처리로 인해 cnt 변수 활용
#                 arr.append(s[i:])
#                 break
#             start = i
    
#     print(arr)

#     # round 별로 점수 계산
#     for i in range(3):
#         tmp = 0
#         print('%d번째 라운드' %(i+1))


#         for j in range(len(arr[i])): # 1 D / 2 S / 3 T *
#             # 숫자
#             if arr[i][j] in num:
#                 if arr[i][j] == '1' and arr[i][j+1] == '0':
#                     tmp = 10
#                 else:
#                     if tmp != 0:
#                         continue
#                     tmp = int(arr[i][j])

#             # 영역
#             elif arr[i][j] in area:
#                 if arr[i][j] == 'S':
#                     continue
#                 if arr[i][j] == 'D':
#                     tmp = pow(tmp, 2)
#                 else:
#                     tmp = pow(tmp, 3)
        
#             # 옵션
#             elif arr[i][j] in option:
#                 if arr[i][j] == '*':
#                     if i == 0:
#                         tmp *= 2
#                     else:
#                         tmp *= 2
#                         answer[i-1] *= 2
#                 else:
#                     tmp = -tmp

#         answer.append(tmp)

#         print('tmp:', tmp)
#         print('answer:', answer)
    
#     print(sum(answer))
#     return sum(answer)

# 3차 코드
'''
10이 2라운드에 나올 수 있다는 것을 간과
'''

def solution(s):
    num = ['0','1','2','3','4','5','6','7','8','9']
    area = ['S', 'D', 'T']
    option = ['*', '#']

    arr = []
    start = 0
    answer = []

    # s를 round별로 해체
    for i in range(2, len(s)+1):
        if i == len(s): # 마지막 round에 대한 처리
            arr.append(s[start:])
            break
        if s[i] in num:
            if s[i] == '0' and s[i-1] == '1': # 10에 대한 처리
                continue
            arr.append(s[start:i])
            start = i
    
    print(arr)

    # round 별로 점수 계산
    for i in range(3):
        tmp = 0
        print('%d번째 라운드' %(i+1))


        for j in range(len(arr[i])): # 1 D / 2 S / 3 T *
            # 숫자
            if arr[i][j] in num:
                if arr[i][j] == '1' and arr[i][j+1] == '0':
                    tmp = 10
                else:
                    if tmp != 0:
                        continue
                    tmp = int(arr[i][j])

            # 영역
            elif arr[i][j] in area:
                if arr[i][j] == 'S':
                    continue
                if arr[i][j] == 'D':
                    tmp = pow(tmp, 2)
                else:
                    tmp = pow(tmp, 3)
        
            # 옵션
            elif arr[i][j] in option:
                if arr[i][j] == '*':
                    if i == 0:
                        tmp *= 2
                    else:
                        tmp *= 2
                        answer[i-1] *= 2
                else:
                    tmp = -tmp

        answer.append(tmp)

        print('tmp:', tmp)
        print('answer:', answer)
    
    print(sum(answer))
    return sum(answer)
    

# s = '1S2D*3T'
# solution(s) # 37

s = '1D2S3T*'
solution(s)



# s = '1S*2T*3S'
# solution(s) # 23

# s = '1D#2S*3S'
# solution(s) # 5

# s = '1T2D3D#'
# solution(s) # -4

# s = '1D2S3T*'
# solution(s) 답이 달라
