def solution(x):
    s = str(x)
    a = sum([int(i) for i in s])
    return not(x % a)

