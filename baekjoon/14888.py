n = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
# idx 0:덧셈, 1:뺄셈, 3:곱셈, 4:나눗셈

def MAX(lst, add, sub, mul, div):
    M = lst[0]
    idx = 1
    while sub > 0:
        M = M - lst[idx]
        idx += 1
        sub -= 1
    while div > 0:
        M = M // lst[idx]
        idx += 1
        div -= 1
    while add > 0:
        M = M + lst[idx]
        idx += 1
        add -= 1
    while mul > 0:
        M = M * lst[idx]
        idx += 1
        mul -= 1
    return M

def MIN(lst, add, sub, mul, div):
    m = lst[0]
    idx = 1
    while add > 0:
        m = m + lst[idx]
        idx += 1
        add -= 1
    while div > 0:
        m = m // lst[idx]
        idx += 1
        div -= 1
    while sub > 0:
        m = m - lst[idx]
        idx += 1
        sub -= 1
    while mul > 0:
        m = m * lst[idx]
        idx += 1
        mul -= 1
    return m

print(MAX(lst, add, sub, mul, div))
print(MIN(lst, add, sub, mul, div))