dy = [0, 1, 2, 4] + [0]*7
for i in range(4, 11):
    dy[i] = dy[i-1]+dy[i-2]+dy[i-3]

n = int(input())
for i in range(n):
    print(dy[int(input())])