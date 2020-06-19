# 보류
k = int(input())
s = input().strip().split(' ')

answer_min = []
answer_max = []
num_min = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_max = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 0
while n < k:
    cnt = 1
    if s[n] == '<': # 부호가 < 인 것의 연속
        for i in range(n+1, k-1): # 현재 지점의 다음 부호부터 s의 마지막 부호까지 순회
            if s[i] == '<':
                cnt += 1
            else:
                break

        # min에 대한 처리
        

        # max에 대한 처리
    
    else: # 부호가 > 인 것의 연속
        for i in range(n+1, k-1):
            if s[i] == '>':
                cnt += 1
            else:
                break
        
        # min에 대한 처리
        for i in range(cnt+1, -1, -1):
            answer_min.append(num_min.pop(i))

        # max에 대한 처리
        for i in range(cnt+1):
            answer_max.append(num_min.pop())
