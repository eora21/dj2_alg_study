def switch(b, idx):
    for step in range(3):
        if idx + step < N + 1:
            lights[b][idx + step] ^= 1


def check():
    global cnt
    for b in range(2):
        cnt = 0
        for i in range(N):
            if lights[b][i]:
                cnt += 1
                switch(b, i)

        if not lights[b][-1]:
            return True


N = int(input())
lights_now = list(map(int, input()))
lights_target = list(map(int, input()))
lights = [[0], [1]]

for i in range(N):
    b = lights_now[i]^lights_target[i]
    lights[0].append(b)
    lights[1].append(b)

cnt = 0
print(cnt if check() else -1)