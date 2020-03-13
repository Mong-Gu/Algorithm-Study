from itertools import permutations
def solution(arr):
    num = [i for i in range(1, 10)]
    AllCase = list(permutations(num, 3))
    Possible = AllCase[:]
    print(Possible)

    for i in range(len(arr)):
        arr[i][0] = str(arr[i][0])

    for i in range(len(arr)):
        for num in AllCase:
            S = 0
            B = 0
            for j in range(3):
                if int(arr[i][0][j]) == num[j]:
                    S += 1
                elif int(arr[i][0][j]) != num[j] and int(arr[i][0][j]) in num:
                    B += 1
            if not(S == arr[i][1] and B == arr[i][2]) and num in Possible:
                Possible.remove(num)
    
    return len(Possible)