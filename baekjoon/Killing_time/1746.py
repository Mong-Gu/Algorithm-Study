import sys
n, m = map(int, input().split())
n_lst = set([sys.stdin.readline().strip() for i in range(n)])
m_lst = set([sys.stdin.readline().strip() for i in range(m)])
result = sorted(list(n_lst & m_lst))
for i in result:
    print(i)