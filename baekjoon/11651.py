# n = int(input())
# lst = sorted([input().split() for i in range(n)], key = lambda x: (x[1], x[0]))
# for i in lst:
#     print(i[0], i[1])

# 나는 당연히 아스키코드로도 대소비교가 가능하니 일부러 int로 캐스팅을 안했었는데
# '11'과 '5'를 비교하면 '1'과 '5' 중에 '5'가 더 커서 '5'가 더 크다고 판명난다... 문자열 간의 대소 비교는 먼저 나오는 글자를 비교한다는 것을 또 까먹었다! 아휴

n = int(input())
lst = sorted([list(map(int, input().split())) for i in range(n)], key = lambda x: (x[1], x[0]))
for i in lst:
    print(i[0], i[1])