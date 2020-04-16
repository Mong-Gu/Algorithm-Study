from collections import Counter

n, k = map(int, input().split())
if k < 5: # 최소 a n t i c 는 알려줘야 함
    print(0)
else:
    words = [list(set(','.join(input()).split(','))) for i in range(n)]

    for i in range(len(words)):
        words[i].remove('a')
        words[i].remove('n')
        words[i].remove('t')
        words[i].remove('i')
        words[i].remove('c')
    k -= 5

    words.sort(key = lambda x : len(x))

    result = 0
    for i in range(len(words)):
        if len(words[i]) >= 1:
            words = words[i:]
            result += i
            break

    while k != 0:
        tmp_lst = Counter([i[0] for i in words if len(i) == 1]).most_common()
        target = tmp_lst[0][0]
        for i in range(len(words)):
            if target in words[i]:
                words[i].remove(target)
        words.sort(key = lambda x : len(x))
        for i in range(len(words)):
            if len(words[i]) >= 1:
                words = words[i:]
                result += i
                break
        k -= 1
    
    print(result)

# 이것도 런타임에러 뜨네...
# 코드가 드럽긴 한데 런타임에러가 왜 자꾸 뜨는거지