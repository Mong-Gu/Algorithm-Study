def solution(s):
    if (len(s) == 4 or len(s) == 6):
        for i in range(len(s)):
            if s[i] not in ['1','2','3','4','5','6','7','8','9','0']:
                return False
        return True
    else:
        return False