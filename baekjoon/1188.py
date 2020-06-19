""" from fractions import Fraction
n, m = map(int, input().split())
size = Fraction(n, m)
cnt = 0
lst = [1 for i in range(n)]
spare = []

# print(lst)
while lst:
    lst.append(lst.pop()-size) # 한 번 자르고, 평론가에게 하나 부여
    cnt += 1
    # print(lst)
    while lst:
        if lst[-1] == size:
            lst.pop()
            # print(lst)
        elif lst[-1] > size:
            lst.append(lst.pop()-size)
            cnt += 1
            # print(lst)
        else: # lst[-1] < size
            spare.append(lst.pop())
            # print(lst)
            # print(spare)
            break

idx = 0
sum = 0
additional = True
for i, val in enumerate(spare):
    sum += val
    if sum < size:
        continue
    elif sum == size:
        additional = False
        break
    else: # sum > size
        idx = i
        break

if additional:
    x = idx*2+1
    cnt += len(spare) // x

print(cnt) """

# 다른 분 코드 보니까 현타와서 못하겠다
# https://pacific-ocean.tistory.com/243