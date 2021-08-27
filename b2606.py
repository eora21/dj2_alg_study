N = int(input())
li = [[] for _ in range(N)]
place = [0] * N
queue = [0]
place[0] = 1

for _ in range(int(input())):
    S, G = map(int, input().split())
    li[S-1].append(G - 1)
    li[G-1].append(S - 1)

while queue:
    while li[queue[0]]:
        if not place[li[queue[0]][0]]:
            queue.append(li[queue[0]][0])
            place[li[queue[0]][0]] = 1
        del(li[queue[0]][0])
    del(queue[0])

print(place.count(1) - 1)