N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse = True)

total = 0
for i in range(N):
    w = rope[i] * (i + 1)

    if total < w:
        total  = w
    else:
        break

print(int(total))