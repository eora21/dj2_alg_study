dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def DFS(r, c, step = 1) :
    if step == K and r == 0 and c == C - 1 :
        global ans
        ans += 1
        return
        elif step == K or (r == 0 and c == C - 1) :
        return

        for to in range(4) :
            y = r + dy[to]
            x = c + dx[to]
            if 0 <= y < R and 0 <= x < Cand field[y][x] != 'T' and check[y][x] :
                check[y][x] = False
                DFS(y, x, step + 1)
                check[y][x] = True

                R, C, K = map(int, input().split())
                field = [input() for _ in range(R)]
                check = [[True]* C for _ in range(R)]
                check[R - 1][0] = False

                ans = 0
                DFS(R - 1, 0)
                print(ans)