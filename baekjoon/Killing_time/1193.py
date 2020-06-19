n = int(input())

i = 1
left = 0
right = i
sum = 2

while not(left < n and n <= right):
    left = right
    i += 1
    right += i
    sum += 1

if sum % 2 == 0: # 분모가 1부터 시작하는 경우
    b = n - left
    a = sum - b
else: # 분모가 sum-1부터 시작하는 경우
    a = n - left
    b = sum - a

print('{}/{}'.format(a, b))