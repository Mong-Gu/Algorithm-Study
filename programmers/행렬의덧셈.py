def solution(arr1, arr2):
    if len(arr1) == 1:
        if len(arr1[0]) == 1:
            arr1[0][0] = arr1[0][0] + arr2[0][0]
        else:
            for i in range(len(arr1[0])):
                arr1[0][i] = arr1[0][i] + arr2[0][i]
    else:
        if len(arr1[0]) == 1:
            for i in range(len(arr1)):
                arr1[i][0] = arr1[i][0] + arr2[i][0]
        else:        
            for i in range(len(arr1)):
                for j in range(len(arr1[i])):
                    arr1[i][j] = arr1[i][j] + arr2[i][j]
    return arr1