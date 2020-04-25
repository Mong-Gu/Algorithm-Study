n = int(input())
dic = {}
for i in range(n):
    age, name = input().split()
    age = int(age)
    dic[age] = dic.get(age, []) + [name]
for age, nameList in sorted(dic.items()):
    for name in nameList:
        print(age, name)