import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())
A -= 1
B -= 1
field = [[False] * N for _ in range(N)]

for _ in range(M):
    X, Y = map(int, input().split())
    field[X - 1][Y - 1] = True
    field[Y - 1][X - 1] = True

dijkstra = [N] * N
check = [True] * N
dijkstra[A] = 0
res = -1

for _ in range(N):
    start = -1
    min_val = N
    for i in range(N):
        if check[i] and min_val > dijkstra[i]:
            min_val = dijkstra[i]
            start = i

    if start == -1:
        break
    elif start == B:
        res = dijkstra[start]
        break

    check[start] = False

    for i in range(N):
        if field[start][i]:
            dijkstra[i] = min(dijkstra[start] + 1, dijkstra[i])

print(res)