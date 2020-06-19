from itertools import combinations
from collections import Counter
# 20.03.04 계속 하는 중 ,,,

def solution(clothes):
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = 0
        dic[clothes[i][1]] += 1

    items = list(Counter(dic).elements())
    print(items)

    for i in range(1, len(items)+1):
        tmp = list(combinations(items,i))
        print(tmp)

    return

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])



'''
def multi(arr):
    result = 1
    for i in range(len(arr)):
        result *= arr[i]
    return result

def solution(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i][1] not in dic:
            dic[arr[i][1]] = 1
        else:
            dic[arr[i][1]] += 1
    s = [i for i in dic.values()]
    print(s)
    
    if len(s) == 1:
        return s[0]
    else:
        return (sum(s) + multi(s))
#    return answer

arr = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
solution(arr)

# 이건 아니야 ,, 어려운디?
'''