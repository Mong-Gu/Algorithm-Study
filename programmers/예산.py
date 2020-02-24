def solution(d, budget):
    d = sorted(d)
    
    best = 0 # 지원 가능한 부서 개수 중 최대 개수
    cnt = 0 # 지원 가능한 부서 개수
    tmp_budget = budget # 비교를 위해 budget을 할당
    
    for i in range(len(d)):
        for j in range(i, len(d)):
            tmp_budget -= d[j]
            cnt += 1
            
            if tmp_budget == 0:
                if cnt > best:
                    best = cnt
                    cnt = 0
                    tmp_budget = budget
                break
                
            elif tmp_budget < 0:
                cnt -= 1 # 예산이 초과했으므로 마지막 count한 부서는 빼줘야 함
                if cnt > best:
                    best = cnt
                    cnt = 0
                    tmp_budget = budget
                break
                
            else: # 모든 부서를 다 돌았는데도 예산이 남았을 경우
                if j == len(d)-1:
                    return len(d)
    
    return best
