from collections import deque

N, K = map(int, input().split())
cnt = 0
max_idx = min(100000, N * 2 if N > K else K * 2)
field = [100000] * (max_idx + 1)
queue = deque()
queue.append((K, 0))
field[K] = 0
while queue:
    now, step = queue.popleft()

    if N >= now:
        arrive_index = N - now + step
        field[N] = field[N] if field[N] < arrive_index else arrive_index
        continue
    elif now & 1:
        end = 2
    else:
        end = 3

    idx_list = [now + 1, now - 1, now // 2]
    for i in range(end):
        if 0 <= idx_list[i] < max_idx + 1 and field[idx_list[i]] > step + 1:
            field[idx_list[i]] = step + 1
            queue.append((idx_list[i], step + 1))

print(field[N])
