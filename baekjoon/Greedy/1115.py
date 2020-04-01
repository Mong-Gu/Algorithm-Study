from itertools import permutations

n = int(input())
P = [int(x) for x in input().split(' ')]

A = list(permutations(range(n), n)) # 순열들을 모아둔 리스트
B = [] # A의 각 원소에 위치한 순열들을 돌며 자식 순열을 만들어보기 위함
Perfect = [] # 그중 완벽한 순열인 것들만 모아둔 리스트

# print(A)

for i in range(len(A)):
    B = [0]
    for j in range(1, n):
        x = A[i][B[j-1]]
        if x in B:
            break
        else:
            B.append(x)
    else:
        Perfect.append(list(A[i]))
        Perfect.append(B)

print (Perfect)
# 중복되는 값들을 제거해야 하는데 리스트로 담았다 보니까 set이 안먹힘


# best = 9999

# for i in range(len(Perfect)):
#     tmp = 0
#     for j in range(n):
#         if target[j] != Perfect[i][j]:
#             tmp += 1
#             if tmp >= best:
#                 break
#     if best > tmp:
#         best = tmp

# print(best)

# # 이게 왜 메모리 터지지?

