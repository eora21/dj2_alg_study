C = int(input())
Km = list(map(int, input().split()))
L = list(map(int, input().split()))

oil = L[0]
total = 0

for i in range(1, len(L)):
    total += oil * Km[i - 1]
    if oil > L[i]:
        oil = L[i]

print(total)