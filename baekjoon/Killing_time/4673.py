A = set()
B = set(i for i in range(1, 10001))
for i in range(1, 10001):
    if i < 10:
        A.add(2*i)
    else:
        sum = i
        x = str(i)
        for j in range(len(x)):
            sum += int(x[j])
        A.add(sum)
X = sorted(list(B - A))
for i in X:
    print(i)