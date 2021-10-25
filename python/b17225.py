import sys
input = sys.stdin.readline

time = [0] * 2
time[0], time[1], N = map(int, input().split())
start = [[] for _ in range(2)]
for _ in range(N):
    t, c, m = input().split()
    t = int(t)
    c = 0 if c == "B" else 1
    m = int(m)

    if time[c] == 0:
        start[c] += [t] * m

    else:
        lastend = 0 if not start[c] else start[c][-1] + time[c]
        if lastend > t:
            t = lastend
        start[c] += list(range(t, t + time[c] * m, time[c]))

A_len = len(start[0])
B_len = len(start[1])
A_ans = [0] * A_len
B_ans = [0] * B_len
num = 1
idx_a = idx_b = 0 

while num < A_len + B_len + 1:
    if idx_b == B_len or (idx_a < A_len and start[0][idx_a] <= start[1][idx_b]):
        A_ans[idx_a] = num
        idx_a += 1
    else:
        B_ans[idx_b] = num
        idx_b += 1
    num += 1

print(A_len)
print(*A_ans)
print(B_len)
print(*B_ans)