# 제출 코드
'''
13번째 줄이 18번째 줄보다 먼저 왔었어야 했는데, 그걸 고려하지 못해서 자꾸 에러가 떴었음.
'''

def solution(N, stages):
    lst = []
    stages.sort()
    
    for i in range(1,N+1):
        # stages 리스트는 비게 되었는데 더 많은 stages를 확인해야 할 때 :
        # 제한사항 중 '스테이지에 도달한 유저가 없는 경우, 해당 스테이지의 실패율 = 0'        
        if stages == []:
            lst = lst + [0 for i in range(N-len(lst))]
            break

        # stages에 i가 안 들어있을 경우, 단 한 번의 비교로 성능 향상
        elif stages[0] != i:
            lst.append(0)
            continue

        # 정상적인 경우
        boundary = 0
        for j in range(1, len(stages)):
            if stages[j] != i:
                boundary = j
                break
        
        if boundary == 0: # boundary가 끝까지 가있으면
            lst.append(1)
            stages = []
            continue
        
        lst.append(boundary/len(stages))
        stages = stages[boundary:]
    
    # 실패율이 큰 스테이지부터 리스트에 담기
    answer = []
    
    for i in range(N):
        answer.append(lst.index(max(lst)) + 1)
        lst[lst.index(max(lst))] = -1

    return answer

# 3차 코드
def solution(N, stages):

    lst = []
    stages.sort()
    
    for i in range(1,N+1):
        #print('stages:', stages)
        # stages에 i가 안 들어있을 경우
        # 단 한 번의 비교로 판단 --> 효율 향상
        if stages[0] != i:
            lst.append(0)
            continue
        
        # stages 리스트는 비게 되었는데 더 많은 stages를 확인해야 할 때
        if stages == []:
            lst = lst + [0 for i in range(N-len(lst))]
            # 제한사항 중 '스테이지에 도달한 유저가 없는 경우, 해당 스테이지의 실패율 = 0'
            
        # 정상적인 경우
        boundary = 0
        for j in range(1, len(stages)):
            if stages[j] != i:
                boundary = j
                break
        
        if boundary == 0: # boundary가 끝까지 가있으면
            lst.append(1)
            stages = []
            break
        
        lst.append(boundary/len(stages))
        stages = stages[boundary:]
    
    #print('lst:', lst)
    # 실패율이 큰 스테이지부터 리스트에 담기
    answer = []
    
    for i in range(N):
        answer.append(lst.index(max(lst)) + 1)
        lst[lst.index(max(lst))] = -1
        
    #print('answer:', answer)
        
    return answer


# 2차 코드
def solution(N, stages):

    lst = []
    stages.sort()
    
    for i in range(1,N+1):
        # stages에 i가 안 들어있을 경우
        # 단 한 번의 비교로 판단 --> 효율 향상
        if stages[0] != i:
            lst.append(0)
            continue
        
        boundary = stages.index(i+1)
        lst.append(boundary/len(stages))
        stages = stages[boundary:]
            
    answer = []
    
    for i in range(N):
        answer.append(lst.index(max(lst)) + 1)
        lst[lst.index(max(lst))] = -1
    
    return answer

# 1차 코드
def solution(N, stages):
    lst = []
    for i in range(1,N+1):
        lst.append(stages.count(i) / len(stages))
        for j in range(stages.count(i)):
            stages.remove(i)
            
    answer = []
    
    for i in range(N):
        answer.append(lst.index(max(lst)) + 1)
        lst[lst.index(max(lst))] = -1
    
    return answer