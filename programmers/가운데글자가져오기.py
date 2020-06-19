def solution(s):
    if len(s) % 2 == 0:
        if len(s) == 2:
            return s
        else:
            x = len(s)//2 - 1
            return s[x:-x]
    else:
        return s[len(s)//2]
    