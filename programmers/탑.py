def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):
        check = False
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                check = True
                break
        if check == False:
            answer.append(0)
            
    answer.reverse()
    return answer