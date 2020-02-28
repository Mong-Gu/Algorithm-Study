# 버블 정렬 개선ver.
def solution(strings, n):
    # 미리 사전순으로 sort
    strings.sort()
    for i in range(len(strings)-1, -1, -1):
        change = False
        for j in range(0, i):
            if strings[j][n] > strings[j+1][n]:
                tmp = strings[j]
                strings[j] = strings[j+1]
                strings[j+1] = tmp
                change = True
        if change == False: break
    return strings