import sys
n = int(input())
target = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(input())
lst = list(map(int, sys.stdin.readline().strip().split()))

for i in lst:
    left = 0
    right = len(target) - 1
    mid = (right + left) // 2

    if i < target[left] or i > target[right]: # 리스트 안에 없을 경우
        print(0)
        continue
    
    while left <= right:
        if i < target[mid]:
            right = mid - 1
            mid = (right + left) // 2
        elif i > target[mid]:
            left = mid + 1
            mid = (right + left) // 2
        elif i == target[mid]:
            print(1)
            break
    else:
        print(0)