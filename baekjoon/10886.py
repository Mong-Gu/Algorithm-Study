n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print('Junhee is not cute!' if sum < n//2+1 else 'Junhee is cute!')