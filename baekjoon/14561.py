# 이거 왜 성공 안되는거지? 테스트케이스는 다 통과하는데?

def convert(n, base):
    T = '0123456789ABCDE'
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        n, base = map(int, input().split())
        target = convert(n, base)

        # 방법 1
        if target == target[::-1]:
            print(1)
        else:
            print(0)

        # 방법 2
        # L = len(target)
        # mid = L // 2
        # for j in range(mid):
        #     if target[j] != target[L-1-j]:
        #         print(0)
        #         break
        # else:
        #     print(1)