def weight_write(H, L):
    more_H = field[H][0] | set([H])
    more_L = field[L][1] | set([L])
    for mh in more_H:
        for ml in more_L:
            field[mh][1].add(ml)
            field[ml][0].add(mh)

N, M = map(int, input().split())
field = [[set(), set()] for _ in range(N + 1)]

for _ in range(M):
    scale = list(map(int, input().split()))
    weight_write(scale[0], scale[1])
    
total = 0
for i in range(1, N + 1):
    if len(field[i][0]) > N // 2 or len(field[i][1]) > N // 2:
        total += 1

print(total)