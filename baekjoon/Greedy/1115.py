from itertools import permutations

n = int(input())
target = [int(x) for x in input().split(' ')]

A = list(permutations(range(n), n))
Perfect = []

for i in range(len(A)):
    B = []
    B.append(0)
    for j in range(1, n):
        tmp = A[i][B[j-1]]
        if tmp in B:
            break
        else:
            B.append(tmp)
    else:
        Perfect.append(A[i])

print(Perfect)


best = 9999

for i in range(len(Perfect)):
    tmp = 0
    for j in range(n):
        if target[j] != Perfect[i][j]:
            tmp += 1
            if tmp >= best:
                break
    if best > tmp:
        best = tmp

print(best)

# 이게 왜 메모리 터지지?