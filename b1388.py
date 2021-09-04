arrow = {"-": (0, 1), "|": (1, 0)}

N, M = map(int, input().split())
floor = [list(input()) for _ in range(N)]

num = 0
for row in range(N):
    for col in range(M):
        if floor[row][col] in arrow.keys():
            delta_y, delta_x = arrow[floor[row][col]]
            cnt = 1
            while (0 <= row + delta_y * cnt < N and 0 <= col + delta_x * cnt < M) and \
                floor[row + delta_y * cnt][col + delta_x * cnt] == floor[row][col]:
                floor[row + delta_y * cnt][col + delta_x * cnt] = "X"
                cnt += 1
            else:
                floor[row][col] = "X"
                num += 1

print(num)
