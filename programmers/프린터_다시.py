def solution(priorities, location):
    elem_order = [i for i in range(len(priorities))]
    print_order = []
    print_priorities = []
    while priorities:
        if priorities[0] == max(priorities):
            print_priorities.append(priorities.pop(0))
            print_order.append(elem_order.pop(0))
        else:
            priorities.append(priorities.pop(0))
            elem_order.append(elem_order.pop(0))
    return(print_order.index(location) + 1)

print(solution([2, 1, 3, 2], 2))