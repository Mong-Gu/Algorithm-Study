# https://potensj.tistory.com/110

from itertools import combinations

# 1차 코드
def solution(number, k):
    items = list(map(''.join, combinations(list(number), len(number)-k)))
    for i in range(len(items)):
        items[i] = int(items[i])
    return str(sorted(items)[len(items)-1])

# 2차 코드
def solution(number, k):
    best = 0
    items = list(map(''.join, combinations(number, len(number)-k)))
    
    items[0] = int(items[0])
    best = items[0]
    for i in range(1, len(items)):
        items[i] = int(items[i])
        if items[i] > best:
            best = items[i]
    return str(best)

# 3차 코드
def solution(number, k):
    items = list(map(''.join, combinations(list(number), len(number)-k)))
    return sorted(items)[len(items)-1]

# 언제했는지는 모르겠지만 헛짓거리 했던 것
def solution(number, k):
    ans = ''
    n = len(number) - k
    items = list(number)

    while n > 0:
        max_value = int(max(items))
        i = items.index(str(max_value))
        if i+n <= len(items):
            ans += items[i]
            items = items[i+1:]
            n -= 1
			
        # 최대값이 answer에 포함될 수 없는 경우
        else:
            while max_value > 0:
                max_value -= 1
                if str(max_value) not in items:
                    max_value -= 1
                    continue
                
                i = items.index(str(max_value))
                if i+n <= len(items):
                    ans += items[i]
                    items = items[i+1:]
                    n -= 1
                else:
                    continue
    return ans
'''