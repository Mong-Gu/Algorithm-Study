import collections

def solution(A):
    c = collections.Counter(A)
    for k, v in c.items():
        if v % 2 != 0:
            return k
