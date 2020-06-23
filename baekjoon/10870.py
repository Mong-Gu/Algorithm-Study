def fibo(n):
    if n <= 2:
        return [0, 1, 1][n]
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))