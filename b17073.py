from collections import deque
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
tree = [[] for _ in range(N)]
place = [True] * N
queue = deque()
queue.append(0)

for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U-1].append(V-1)
    tree[V-1].append(U-1)

count = 0

while queue:
    if place[queue[0]]:
        place[queue[0]] = False
        flag = True
        for leaf in tree[queue[0]]:
            if place[leaf]:
                flag = False
                queue.append(leaf)

        if flag:
            count += 1

    queue.popleft()

print(W / count)
