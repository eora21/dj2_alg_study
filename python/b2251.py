from typing import Deque


A, B, C = map(int, input().split())
check = [[True] * (C + 1) for _ in range(A + 1)]
queue = Deque()

queue.append([0, 0, C])
check[0][C] = False

move = [0] * 6
while queue:
    a, b, c = queue.popleft()

    target = min(a + b, B)
    move[0] = [a + b - target, target, c]  # AtoB

    target = min(a + c, C)
    move[1] = [a + c - target, b, target]  # AtoC

    target = min(b + a, A)
    move[2] = [target, b + a - target, c]  # BtoA

    target = min(b + c, C)
    move[3] = [a, b + c - target, target]  # BtoC

    target = min(c + a, A)
    move[4] = [target, b, c + a - target]  # CtoA

    target = min(c + b, B)
    move[5] = [a, target, c + b - target]  # CtoB

    for mov in move:
        if check[mov[0]][mov[2]]:
            check[mov[0]][mov[2]] = False
            queue.append(mov)

for i in range(C + 1):
    if not check[0][i]:
        print(i, end=" ")