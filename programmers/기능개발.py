def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        if progresses[0] < 100: # 첫 번째 기능이 진행률 100% 미만일 때
            for i in range(len(progresses)): # 각 기능의 진행률에 sppeds를 더해줌
                if progresses[i] < 100: # 다만, 이미 100%인 기능들은 더해주지 않고
                    progresses[i] = progresses[i] + speeds[i]
                    if progresses[i] > 100: # 더한 후 100%가 초과된 기능들은 100%로 맞춰줌
                        progresses[i] = 100

        else: # 첫 번째 기능이 진행률 100%가 되었다면
            cnt = 0
            while len(progresses) != 0 and progresses[0] == 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1

            answer.append(cnt)
    return answer