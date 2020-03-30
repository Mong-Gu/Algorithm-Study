""" 
망했음
import sys, collections

c = collections.Counter()
while True:
	try:
		tmp = collections.Counter(sys.stdin.readline().strip())
		c += tmp
	except:
		break

x = c.most_common()
best = -1
lst = []
for tpl in x:
	print(tpl)
	if tpl[0] == ' ':
		continue
	else:
		if best <= tpl[1]:
			lst.append(tpl[0])
			best = tpl[1]
		else:
			break

for i in sorted(lst):
	print(i, end ='') """