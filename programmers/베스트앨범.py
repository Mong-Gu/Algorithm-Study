def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = {'total': 0}
            
        dic[genres[i]]['total'] += plays[i]
        dic[genres[i]][i] = plays[i]

    print('dic:', dic)

    total_lst = []
    for key in dic.keys():
        total_lst.append([key, dic[key]['total']])
    
    total_lst.sort(key = lambda index : index[1], reverse = True)
    print(total_lst)

    result = []
    for i in range(len(list(dic.keys()))):
        first = 0
        first_idx = 0
        second = 0
        second_idx = 0
        for index, count in dic[total_lst[0][0]].items():
            if index == 'total':
                continue
            print(index, count)
            if count > first :
                if first > second :
                    second = first
                    second_idx = first_idx
                first = count
                first_idx = index

        result.append(first_idx)
        result.append(second_idx)
        total_lst.pop(0)
        print(total_lst)
        print('result:', result)
        
    return result
                





    print(dic)
    print(total_lst)

solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])
