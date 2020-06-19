# https://this-programmer.com/entry/%EB%B0%B1%EC%A4%802579%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0 참고

n = int(input())
lst = [0] + [int(input()) for i in range(n)]
if n == 1:
    print(lst[-1])
elif n == 2:
    print(sum(lst))
else:
    result = [0, lst[1], lst[1]+lst[2], max(lst[1]+lst[3], lst[2]+lst[3])]
    for i in range(4, n+1):
        answer = max((lst[i]+result[i-2]), (lst[i]+lst[i-1]+result[i-3]))
        result.append(answer)
    print(result[n])


# 시간 터질 줄은 알았는데 컷오프를 어떻게 시켜야할지 모르겠네
# n = int(input())
# lst = [0] + [int(input()) for i in range(n)]

# m = -1
# def dp(prev, now, score):
#     global m
#     if now == n:
#         score += lst[now]
#         if score > m:
#             m = score
#         return
#     else:
#         score += lst[now]
#         if now != 1 and now - prev == 1:
#             if now+2 <= n:
#                 dp(now, now+2, score)
#             # else : 불가능한 경우
#         else:
#             dp(now, now+1, score)
#             if now+2 <= n:
#                 dp(now, now+2, score)
#             # else : 불가능한 경우

# dp(0, 1, 0)
# dp(0, 2, 0)
# print(m)


