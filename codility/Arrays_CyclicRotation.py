import collections

def solution(A, K):
    d = collections.deque(A)
    d.rotate(K)
    return list(d)
