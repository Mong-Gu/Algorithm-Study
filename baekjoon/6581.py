""" End = True
result = []
while End:
    try:
        s = input().strip()
    except:
        break

    if s == '':
        continue
    
    if s == '<br>':
        result.append('\n')
        continue

    elif s == '<hr>':
        result.append('\n'+'-'*80+'\n')
        continue

    else:
        while True:
            if '<br>' in s:
                point = s.index('<br>')
                if point != 0:
                    result.append((s[:point-1]))
                result.append('\n')
                s = s[point+5:]

            elif '<hr>' in s:
                point = s.index('<hr>')
                if point != 0:
                    result.append((s[:point-1]))
                result.append('\n'+'-'*80+'\n')
                s = s[point+5:]

            else:
                result.append(s+' ')
                break

    print(result)

for i in range(len(result)):
    print(result[i], end = '') """

result = []
while True:
    try:
        result.extend(input().strip().split(' '))
    except:
        break
print(result)

for idx, val in enumerate(result):
    if val == '<br>':
        print()
    elif val == '<hr>':
        if idx > 0 and result[idx-1] == '<hr>':
            print('-'*80)
        else:
            print('\n'+'-'*80)
    else:
        if val == '':
            continue
        print(val, end = ' ')

# 이거 출력 조건을 제대로 안봤었다 미쳤나봐
# 내일 다시 하자