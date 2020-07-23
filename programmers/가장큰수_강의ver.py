def solution(numbers):
    # number = [3, 30, 34, 5, 9]
    numbers = [str(x) for x in numbers] # 시간 복잡도 : N
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True) # 시간 복잡도 : NlonN
    if numbers[0] == '0':
        answer = '0' # 시간 복잡도 : 1
    else:
        answer = ''.join(numbers) # 시간 복잡도 : N
    return answer

    # 전체 시간 복잡도 = N + NlogN + 1 + N = NlogN + 2N + 1 = O(NlogN)

'''
궁금한 점
1. sort에서 key는 어떻게 쓰는 것인가
2. lambda의 활용 방법
3. 핵심 코드인 3번 line을 생각해내는 과정을 다시 한 번 보자.
'''