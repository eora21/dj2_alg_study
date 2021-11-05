def switch(index):
    global cnt
    for i in range(index - 1, index + 2):
        if 0 <= i < N:
            lights[i] = 1 - lights[i]
    cnt += 1
    print(lights)


N = int(input())
lights_now = list(map(int, input()))
lights = list(map(int, input()))
for i in range(N):
    lights[i] ^= lights_now[i]

cnt = 0

if lights[-1] != lights[-2]:
    switch(N - 3)
if lights[0] and ((lights[1] and lights.count(1) % 3) or (not lights[1] and not lights.count(1) % 3)):
    switch(0)

for i in range(N - 1):
    if lights[i]:
        switch(i + 1)

print(-1 if lights[-1] else cnt)