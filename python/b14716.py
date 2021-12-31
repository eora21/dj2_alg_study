import sys
input = sys.stdin.readline 


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def DFS(row, col):
    stack.append((row, col))
    while stack:
        r, c = stack.pop()
        for to in range(8):
            y = r + dy[to]
            x = c + dx[to]
            if 0 <= y < M and 0 <= x < N and image[y][x]:
                image[y][x] = 0
                stack.append((y, x))


M, N = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(M)]
stack = []

cnt = 0
for row in range(M):
    for col in range(N):
        if image[row][col]:
            image[row][col] = 0
            DFS(row, col)
            cnt += 1

print(cnt)