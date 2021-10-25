from typing import Deque

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]


def BFS():
    while queue:
        r, c, step = queue.popleft()
        for to in range(8):
            y = r + dy[to]
            x = c + dx[to]
            if 0 <= y < N and 0 <= x < N and check[y][x]:
                check[y][x] = False
                if y == target_r and x == target_c:
                    print(step + 1)
                    return
                queue.append((y, x, step + 1))


for _ in range(int(input())):
    N = int(input())
    sr, sc = map(int, input().split())
    target_r, target_c = map(int, input().split())
    if sr == target_r and sc == target_c:
        print(0)
        continue
    check = [[True] * N for _ in range(N)]
    queue = Deque()
    check[sr][sc] = False
    queue.append((sr, sc, 0))
    BFS()