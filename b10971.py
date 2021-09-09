def BFS(repeat=0, city=0, total_cost=0):
    global lowest_cost
    if repeat == N - 1 and cities[city][0] != 0:
        if lowest_cost > total_cost + cities[city][0]:
            lowest_cost = total_cost + cities[city][0]
        return
    for i in range(1, N):
        if check[i-1] and cities[city][i] != 0:
            cost = cities[city][i]
            if total_cost + cost >= lowest_cost:
                continue
            check[i-1] = False
            BFS(repeat + 1, i, total_cost + cost)
            check[i-1] = True

    return lowest_cost

N = int(input())

cities = [list(map(int, input().split())) for _ in range(N)]
check = [True] * (N - 1)
lowest_cost = 1000000 * N

print(BFS())