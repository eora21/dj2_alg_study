C = int(input())
Km = list(map(int, input().split()))
L = list(map(int, input().split()))
_L = L[:]
total = 0

min_L = min(L[:-1])

min_L_idx = []

i = 0
while True:
    if min_L == _L[i]:
        min_L_idx.insert(0, i)
        _L = _L[:i]
        if not len(_L):
            break
        min_L = min(_L)
        i = -1
    i += 1
# print(min_L)
for k in range(len(min_L_idx) - 1):
    total += sum(Km[min_L_idx[k]:min_L_idx[k + 1]]) * L[min_L_idx[k]]
total += sum(Km[min_L_idx[-1]:]) * L[min_L_idx[-1]]

print(total)