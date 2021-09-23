import sys
input = sys.stdin.readline

N = int(input())

router = []
while True:
    data = int(input())

    if data == -1:
        break

    if data == 0:
        del(router[0])
        continue

    if len(router) == N:
        continue
    else:
        router.append(data)

if router:
    print(*router)
else:
    print("empty")
