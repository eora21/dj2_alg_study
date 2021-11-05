def search(index):
    for i in range(index - K, index + K + 1):
        if 0 <= i < N and st[i] == 'P':
            st[i] = 'X'
            return 1
    return 0


N, K = map(int, input().split())
st = list(input())
total = 0

for idx in range(N):
    if st[idx] == 'H':
        total += search(idx)

print(total)
