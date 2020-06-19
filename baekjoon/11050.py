n, k = map(int, input().split())
from math import factorial as fac
print(fac(n) // (fac(k)*fac(n-k)))

""" 
# lst = [1]

# for i in range(1, n+1):
#     lst.append(lst[i-1]*i)
# print(lst)

# a = lst[n]
# b = lst[k] * lst[n-k]

# print(a//b)
이게 왜 안돼?

"""