T = int(input())

for _ in range(T):
    N = int(input())
    wood = list(map(int, input().split()))

    wood.sort(reverse=True)

    cnt = abs(wood[0] - wood[1])
    for w in range(N - 2):
        if cnt < abs(wood[w] - wood[w + 2]):
            cnt = abs(wood[w] - wood[w + 2])

    print(cnt)