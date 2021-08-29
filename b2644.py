N = int(input())
S, G = map(int, input().split())
li = [[] for _ in range(N)]
for _ in range(int(input())):
    A, B = map(int, input().split())
    li[A - 1].append(B - 1)
    li[B - 1].append(A - 1)

queue = [S - 1]
place = [-1] * N
place[S - 1] = 0

while queue:
    while li[queue[0]]:
        if place[li[queue[0]][0]] == -1:
            queue.append(li[queue[0]][0])
            place[li[queue[0]][0]] = place[queue[0]] + 1
        del li[queue[0]][0]
    del queue[0]
    if place[G - 1] != -1:
        break

print(place[G - 1])