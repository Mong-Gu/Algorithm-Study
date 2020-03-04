def solution(n):
    if n == 1 or n == 2:
        return n
    
    answer = 1 # 타일을 모두 세로로 배치한 경우는 미리 포함
    a, b = n, 0 # a = 타일을 세로로 배치한 개수, b = 타일을 가로로 배치한 개수
    
    while not(a <= 1):
        a = a - 2
        b = b + 1
        answer = answer + (a * b + 1)

    return answer % 1000000007

print(solution(4))