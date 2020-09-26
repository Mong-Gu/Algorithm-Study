pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]

def get_location(target):
    for i in range(4):
        if target in pad[i]:
            return [i, pad[i].index(target)]

def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    numbers = list(map(str, numbers))

    for num in numbers:
        if num in ['1', '4', '7']:
            answer += 'L'
            left = num
        elif num in ['3', '6', '9']:
            answer += 'R'
            right = num
        else:
            num_loc = get_location(num)
            l_loc = get_location(left)
            r_loc = get_location(right)
            dist_with_l = abs(num_loc[0] - l_loc[0]) + abs(num_loc[1] - l_loc[1])
            dist_with_r = abs(num_loc[0] - r_loc[0]) + abs(num_loc[1] - r_loc[1])
            if dist_with_l < dist_with_r:
                answer += "L"
                left = num
            elif dist_with_l > dist_with_r:
                answer += "R"
                right = num
            else:
                if hand == "left":
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
    return answer