s, k = map(int, input().split())
# 합이 s인 k개의 양의 정수를 찾기
# k <= 20, k <= s <= 100
# output < 9223372036854775807

key = s // k

if s % k == 0:
    print(pow(key, k))
        
else:
    result = 1
    while k != 0:
        if s % k != 0:
            result *= key
            s -= key
            k -= 1
            # print(result, s, k)
        else:
            result = result * pow(s//k, k)
            k = 0
            # print(result, s, k)
    print(result)