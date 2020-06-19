n = int(input()) # 단어의 개수
match = {'@':''}
num_lst = [str(i) for i in range(10)]
lst = sorted([input() for i in range(n)], key = lambda x : -len(x))
standard = len(lst[0])

for i in range(len(lst)):
    if len(lst[i]) != standard:
        lst[i] = '@'*(standard - len(lst[i])) + lst[i]

for i in range(standard):
    for j in range(len(lst)):
        if lst[j][i] != '@' and lst[j][i] not in match:
            match[lst[j][i]] = num_lst.pop()

result = []
for i in range(len(lst)):
    tmp = []
    lst[i] = lst[i].replace('@', '')
    for alphabet in lst[i]:
        tmp.append(match[alphabet])
    result.append(''.join(tmp))

sum = 0
for i in result:
    sum += int(i)
print(sum)

# 생각을 해보니 같은 인덱스에 위치한 알파벳들이라도 아무거나 pop시키면서
# 내키는대로 값을 배정해서는 안 될 것 같다.
# 예를 들어서
# A C B
# B A C
# 라는 입력값이 들어왔을 때 내 로직에 의하면
# 9 7 8
# 8 9 7 이다. (합은 1875)
# 하지만
# 8 7 9
# 9 8 7 이다. (합은 1866)
# 아 이게 아닌데, 뭐랄까 아무튼 이렇게 무작위로 배정하면 최대합이 안 될 것 같다
