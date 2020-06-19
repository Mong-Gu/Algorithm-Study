a, b = map(int, input().split())

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b, x):
    return a * b // x

x = gcd(a, b)
y = lcm(a, b, x)

print(x)
print(y)