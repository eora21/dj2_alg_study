import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {input() for _ in range(N)}

total = 0
for _ in range(M):
    if input() in S:
        total += 1

print(total)