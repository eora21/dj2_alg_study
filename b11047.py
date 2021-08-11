N, M = map(int, input().split())

coins = []
num = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(N - 1, -1, -1):
    num += M // coins[i]
    M %= coins[i]

print(num)