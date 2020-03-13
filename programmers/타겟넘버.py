def solution(numbers, target):
    answer = [0]
    for i in numbers:
        tmp_lst = []
        for j in answer:
            tmp_lst.append(j+i)
            tmp_lst.append(j-i)
        answer = tmp_lst
    return answer

# 나중에 꼭 다시 짜보기