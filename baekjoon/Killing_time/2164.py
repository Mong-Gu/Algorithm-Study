from collections import deque
n = int(input()) # 1 <= n <= 500,000
cards = deque([i for i in range(1, n+1)])
while len(cards) > 1:
    cards.popleft() # (1) 제일 위에 있는 카드를 버린다
    cards.append(cards.popleft()) # (2) 그 다음 제일 위에 있는 카드를 맨 뒤로 보낸다
print(cards[0])