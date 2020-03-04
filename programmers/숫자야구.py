def solution(arr):
    target = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    can = []
    
    for i in range(len(arr)):
        if arr[i][1] == 0 and arr[i][2] == 0:
            for j in range(3):
                target.remove(target.index(arr[i][j]))
            
        
        
        
    answer = 0
    return answer