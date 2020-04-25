# A = 고정비용
# B = 가변 비용
# C = 판매 가격
# C*N > A+B*N 이 되는게 Break-even point

a, b, c = map(int, input().split())
n = 0

# 손익분기점이 존재하지 않는 경우는?
# -> 가변비용이 판매가격보다 클 경우
if b >= c:
    print(-1)
# else:
#     while c*n <= a+b*n:
#         n += 1
#     print(n)

# 위 else문에서는 시간 초과가 뜨는데 while문이 너무나도 많이 돌 경우 그렇게 될 것 같다.
# 예를 들어 b = 100, c = 101이고 a가 아주 크다면 while문이 매우 많이 돌 것이야.
# 그래서 반복보다는 그냥 한 번에 수식을 짜는 것이 맞다고 생각됨.
# 효율성을 증진시킬 수 있는 방법은?
else:
    n = a / (c-b)
    print(int(n)+1)