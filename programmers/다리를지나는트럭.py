# 제출코드
def solution(bridge_length, weight, truck_weights):
    total_time = 0
    moving = [] # 건너는 중인 트럭
    moving_time =[] # 건너는 중인 트럭의 움직인 시간
    
    while len(truck_weights) != 0 or len(moving) != 0:
        total_time += 1
        for i in range(len(moving_time)):
            moving_time[i] += 1
        
        # 다리를 건넌 트럭이 있는지 체크
        while len(moving) != 0:
            if moving_time[0] == bridge_length: # 이게 1차 코드랑 다른 점. '>'가 '=='으로 바뀌었다...
                moving.pop(0)
                moving_time.pop(0)
            else:
                break
        
        # 다리가 견딜 수 있는 무게가 된다면 트럭이 움직이자.
        if len(truck_weights) != 0 and sum(moving) + truck_weights[0] <= weight: 
            moving.append(truck_weights.pop(0)) # 건너는 중으로 상태 변환
            moving_time.append(0)

    return total_time

'''
# 1차 코드 : 문제를 이해를 잘못함; 다리를 건너는 데에 bridge_length가 걸린다는 걸 왜 저거 이상으로 가야 건넌거라고 생각했지.
def solution(bridge_length, weight, truck_weights):
    total_time = 0
    moving = [] # 건너는 중인 트럭
    moving_time =[] # 건너는 중인 트럭의 움직인 시간
    
    while len(truck_weights) != 0 or len(moving) != 0:
        total_time += 1
        for i in range(len(moving_time)):
            moving_time[i] += 1

        # 다리를 건넌 트럭이 있는지 체크
        while len(moving) != 0:
            if moving_time[0] > bridge_length:
                moving.pop(0)
                moving_time.pop(0)
            else:
                break

        # 다리가 견딜 수 있는 무게가 된다면 트럭이 움직이자.
        if len(truck_weights) != 0 and sum(moving) + truck_weights[0] <= weight: 
            moving.append(truck_weights.pop(0)) # 건너는 중으로 상태 변환
            moving_time.append(0)

    print(total_time)
    return total_time
'''