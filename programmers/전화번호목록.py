# 제출 코드
'''
접두사인지 아닌지를 확인했어야 했는데 1차 코드에서는 단순히 in만 확인했다.
'''

def solution(book):
    for i in range(len(book)):
        for j in range(len(book)):
            if i == j:
                continue
            if book[i] == book[j][:len(book[i])]:
                return False
    return True

# 1차 코드
def solution(book):
    for i in range(len(book)):
        for j in range(len(book)):
            if i == j:
                continue
            if book[i] in book[j]:
                return False
    return True
