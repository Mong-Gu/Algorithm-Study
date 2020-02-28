def solution(answers):
    answer = []
    List1 = [1, 2, 3, 4, 5]
    List2 = [2, 1, 2, 3, 2, 4, 2, 5]
    List3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    if len(answers) > len(List1):
        x = len(answers)//len(List1) + 1
        List1 *= x
                
    if len(answers) > len(List2):
        x = len(answers)//len(List2) + 1
        List2 *= x

    if len(answers) > len(List3):
        x = len(answers)//len(List3) + 1
        List3 *= x
    
    correct = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == List1[i]:
            correct[0] += 1
        if answers[i] == List2[i]:
            correct[1] += 1
        if answers[i] == List3[i]:
            correct[2] += 1
    
    max_value = max(correct)
    
    for i in range(3):
        if correct[i] == max_value:
            answer.append(i+1)
    
    return answer