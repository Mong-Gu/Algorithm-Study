def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('tmp')
    for i in range(0, len(participant)):
        if participant[i] != completion[i]:
            break
    return participant[i]