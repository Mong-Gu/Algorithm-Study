def solution(board, moves):
    bucket = []
    answer = 0
    for line in moves:
        for i in range(len(board)):
            if board[i][line-1]: # 인형이 있으면
                bucket.append(board[i][line-1])
                board[i][line-1] = 0
                break
        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            answer += 2
    return answer

'''
# 실패
def solution(board, moves):
    bucket = []
    answer = 0
    for line in moves:
        for i in range(len(board)):
            if board[i][line-1]: # 인형이 있으면
                if len(bucket) > 1:
                    if board[i][line-1] == bucket[-1]:
                        bucket.pop()
                        answer += 2
                    else:
                        bucket.append(board[i][line-1])
                else:
                    bucket.append(board[i][line-1])
                board[i][line-1] = 0
                break
    return answer
'''

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))