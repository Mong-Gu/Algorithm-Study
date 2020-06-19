def solution(n, arr1, arr2):
    for i in range(n):
        arr1[i] = (bin(arr1[i])[2:])
        arr2[i] = (bin(arr2[i])[2:])
        if len(arr1[i]) != n:
            arr1[i] = '0'*(n-len(arr1[i])) + arr1[i]
        if len(arr2[i]) != n:
            arr2[i] = '0'*(n-len(arr2[i])) + arr2[i]

    answer = ['' for i in range(n)]

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                answer[i] += '#'
            elif arr1[i][j] == '0' and arr2[i][j] == '0':
                answer[i] += ' '

    return answer