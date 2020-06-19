s = input()
statement = [s[0]]
for i in range(1, len(s)):
    if s[i] != statement[-1]:
        statement.append(s[i])
cnt_0 = statement.count('0')
if cnt_0 >= len(statement) - cnt_0:
    print(len(statement) - cnt_0)
else:
    print(cnt_0)