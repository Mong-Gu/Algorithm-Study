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