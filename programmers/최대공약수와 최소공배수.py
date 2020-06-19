def gcd(a, b):
    while a*b != 0:
        if a > b: a = a % b
        else: b = b % a
    return a + b
            
def solution(n, m):
    a = gcd(n, m)
    
    if a == 1:
        return ([a, n*m])
    
    else:
        lst = [a]
        x = a
        
        while n != 1 or m != 1:
            n, m = n//x, m//x
            x = gcd(n,m)
            
            if x == 1: break
            else: lst.append(x)
                
        b = n * m
        for i in lst: 
            b = b * i
        
    return([a, b])