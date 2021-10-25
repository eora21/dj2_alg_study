import sys
from typing import Deque
input = sys.stdin.readline

N, M = map(int, input().split())
coms = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    coms[B].append(A)

max_val = 0
ans = []
queue = Deque()
for idx in range(1, N + 1):
    cnt = 1
    if coms[idx]:
        check = [True] * (N + 1)
        check[idx] = False
        queue.append(idx)
        while queue:
            i = queue.popleft()
            for move in coms[i]:
                if check[move]:
                    check[move] = False
                    cnt += 1
                    queue.append(move)

    if max_val < cnt:
        max_val = cnt
        ans.clear()
        ans.append(idx)

    elif max_val == cnt:
        ans.append(idx)

print(*ans)