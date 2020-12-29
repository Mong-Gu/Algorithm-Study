import sys

def makeTable(pattern):
	size = len(pattern)
	table = [0 for i in range(size)]
	j = 0
	for i in range(1, size):
		while j > 0 and pattern[i] != pattern[j]:
			j = table[j - 1]
		if pattern[i] == pattern[j]:
			j += 1
			table[i] = j
	return table

n = int(input())
string_len = int(input())
string = sys.stdin.readline().strip()
cnt = 0

pattern = 'I' + 'OI'* n
pattern_len = len(pattern)
table = makeTable(pattern)
j = 0
for i in range(string_len):
	while j > 0 and string[i] != pattern[j]:
		j = table[j - 1]
	if string[i] == pattern[j]:
		if j == pattern_len - 1:
			# print("index {}에서 발견".format(i - pattern_len + 2))
			cnt += 1
			j = table[j]
		else:
			j += 1
print(cnt)



# for i in range(0, m - pattern_len + 1):
# 	if pattern == s[i : i + pattern_len]:
# 		cnt += 1
# print(cnt)
