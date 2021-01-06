from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
	visited[v] = True # dfs에서 방문 표시는 True
	print(v, end=' ')
	for i in range(1, n+1):
		if visited[i] == False and graph[v][i]:
			dfs(i)

def bfs(v):
	queue = deque([v])
	visited[v] = False # bfs에서 방문 표시는 False
	while queue:
		v= queue.popleft()
		print(v, end=' ')
		for i in range(1, n+1):
			if visited[i] == True and graph[v][i]:
				queue.append(i)
				visited[i] = False

n, m, v = map(int, input().strip().split())
graph = [[0] * (n+1) for i in range(n+1)]

for i in range(m):
	v1, v2 = map(int, input().strip().split())
	graph[v1][v2] = graph[v2][v1] = 1
visited = [False] * (n+1)

dfs(v)
print()
bfs(v)

# 첫 번째 코드 - 실패
# 인접리스트를 활용한 건 왜 안됐지?

# from collections import deque
# import heapq
# import sys
# input = sys.stdin.readline

# def dfs(v):
# 	visited_dfs[v] = True
# 	print(v, end = ' ')
# 	for i in graph[v]:
# 		if not visited_dfs[i]:
# 			dfs(i)

# def bfs(start):
# 	queue = deque([start])
# 	visited_bfs[start] = True
# 	while queue:
# 		v = queue.popleft()
# 		print(v, end = ' ')
# 		for i in graph[v]:
# 			if not visited_bfs[i]:
# 				queue.append(i)
# 				visited_bfs[i] = True

# n, m, v = map(int, input().strip().split())
# graph = [[] for i in range(n+1)]
# for _ in range(m):
# 	v1, v2 = map(int, input().strip().split())
# 	heapq.heappush(graph[v1], v2)
# 	heapq.heappush(graph[v2], v1)
# print(graph)
# visited_dfs = [False] * (n+1)
# visited_bfs = [False] * (n+1)

# dfs(v)
# print()
# bfs(v)

# ---

# 아래 코드는 인접리스트 활용한 것. - jeonjine님의 코드
# https://www.acmicpc.net/source/24899980

# from collections import deque

# def dfs(N, M, V, adjList):
#     stack = []
#     stack.append(V)

#     hasBeenDict = {}
#     retList = []
#     while len(stack) > 0:
#         nowV = stack.pop()
#         if not (nowV in hasBeenDict):
#             retList.append(str(nowV))
#             hasBeenDict[nowV] = True
#             for adjV in adjList[nowV]:
#                 stack.append(adjV)
#     print(" ".join(retList))

# def bfs(N, M, V, adjList):
#     queue = deque([])
#     queue.append(V)

#     hasBeenDict = {}
#     retList = []
#     while len(queue) > 0:
#         nowV = queue.popleft()
#         if not (nowV in hasBeenDict):
#             retList.append(str(nowV))
#             hasBeenDict[nowV] = True
#             for adjV in adjList[nowV]:
#                 queue.append(adjV)
#     print(" ".join(retList))

# def main():
#     numList = list(map(int, (input()).split()))
#     N, M, V = numList[0], numList[1], numList[2]

#     adjList = [[] for i in range(N+1)]
#     for m in range(M):
#         edge = tuple(map(int, (input()).split()))
#         adjList[edge[0]].append(edge[1])
#         adjList[edge[1]].append(edge[0])

#     for n in range(1, N+1):
#         adjList[n].sort(reverse=True)
#     dfs(N, M, V, adjList)

#     for n in range(1, N+1):
#         adjList[n].sort()
#     bfs(N, M, V, adjList)

# main()
