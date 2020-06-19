n = int(input())
# for i in range(1, 2*n):
#     if i <= n:
#         print(('*'*(2*n-2*i+1)).center(2*n-1))
#     else:
#         print(('*'*(2*i-2*n+1)).center(2*n-1))
# 이거 왜 안돼? ㅡㅡ

for i in range(n):
    print(' '*i, end='')
    print('*'*(2*n-(2*i+1)))
for i in range(n-1):
    print(' '*(n-2-i), end='')
    print('*'*(2*i+3))
