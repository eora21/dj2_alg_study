import sys, heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
field = [[] for _ in range(N + 1)]
djik = [300001] * (N + 1)
HQ = []
heapq.heappush(HQ, (0, X))
check = [True] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    field[A].append(B)

while HQ:
    dist, target = heapq.heappop(HQ)
    if check[target]:
        check[target] = False
        djik[target] = dist

        for to in field[target]:
            if check[to]:
                heapq.heappush(HQ, (dist + 1, to))

flag = True
for city in range(1, N + 1):
    if djik[city] == K:
        flag = False
        print(city)

if flag:
    print(-1)