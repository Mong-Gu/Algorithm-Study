n = int(input())

end = 1
cnt = 0
total = 0

for start in range(1, n+1):
	while total < n and end <= n:
		total += end
		end += 1
	if total == n:
		cnt += 1
	total -= start
print(cnt)

