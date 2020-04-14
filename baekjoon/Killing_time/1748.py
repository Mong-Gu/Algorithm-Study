# n = int(input())
# lst = [str(i) for i in range(1, n+1)]
# s = ('').join(lst)
# print(len(s))

# N이 1억까지 갈 수 있으므로 메모리 초과가 된다.
# 즉, 진짜 수를 붙여가며 생각하면 안 된다.

# n = int(input())
# lst = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
# max = 0 # 몇의 자리인지 파악하기 위한 변수

# for i in lst:
#     if n // i > 0:
#         max += 1
#     else:
#         break

# if max == 1:
#     print(n)
# else:
#     len = (n-pow(10, max-1)) * max
#     print(len)
#     max -= 1

#     while max != 1:
#         len = len + (max * ((pow(10, max)-1) - pow(10, max-1)-1))
#         max -= 1
#         print(len)

n = int(input())
lst = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]
max = 0
len = 0
for idx, val in enumerate(lst):
    if n < val:
        max += 1
        break
    else:
        max = idx + 1
        len += max*int('9'+'0'*idx)

if max == 1:
    print(n)
else:
    len = len + (n-pow(10, max-1)) * max + max
    print(len)