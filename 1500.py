s, k = map(int, input().split())

key = s // k

if s % k == 0:
    print(pow(key, k))
        
else:
    result = 1
    while k != 0:
        # print()
        if s % k != 0:
            result *= key
            s -= key
            k -= 1
            # print('result: %3d, s: %3d, k: %3d' % (result, s, k))
            # print('조합에 들어가는 수:', key)
        else:
            # x = s//k
            # K = k
            result = result * pow(s//k, k)
            k = 0
            # s = 0
            # print('result: %3d, s: %3d, k: %3d' % (result, s, k))
            # print('조합에 들어가는 수: %d, 그 개수: %d' % (x, K))
    
    print(result)