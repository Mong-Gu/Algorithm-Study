def solution(s):
    s = s[1:-1]
    lst = []
    while True:
        start = 0
        end = 0
        for i, v in enumerate(s):
            if v == '{':
                start = i
            elif v == '}':
                end = i
                break
        lst.append(list(map(int, s[start+1:end].split(','))))
        s = s[end+2:]
        if s == '':
            break

    lst = sorted(lst, key = lambda x : len(x))
    answer = []
    for in_list in lst:
        for i in in_list:
            if i not in answer:
                answer.append(i)

    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))