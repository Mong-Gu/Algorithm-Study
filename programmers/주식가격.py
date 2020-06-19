def solution(prices):
    answer = []
    for i in range(len(prices)):
        if i == len(prices): # 마지막 원소에 대한 처리
            answer.append(0)
            break
        
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1 # 1초 뒤에 바로 떨어져도 1초간 가격이 떨어지지 않은 것으로 봄
                break
        answer.append(cnt)
        
    return answer