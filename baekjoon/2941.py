s = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in lst:
    while i in s:
        # s = s[:s.index(i)] + s[s.index(i) + len(i):] # 이걸 하니까 삭제되는 알파벳 앞 뒤가 붙어버려서 하나의 알파벳처럼 인식됨
        cnt += s.count(i)
        s = s.replace(i, '0'*len(i))        
print(cnt + len(s) - s.count('0'))