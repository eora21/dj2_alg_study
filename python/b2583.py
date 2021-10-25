adder = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def check(r, c):
    queue = [(r, c)]
    cnt = 1
    while queue:
        r, c = queue.pop(0)
        for arrow in range(4):
            y_adder, x_adder = adder[arrow]
            if 0 <= r + y_adder < M and 0 <= c + x_adder < N and arr[r + y_adder][c + x_adder]:
                arr[r + y_adder][c + x_adder] = 0
                queue.append((r + y_adder, c + x_adder))
                cnt += 1
    
    return cnt


M, N, K = map(int, input().split())

arr = [[1] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for row in range(y1, y2):
        for col in range(x1, x2):
            arr[row][col] = 0

square = []

for row in range(M):
    for col in range(N):
        if arr[row][col]:
            arr[row][col] = 0
            square.append(check(row, col))

print(len(square))
print(*sorted(square))
