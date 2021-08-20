N = int(input())

Hanoi = [list(map(int, input().split())), [], []]

target = N
i = 0
cnt = 0

log = []

while len(Hanoi[2]) < N:
    i %= 2
    if target in Hanoi[i]:
        while True:
            t = Hanoi[i].pop()
            cnt += 1
            if t == target:
                Hanoi[2].append(t)
                log.append(f"{i + 1} {3}")
                target -= 1
                break
            else:
                Hanoi[not i].append(t)
                log.append(f"{i + 1} {(not i) + 1}")
    i += 1

print(cnt)
for l in log:
    print(l)