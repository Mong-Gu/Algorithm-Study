def solution(skill, skill_trees):
    count = 0
    for i in range(len(skill_trees)):
        status = 0
        check = True
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                if skill.index(skill_trees[i][j]) != status:
                    check = False
                    break
                else:
                    status += 1
        if check == True:
            count += 1
    return count