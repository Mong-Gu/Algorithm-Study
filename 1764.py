import sys
n, m = map(int, input().split())
n_lst = set([sys.stdin.readline().strip() for i in range(n)])
m_lst = set([sys.stdin.readline().strip() for i in range(m)])
result = sorted(list(n_lst & m_lst))
print(len(result))
for i in result:
    print(i)

# # 이름이 중복이 될 수도 있다는 생각을 해보고 구현해보자.
# import sys
# n, m = map(int, input().split())
# n_lst = sorted([sys.stdin.readline().strip() for i in range(n)])
# m_lst = sorted([sys.stdin.readline().strip() for i in range(m)])

# n_set = set(n_lst)
# m_set = set(m_lst)
# result = n_set & m_set
# print()
# for i in result:
#     repeat = min(n_lst.count(i), m_lst.count(i))
#     for j in range(repeat):
#         print(i)

# 헛짓거리했다. 출력문의 조건을 제대로 안보고 이름만 사전순으로 출력함.