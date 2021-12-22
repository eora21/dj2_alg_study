from typing import Deque


N = int(input())
cards = Deque(range(1, N + 1))

for _ in range(N - 1):
    print(cards.popleft(), end=" ")
    cards.append(cards.popleft())

print(cards[0])
