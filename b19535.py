import sys
input = sys.stdin.readline

N = int(input())
field = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    field[A].append(B)
    field[B].append(A)

queue = [0] * (N + 1)
queue[0] = 1
head = -1
tail = 0
check = [True] * (N + 1)
check[1] = False
D = 0
G = 0

while head < tail:
    head += 1
    now = queue[head]
    L = len(field[now])
    
    if L > 2:
        G += L * (L - 1) * (L - 2) // 6
    
    for child in field[now]:
        if check[child]:
            check[child] = False
            tail += 1
            queue[tail] = child

            down = len(field[child]) - 1
            D += (L - 1) * down

ans = "G"
if D == G * 3:
    ans = "DUDUDUNGA"
elif D > G * 3:
    ans = "D"

print(ans)
