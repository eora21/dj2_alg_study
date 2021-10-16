from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

check = [True] * (N + 1)
check[1] = False
total = 0

queue = deque()
queue.append((1, 0))

while queue:
    node, step = queue.popleft()

    if len(tree[node]) == 1 and node != 1:
        total += step
        continue

    for idx in tree[node]:
        if check[idx]:
            check[idx] = False
            queue.append((idx, step + 1))

print("Yes" if total % 2 else "No")
