# 1번 코드
# 처참히 실패. 내 로직대로 하면 딱 12까지만 잘 나오고 그 뒤로는 다 망가진다.
# 난 이 나라에서 못살겠다 바보가 된 기분이야.

def solution(n):
    # if (n // 3 == 0 and n % 3 != 0) or (n // 3 == 1 and n % 3 == 0):
    #     return # 그대로 치환

    # if (n // 3 == 1 and n % 3 != 0) or (n // 3 == 2 and n % 3 == 0):
    #     return # 1을 더한 후 치환

    # if (n // 3 == 2 and n % 3 != 0) or (n // 3 == 3 and n % 3 == 0):
    #     return # 2를 더한 후 치환

    # 규칙 확인.

    i = 0
    while True:
        if (n // 3 == i and n % 3 != 0) or (n // 3 == i+1 and n % 3 == 0):
            n += i
            break
        else:
            i += 1

    result = ''
    while n != 0:
	    n, q = divmod(n, 4)
	    result = result + str(q)
    result = list(result.replace('3', '4'))
    print(result)
    result.reverse()

    result = ''.join(result)
    print(type(result))
    return result

solution(13)