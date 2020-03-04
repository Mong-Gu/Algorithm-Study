# 방법 1 : n이 충분히 작을 때
def solution1(n, lost, reserve):
    u = [1] * (n + 2)
    # 학생 수 + 2 칸을 만듦으로써 양 옆을 1로 막아둠. 그러면 로직이 편리해짐

    for i in reserve: # 시간 복잡도 : O(N)
        u[i] += 1
    for i in lost: # 시간 복잡도 : O(N)
        u[i] -= 1
    for i in range(1, n+1): # 시간 복잡도 : O(N)
        if u[i-1] == 0 and u[i] == 2:
            u[i-1 : i+1] = [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i : i+2] = [1,1]
    return len([x for x in u[1:-1] if x > 0]) # 시간 복잡도 : O(N)
    # -> 양 옆에 임의로 확장시켜 놓은 한 칸씩은 제외

    # 전체 시간 복잡도 : O(N)

# 방법 2 : n이 아주 클 때
def solution2(n, lost, reserve):
    s = set(lost) & set(reserve) 
    # 집합에서 &는 교집합을 의미.
    # 체육복을 잃어버렸지만 여분이 있어 빌릴 필요가 없는 학생들
    l = set(lost) - s 
    # 집합에서 - 는 차집합을 의미. 
    # 체육복을 잃어버렸는데 여분이 없어 빌려야만 하는 학생들
    r = set(reserve) - s
    # 여벌은 가져왔는데 도난은 당하지 않아서 빌려줄 수 있는 학생들

    # r을 오름차순으로 정렬했기 때문에 
    # for문 안에서는 나보다 번호가 하나 작은 학생부터 먼저 살펴봐야 탐욕법이 먹힌다
    for x in sorted(r): 
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)

    '''
    전체 시간 복잡도 :
    (1) set을 만드는 데에는 리스트 lost나 reserve 안의 요소 개수에 비례.
        -> 최악의 경우 O(N)
    (2) r의 크기, 즉 체육복을 빌려줄 수 있는 학생 수가 k일 때,
        r을 정렬하는 데에는 O(klogk) 소요

        그 안의 if-elif 구문은 결국 klogk에 비례.
    
    n이 매우 큰데, 여벌의 체육복을 가져온 학생 수 k가 아주 작을 경우 방법2가 훨씬 효율적.
     
    '''

