from typing import Deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N = int(input())
field = []
flag = True
sr = sc = -1
for row in range(N):
    field.append(list(map(int, input().split())))
    if flag:
        for col in range(N):
            if field[row][col] == 9:
                sr = row
                sc = col
                flag = False
                break

queue = Deque()
queue.append((sr, sc, 0))
baby_size = 2
ate = 0
possible_eat_list = []
check = [[True] * N for _ in range(N)]
check[sr][sc] = False
field[sr][sc] = 0
total_second = 0
while queue:
    r, c, second = queue.popleft()
    for to in range(4):
        y = r + dy[to]
        x = c + dx[to]
        if 0 <= y < N and 0 <= x < N and check[y][x]:
            check[y][x] = False
            if field[y][x] == 0 or field[y][x] == baby_size:
                if not possible_eat_list:
                    queue.append((y, x, second + 1))
            elif baby_size > field[y][x]:
                if not possible_eat_list:
                    total_second += second + 1
                    idx = 0
                    while idx < len(queue):
                        if queue[idx][2] > second:
                            del(queue[idx])
                        else:
                            idx += 1

                possible_eat_list.append((y, x))

    if not queue and possible_eat_list:
        possible_eat_list.sort(key=lambda x: (x[0], x[1]))
        y, x = possible_eat_list[0]
        field[y][x] = 0
        queue.append((y, x, 0))
        check = [[True] * N for _ in range(N)]
        check[y][x] = False
        possible_eat_list.clear()
        ate += 1
        if ate == baby_size:
            baby_size += 1
            ate = 0

print(total_second)