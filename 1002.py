from math import sqrt

T = int(input())
for number in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # x1, y1 = 조규현의 위치 / r1 = 조규현과 류재명 간 거리
    # x2, y2 = 백승환의 위치 / r2 = 백승환과 류재명 간 거리
    # 원의 위치관계 파악을 해야 함. 케이스는 6가지

    distance = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)) # 규현과 승환 간의 거리
    longer,shorter = max(r1, r2), min(r1, r2)

    # print(-1) : 두 원이 완전히 일치
    if x1 == x2 and y1 == y2 and r1 == r2: print(-1)

    # print(0) : 원이 서로 밖에 있으며 만나지 않는 경우
    #            하나의 원이 다른 원의 내부에 있으며 접하지 않는 경우
    elif distance > r1+r2 or longer - shorter > distance: print(0)

    # print(1) : 원이 서로 밖에 있으며 외접하는 경우
    #            두 원이 내접하는 경우
    elif distance == r1+r2 or longer - shorter == distance: print(1)

    # print(2) : 원이 서로 밖에 있으며 서로 다른 두 점에서 만남
    elif longer - shorter < distance and distance < r1+r2: print(2)