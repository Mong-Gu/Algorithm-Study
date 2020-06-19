while True:
    n = input()
    if n == '.':
        break
    lst = []
    result = True
    for i in n:
        if i == '(' or i == '[':
            lst.append(i)
        elif i == ')':
            if len(lst) == 0 or lst[-1] != '(':
                result = False
                break
            else:
                lst.pop()
        elif i == ']':
            if len(lst) == 0 or lst[-1] != '[':
                result = False
                break
            else:
                lst.pop()

    if result and len(lst) == 0:
        print('yes')
    else:
        print('no')