n = int(input())
original_lst = list(map(int, input().split()))
sorted_lst = sorted(list(set(original_lst)))
answer = {}
for i in range(len(sorted_lst)):
    answer[sorted_lst[i]] = i
for i in original_lst:
    print(answer[i], end = ' ')

# n = int(input())
# original_lst = list(map(int, input().split()))
# sorted_lst = sorted(list(set(original_lst)))
# dic = {}
# for i in original_lst:
#     dic[i] = dic.get(i, sorted_lst.index(i))
#     print(dic[i], end = ' ')

# 시간초과 떠버렸던 처음 코드.