# 일단 보류

# 1차 코드
# 다른 사람들이 제시해준 테스트 케이스를 보니 부족할 때만 공급받을 게 아니다.
# 부족할 때만 공급받았다가 날짜 k일차에 도달하기 전에 고갈날 수도 있음

# 그렇다면 어떻게 해야 할까?
# '(지금 재고) + (추후 받을 수 있는 총 공급량) >= k' 가 아니라면 공급 받아야 한다
# 그렇다면 지금 당장은 공급을 받지 않아도 되는 와중에 위 줄에 걸려서 공급을 받아야 한다면
# 아무때나 공급을 받아야 하는가? 가장 공급량이 많을 때만 딱 받으면 되는 게 아닐까?

def solution(stock, dates, supplies, k):
    '''
    1. 하루에 밀가루 1톤씩 사용.
    2. 밀가루가 떨어지지 않고 공장을 운영하기 위해서 
       최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 return
       
    - stock : 현재 공장에 남아있는 밀가루 수량
    - dates : 밀가루 공급 일정 
              -> dates[i]에는 공급 가능한 i번째 날. i일 후라고 생각하면 편할듯.
    - supplies : 해당 시점에 공급 가능한 밀가루 수량 
                 -> supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량
    - k : 원래 공장으로부터 공급받을 수 있는 시점
    '''
    
    '''
    생각한 조건:
    1. 'k - 현재 일차 <= 당일날 1톤 소모 전 재고' 라면 더이상 공급받지 않아도 된다
    2. '다음 공급일' - '현재 일차' <= 현재 일차 공급받기 전 재고 라면 이번 공급받는 건 패스
    '''
    answer = 0
    today = 0
    i = 0
    while True:
        if k - today <= stock:
            break
            
        # 다음 공급받을 날짜의 작업 시작 전 시점까지 jump
        stock -= (dates[i] - today)
        today += (dates[i] - today)
        
        if i == len(dates)-1 :
            if k - today <= stock:
                break
            else:
                stock += supplies[i]
                answer += 1
                break
            
        # 다음 공급받을 날짜까지 여유가 있다면 공급받지 않음        
        if dates[i+1] - today <= stock:
            pass
        # 여유가 없다면 공급을 받음
        else:
            stock += supplies[i]
            answer += 1
        i += 1
        
    return answer