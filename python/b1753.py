import sys, heapq
readline = sys.stdin.readline

V, E = map(int, readline().split())
K = int(input())
K -= 1
field = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, readline().split())
    field[u-1].append((v-1, w))

check = [True] * V
djikstra = [11 * E] * V
hq = [(0, K)]

while hq:
    dis, start = heapq.heappop(hq)
    if not check[start]:
        continue

    djikstra[start] = dis
    check[start] = False

    for to, val in field[start]:
        if check[to]:
            heapq.heappush(hq, (dis + val, to))
    
for i in range(V):
    print(djikstra[i] if djikstra[i] != 11 * E else "INF")
