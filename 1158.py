N, K = map(int, input().split())

people = [p for p in range(1, N + 1)]

i = 0
log = []
while N:
    i += K - 1
    i %= N
    log.append(str(people.pop(i)))
    N -= 1

print(f"<{', '.join(log)}>")