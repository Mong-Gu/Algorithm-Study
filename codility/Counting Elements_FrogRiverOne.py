# def solution(X, A):
#     s = {i for i in range(1, X+1)}
#     for i, v in enumerate(A):
#         s = s.difference({v})
#         if len(s) == 0:
#             return i
#     return -1
# 		# O(N ** 2)

def solution(X, A):
    s = {i for i in range(1, X+1)}
    dic = {i:1 for i in range(1, X+1)}
    for i, v in enumerate(A):
        if dic[v]:
            s.remove(v)
            dic[v] = 0
        if len(s) == 0:
            return i
    return -1
		# O(N)
