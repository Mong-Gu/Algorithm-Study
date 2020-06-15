# DNA
import sys
import collections

n, m = map(int, sys.stdin.readline().strip().split())
DNA = []
for i in range(n):
    DNA.append(sys.stdin.readline().strip())

result = []
cnt = 0

for i in range(m):
    tmp = [] # 각 문자열의 j번째 자리에 있는 알파벳을 임시로 담기 위한 리스트
    most = [] # 최종적으로 반환할 문자열의 j번째 자리 알파벳을 고르기 위함
    for j in range(n):
        tmp.append(DNA[j][i])
    tmp = collections.Counter(tmp).most_common()
    most.append(tmp[0])

    x = 1
    while len(tmp) != 1 and x <= len(tmp)-1 and tmp[x-1][1] == tmp[x][1]:
        most.append(tmp[x])
        x += 1
    if len(most) != 1:
        most.sort()

    result.append(most[0][0])
    cnt += n - most[0][1]

print(''.join(result))
print(cnt)

# 구현은 했는데 너무 코드가 못생겼다...