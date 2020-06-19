T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    x = b*2 - a # 다리가 잘린 닭의 수
    print(x, b-x)