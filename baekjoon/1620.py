import sys
n, m = map(int, input().split())
lst = [sys.stdin.readline().strip() for i in range(n)] # 포켓몬 이름

for i in range(m):
	x = sys.stdin.readline().strip()
	try: # 번호가 문제로 주어진다면
		x = int(x)
		sys.stdout.write(str(lst[x-1])+'\n')
	except:
		sys.stdout.write(str(lst.index(x)+1)+'\n')