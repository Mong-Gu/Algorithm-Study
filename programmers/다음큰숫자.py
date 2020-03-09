def solution(n):
    cnt = bin(n).count('1')
    target = n+1
    while True:
        if bin(target).count('1') == cnt:
            break
        else:
            target += 1
    print(target)
    return target