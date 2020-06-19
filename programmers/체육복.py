def solution(n, lost, reserve):
    # case 1 : No lost
    answer = n - len(lost)

    # case 2 : lost
    for i in lost:
        if i in reserve:
            answer = answer + 1
            reserve.remove(i)
            continue
        for j in reserve:
            if j == i-1:
                answer = answer + 1
                reserve.remove(j)
                break
            elif j == i+1:
                if j in lost:
                    break
                answer = answer + 1
                reserve.remove(j)
                break

    return answer