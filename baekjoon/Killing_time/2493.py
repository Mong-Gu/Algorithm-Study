n = int(input()) # 탑의 개수
lst = list(map(int, input().split())) # 탑의 높이
result = []

for i in range(len(lst)-1, -1, -1):
    for j in range(i-1, -1, -1):
        if lst[i] < lst[j]:
            result.append(j+1)
            break
    else:
        result.append(0)

result.reverse()
for i in result:
    print(i, end=' ')