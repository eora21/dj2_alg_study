dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def make_num(r, c, n, step=1):
    if step == 6:
        nums.append(n)
        return

    for to in range(4):
        y = r + dy[to]
        x = c + dx[to]

        if 0 <= y < 5 and 0 <= x < 5:
            make_num(y, x, n * 10 + field[y][x], step + 1)


field = [list(map(int, input().split())) for _ in range(5)]

nums = []
for row in range(5):
    for col in range(5):
        num = field[row][col]
        make_num(row, col, num)

print(len(set(nums)))