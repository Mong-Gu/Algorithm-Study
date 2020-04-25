while True:
    n = input()
    if n == '0':
        break
    if len(n) == 1:
        print('yes')
    else:
        for i in range(len(n)//2):
            if n[i] != n[-(i+1)]:
                print('no')
                break
        else:
            print('yes')