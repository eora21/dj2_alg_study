P = int(input())
T = list(map(int, input().split()))

T.sort()

time = 0
total = 0
for i in range(P):
    time += T[i]
    total += time

print(total)