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