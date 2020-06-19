S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i in alphabet:
    dic[i] = -1
for idx, i in enumerate(S):
    if dic[i] == -1:
        dic[i] = idx
for i in dic:
    print(dic[i], end=' ')