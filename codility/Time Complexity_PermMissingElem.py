def solution(A):
    s = set(i for i in range(1, len(A)+2))
    for i in A:
        s.remove(i)
    return(list(s)[0])
