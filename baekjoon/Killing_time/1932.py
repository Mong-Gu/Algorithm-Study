import sys
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n-1):
    for j in range(len(lst[i+1])):
        if j == 0:
            lst[i+1][j] = lst[i][j] + lst[i+1][j]
        elif j == len(lst[i+1])-1:
            lst[i+1][j] = lst[i][j-1] + lst[i+1][j]
        else:
            lst[i+1][j] = max((lst[i+1][j] + lst[i][j-1]),(lst[i+1][j] + lst[i][j]))

print(max(lst[-1]))

# 시간초과로 터져버림
# import sys
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(list(map(int, sys.stdin.readline().strip().split())))
# max = -1

# def search(size, loc, idx, sum): # size:삼각형의 크기, loc:현재층
#     global max
#     sum += lst[loc][idx]
#     if loc == size-1:
#         if  max < sum:
#             max = sum
#         else:
#             pass
#         return
#     else: # 아직 바닥까지 안 갔을 경우
#         loc += 1
#         search(size, loc, idx, sum)
#         search(size, loc, idx+1, sum)

# search(n, 0, 0, 0)
# print(max)


