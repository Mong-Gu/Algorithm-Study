""" 
1차 제출코드
n = int(input())
lst = sorted([int(input()) for i in range(n)])

dic = {}
i = 0
while i < len(lst):
    dic[lst[i]] = lst.count(lst[i])
    i += dic[lst[i]]
best = -1
for v in dic.values():
    if v > best:
        best = v

target = []
for k, v in dic.items():
    if v == best:
        target.append(k)

print('%.0f'% (sum(lst)/len(lst))) # 산술평균
print(lst[n//2]) # 중앙값
# 최빈값 - 다수일 때는 두 번째로 작은 값 출력
if len(target) == 1:
    print(target[0])
else:
    print(sorted(target)[1]) 
print(max(lst)-min(lst)) # 범위 

# 결과 : 최빈값을 구하는 과정이 너무 오래걸려서 시간초과뜸
"""

"""
2차 제출코드
n = int(input())
lst = sorted([int(input()) for i in range(n)])
lst2 = sorted(lst, key = lambda x: -lst.count(x))

tmp = []
i = 0
while i < len(lst2)-1:
    tmp.append(lst2[i])
    i += lst2.count(lst2[i])
    if lst2.count(lst[i]) != lst2.count(tmp[0]):
        break

print('%.0f'% (sum(lst)/len(lst))) # 산술평균
print(lst[n//2]) # 중앙값

if len(tmp) == 0:
    print(lst[0])
elif len(tmp) == 1:
    print(tmp[0])
else:
    print(sorted(tmp)[1])

print(max(lst)-min(lst)) # 범위

# 결과 : 또 시간초과. 어떻게 하면 좋은거지?
"""

"""
3차 제출코드 - 입력을 sys로 해봄. 실패!
import sys
n = int(input())
lst = []
for i in range(n):
    x = int(sys.stdin.readline())
    lst.append(x)
lst.sort()
lst2 = sorted(lst, key = lambda x: -lst.count(x))

tmp = []
i = 0
while i < len(lst2)-1:
    tmp.append(lst2[i])
    i += lst2.count(lst2[i])
    if lst2.count(lst[i]) != lst2.count(tmp[0]):
        break

print('%.0f'% (sum(lst)/len(lst))) # 산술평균
print(lst[n//2]) # 중앙값

if len(tmp) == 0:
    print(lst[0])
elif len(tmp) == 1:
    print(tmp[0])
else:
    print(sorted(tmp)[1])

print(max(lst)-min(lst)) # 범위
"""
# import sys
# from collections import Counter
# n = int(input())
# lst = []
# for i in range(n):
#     x = int(sys.stdin.readline())
#     lst.append(x)
# lst.sort()

# x = Counter(lst).most_common()
# tmp = [x[0][0]]
# i = 0
# while i < len(x)-1 and x[i][1] == x[i+1][1]:
#     tmp.append(x[i+1][0])
#     i += 1

# print('%.0f'% (sum(lst)/len(lst))) # 산술평균
# print(lst[n//2]) # 중앙값

# if len(tmp) == 1:
#     print(tmp[0])
# else:
#     print(sorted(tmp)[1])

# print(max(lst)-min(lst)) # 범위


# 다른사람 중 극한의 숏코더 것을 참고했는데
# 특히 126번과 127번 라인에서 최빈값 쪽이 신기했다. 저런 식으로도 할 수 있구나.
# 진심 혼자서 계속 보면서 이게 대체 뭔가 싶었다.
# import sys, collections
# d = sorted(int(sys.stdin.readline()) for i in "0" * int(input()))
# c = collections.Counter(d)
# t = sorted(x for x in c if c[x] == max(c.values()))
# print('%.f' % (sum(d)/len(d)), d[len(d)//2], t[len(t)!=1], max(d)-min(d), sep='\n')