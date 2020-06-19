# n = int(input())
# cnt = 0
# def solution(n, cnt):
#     if n == 1:
#         # print(1)
#         return cnt
#     elif n % 3 == 0:
#         # print(n//3)
#         return solution(n//3, cnt+1)
#     elif (n-1) % 3 == 0:
#         # print(n-1)
#         return solution(n-1, cnt+1)
#     elif n % 2 == 0:
#         # print(n//2)
#         return solution(n//2, cnt+1)
#     else:
#         # print(n-1)
#         return solution(n-1, cnt+1)

# print(solution(n, cnt))

# 이렇게 짜니까 32를 입력했을 경우 2의 5제곱이라 2로만 계속 나누는 게 가장 빠른데 6이 나와버리네

n = int(input())
lst = [0, 0, 1, 1] + [0 for i in range(n-3)]
idx = 4

while idx <= n:
    tmp = [1+lst[idx-1]] * 3
    if idx % 3 == 0:
        tmp[0] = 1 + lst[idx//3]
    elif idx % 2 == 0:
        tmp[1] = 1 + lst[idx//2]
    lst[idx] = min(tmp)
    idx += 1
    # print(lst)
print(lst[n])

# 와 근데 무조건 시간이 터질 줄 알았는데 시간이 어떻게 안터지네?
# 이렇게 짜도 된다는 자신감을 언제 어디서 어떻게 가져야 할지 모르겠다 정말
