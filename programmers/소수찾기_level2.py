from itertools import permutations
def solution(numbers):
    answer = 0

    # 가능한 수의 조합 만들기
    possible = []

    for i in range(len(numbers)):
        possible.extend(list(permutations(numbers, i+1)))

    possible = [''.join(i) for i in possible]
    possible = sorted(list(set(map(int, possible))))

    idx = -1
    for i in range(len(possible)):
        if possible[i] <= 1: idx = i
        else: break
            
    if idx == -1: pass
    else: possible = possible[idx+1:]

    # 소수 찾아내기
    for num in possible:
        for i in range(2, round(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            answer += 1

    return answer

'''
궁금한 점!
26번 줄에서 for문의 범위를 round(num ** 0.5) + 1 이 아닌 
round(num ** 0.5) + 2 까지로 하면 다수의 테스트케이스가 실패하게 된다.
하지만 한 번 더 반복문을 돌린다고 하면 효율성이 안 좋아질 뿐 
테스트케이스가 실패할 일은 없어야 되는 것 아닌가?
'''
