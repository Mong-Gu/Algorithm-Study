
# 소스코드 짜는 강의 보기 전 내가 짠 것
def MySolution(number, k):
    lst = []
    cnt = k
    
    lst.append(number[0])
    for i in range(1, len(number)):
        if cnt == 0:
            break
        elif int(lst[-1]) > int(number[i]) :
            lst.append(number[i])
        else:
            while len(lst) != 0 and not(int(number[i]) <= int(lst[-1])) and cnt != 0:
                lst.pop()
                cnt -= 1
            lst.append(number[i])

    if cnt == 0 and i != len(number)-1:
        return ''.join(lst) + number[i:]
    
    else:
        while cnt != 0:
            lst.pop()
            cnt -= 1
    
    return ''.join(lst)

# 강사님의 코드
def TeachersSolution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer

'''
33번~35번 line에 while문이 하나 더 있어서 32번~39번 for문은 O(N^2)라고 생각할 수 있는데
number라는 문자열에서 num이 빠져나오며 collected에 추가되는 게 1번,
그리고 추가되었다가 도로 빠져나와야 된다고 하더라도 기껏해야 1번만 나오면 된다.
그래서 1번 들어갔다가 1번 나오는 게 최악의 경우인데 결국 최악의 경우는 2N이다. -> O(N)

가장 핵심적인 32번~39번 line의 시간 복잡도가 O(N)이므로 해당 함수의 시간 복잡도는 O(N)이다.
'''
