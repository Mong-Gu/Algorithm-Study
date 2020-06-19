def solution(record):
    arr = [] 
    result = []
    dic ={}

    # record의 각 원소를 공백 기준으로 잘라서 그 조각들을 arr의 각 원소로 append
    for i in range(len(record)): 
        arr.append(record[i].split(' '))

    # 딕셔너리 내부의 닉네임을 최종 상태까지 변경
    for i in range(len(arr)):
        # Enter
        if arr[i][0] == 'Enter':
            if arr[i][1] not in dic:
                dic[arr[i][1]] = arr[i][2]
            else:
                if dic[arr[i][1]] != arr[i][2]:
                    dic[arr[i][1]] = arr[i][2]
        # Change
        elif arr[i][0] == 'Change':
            dic[arr[i][1]] = arr[i][2]
        # Leave는 무시
    
    # 닉네임의 최종 상태까지 반영된 딕셔너리 기준으로 출력하고 그 값을 result에 append
    for i in range(len(arr)):
        if arr[i][0] == 'Enter':
            result.append("{}님이 들어왔습니다.".format(dic[arr[i][1]]))
        elif arr[i][0] == 'Leave':
            result.append("{}님이 나갔습니다.".format(dic[arr[i][1]]))
        # Change는 무시

    return result