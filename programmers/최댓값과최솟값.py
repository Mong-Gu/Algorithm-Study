def solution(s):
    lst = s.split(' ')
    lst = [int(i) for i in lst]
    return "{} {}".format(min(lst), max(lst))