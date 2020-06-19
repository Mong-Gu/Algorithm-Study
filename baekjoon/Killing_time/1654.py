import sys

k, n = map(int, input().split())
# k = 가지고 있는 랜선의 개수
# k개의 랜선은 각각 다른 길이를 가지고 있음
# n = 필요한 랜선의 개수
# k <= n
lst = sorted([int(sys.stdin.readline().strip()) for i in range(k)], reverse = True)
left = 1
right = max(lst)
res = 0

while left <= right:
    mid = (left+right) // 2
    cnt = 0

    for i in lst:
        if i // mid >= 1:
            cnt += (i // mid)
        else:
            break

    if cnt < n:
        right = mid-1
    else:
        res = mid
        left = mid+1

print(res)