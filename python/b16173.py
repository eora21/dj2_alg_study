def DFS(r=0, c=0):
    step = field[r][c]

    if step == -1:
        return True

    for d in range(2):
        y = r if d else r + step
        x = c + step if d else c
        if 0 <= y < N and 0 <= x < N and check[y][x]:
            check[y][x] = False
            if DFS(y, x):
                return True
    
    return False


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
check = [[True] * N for _ in range(N)]
check[0][0] = False

print("HaruHaru" if DFS() else "Hing")
