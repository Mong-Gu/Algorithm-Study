def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = {'total': 0}
            
        dic[genres[i]]['total'] += plays[i]
        dic[genres[i]][i] = plays[i]
    print(dic)

    
    
    answer = []
    return answer