T = int(input())

lst = [[i for i in range(1, 15)]] # 0층 각 호수의 거주 인원
for i in range(14): # 총 열네층을 더해야 함
    tmp = [] # i+1층의 거주 인원 담을 리스트
    for j in range(14): # 각 호수를 돌며 인원 집계
        tmp.append(sum(lst[i][:j+1]))
    lst.append(tmp) # i+1층의 거주 인원 체크 완료

# 아파트 구성 인원 보기
# lst.reverse()
# for i in lst:
#     print(i)

for i in range(T):
    k = int(input())
    n = int(input())
    print(lst[k][n-1])
