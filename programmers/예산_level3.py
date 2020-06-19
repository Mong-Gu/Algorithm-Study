def solution(budgets, M):
    answer = 0
    total_demand = sum(budgets) # O(N)

    if total_demand <= M:
        return max(budgets)
    
    tmp_demand = 0
    limit = 0
    start = 0
    end = len(budgets) - 1
    mid = (start+end) // 2

    while start <= end:
        tmp_demand = sum(budgets[:mid]) # mid 전까지 포함
        limit = (total_demand - tmp_demand) // len(budgets[mid:])

            



        


# solution([120, 110, 140, 150], 485)