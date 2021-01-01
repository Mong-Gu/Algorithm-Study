# def solution(A):
#     min_val = 999999999
#     for p in range(1, len(A)):
#         left = sum(A[0:p])
#         right = sum(A[p:])
#         tmp = abs(left-right)
#         min_val = min(min_val, tmp)
#     return min_val
#	결과: 효율성 박살. O(N^2)

def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])
    left_sum = sum(A[0:1])
    right_sum = sum(A[1:])
    min_val = abs(left_sum - right_sum)
    for p in range(1, len(A) - 1):
        left_sum += A[p]
        right_sum -= A[p]
        tmp = abs(left_sum-right_sum)
        min_val = min(min_val, tmp)
    return min_val
