def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1 # 시간 복잡도 : get + 더하기 -> 2n
    for x in completion:
        d[x] -= 1 # 시간 복잡도 : 빼기 -> n
    dnf = [k for k, v in d.items() if v > 0] # 시간 복잡도 : 비교문 + append -> 2n
    answer = [dnf[0]] # 시간 복잡도는 1이지만, 사실 없어도 되는 한 줄
    return answer

    # 전체 시간 복잡도 : 2n + n + 2n + 1 = 5n + 1 = O(N))

'''
내가 풀었던 방식은 list에서 sort한 후 비교 연산을 통해 다른 원소를 return하는 것이었다.
다만, list에서 sort는 O(NlogN)이라는 시간복잡도를 가지고 있기 때문에 더 효율적으로 짜려면 dictionary를 이용하는 것이 좋다.
'''
