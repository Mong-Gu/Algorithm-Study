import heapq
'''
heapq 관련 메서드
1. heapq.heapify(L) : 리스트 L로부터 min heap 구성
2. m = heapq.heappop(L) : min heap L에서 최소값을 삭제한 후 m에 반환. 이후 heap 형태 유지
3. heapq.heappush(L, x) : min heap L에 원소 x 삽입 후 heap 형태 유지
'''

# 강사님 풀이 전 내가 구현한 코드
def solution(arr, K):
    cnt = 0
    heapq.heapify(arr)
    while len(arr) != 1:
        if arr[0] < K:
            x = heapq.heappop(arr) + heapq.heappop(arr) * 2
            heapq.heappush(arr, x)
            cnt += 1
        else:
            break
        
    if arr[0] < K:
        return -1
    else:
        return cnt

# 강사님 코드
def solution2(arr, K):
    answer = 0
    heapq.heapify(arr)
    while True:
        min1 = heapq.heappop(arr)
        if min1 >= K:
            break
        elif len(arr) == 0:
            answer -1
            break
        min2 = heapq.heappop(arr)
        new_scoville = min1 + 2 * min2
        heapq.heappush(arr, new_scoville)
        answer += 1
        
    return answer

'''
### 강사님 코드의 시간 복잡도 ###
While True문이 해당 코드의 전체 시간 복잡도를 좌우한다.

- 최악의 경우는 elif len(arr) == 0까지 가버리게 되는 것이다.
  그때는 n-1번 반복되기 때문에 최악의 경우 반복은 O(N) 소요

- min1, min2를 pop하고 새로운 scoville을 push하는 것은 각각 logN만큼 소요
  그 세 연산은 총 3logN만큼 소요되지만 상수는 떨어버려서, O(logN) 소요

- 결론 : 최대 O(N) 만큼 반복되며 그 안에서 O(logN) 이 소요되므로
         총 시간 복잡도는 O(NlogN)
'''

'''
Heap을 이용하지 않고 리스트 등을 이용하여

최소값과 그 다음의 최소값을 pop하고 
새롭게 만든 new_scoville을 알맞은 자리에 끼워넣는 작업을 따져보면

총 시간 복잡도는 O(N^2) 이 될 것이다.

나 또한 기존에는 heapq를 몰랐고 리스트로 구현했었기 때문에 효율성 계속 탈락했다
'''
