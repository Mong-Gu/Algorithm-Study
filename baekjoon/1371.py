""" import sys, collections

s = ''
while True:
	try:
		s += sys.stdin.readline().strip()
	except:
		break
x = collections.Counter(s).most_common()
print(x)
best = -1
result = []
for i in x:
	if i[0] == ' ':
		pass
	else:
		if i[1] >= best:
			result.append(i[0])
			best = i[1]
		else:
			break
for i in sorted(result):
	print(i, end='') """

# Counter 쓰지 말자 . . .

s = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
while True:
	try:
		s += input()
	except:
		break

best = -1
result = []
for i in alphabet:
	x = s.count(i)
	if x > best:
		result = [i]
		best = x
	elif x == best:
		result.append(i)
for i in result:
	print(i, end='')

# 다른게 문제가 아니고 sys.stdin.readline().strip()을 input()으로 바꿔버리니까 되네 뭐고...