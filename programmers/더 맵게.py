# 이 코드들은 기록으로만 남기고 버리기로 한다. 강의 ver을 보기!!!!!!!

'''
# 3차 코드 : cnt의 위치를 바꿨음. 테스트케이스 모두 통과, 효율성테스트는 다시 또 다 실패.
#            질문하기를 눌러봤더니 다 heapq 모듈을 이용. 제엔장... 모듈 없이는 힘들듯.ㅠㅠ

def solution(arr, K):
    if min(arr) >= K or K == 0: return 0 # 섞을 필요도 없을 경우
    if len(arr) == 1: return -1 # 제한 사항 4번

    cnt = 0 # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 count
    arr.sort()
    
    while True:
        if arr[0] >= K: return cnt
        if len(arr) == 1: return -1
        
        x = ((arr.pop(0) + (arr.pop(0) * 2)))
        cnt += 1
        
        if len(arr) == 0:
            arr.append(x)
            continue
            
        elif len(arr) == 1:
            if arr[0] < x :
                arr.append(x)
                continue
            else:
                arr.insert(0, x)
                continue
                
        else: # len(arr) >= 2
            for i in range(len(arr)):
                if i != len(arr) -1:
                    if arr[i] >= x :
                        arr.insert(i, x)
                        break
                else: # 마지막 원소일 경우
                    if arr[i] >= x: 
                        arr.insert(i, x)
                    else:
                        arr.append(x)
'''

'''
# 2차 코드 : 갑자기 테스트 케이스 계속 몇 개 실패
def solution(arr, K):
    if min(arr) >= K or K == 0: return 0 # 섞을 필요도 없을 경우
    if len(arr) == 1: return -1 # 제한 사항 4번

    cnt = 0 # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 count
    arr.sort()
    
    while True:
        if arr[0] >= K: return cnt
        if len(arr) == 1: return -1
        
        x = ((arr.pop(0) + (arr.pop(0) * 2)))
        
        if len(arr) == 0:
            arr.append(x)
            continue
            
        elif len(arr) == 1:
            if arr[0] < x :
                arr.append(x)
                continue
            else:
                arr.insert(0, x)
                continue
                
        else: # len(arr) >= 2
            for i in range(len(arr)):
                if i != len(arr) -1:
                    if arr[i] > x :
                        arr.insert(i, x)
                        break
                    elif arr[i] <= x and arr[i+1] >= x:
                        arr.insert(i+1, x)
                        break
                else: # 마지막 원소일 경우
                    if arr[i] < x:
                        arr.append(x)
                    else:
                        arr.insert(i, x)
                
        cnt += 1
'''

'''
# 1차 코드 : 테스트케이스는 모두 통과. 효율성 테스트는 모두 시간초과.
def solution(arr, K):
    if min(arr) >= K:
        return 0

    cnt = 0
    while True:
        if min(arr) >= K:
            return cnt

        arr.sort()
        arr.insert(0, (arr.pop(0) + (arr.pop(0) * 2)))
        cnt += 1
'''    


solution([1, 2, 3, 9, 10, 12], 7)