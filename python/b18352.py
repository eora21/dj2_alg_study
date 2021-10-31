import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
field = [[] for _ in range(N + 1)]
djik = [300001] * (N + 1)
djik[X] = 0
check = [True] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    field[A].append(B)

for _ in range(N):
    min_load = 300001
    target = X
    for search in range(1, N + 1):
        if check[search] and djik[search] < min_load:
            min_load = djik[search]
            target = search
    
    check[target] = False

    for to in field[target]:
        djik[to] = djik[target] + 1 if djik[target] + 1 < djik[to] else djik[to]

flag = True
for city in range(1, N + 1):
    if djik[city] == K:
        flag = False
        print(city)

if flag:
    print(-1)

#시간초과