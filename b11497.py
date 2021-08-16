T = int(input())

for _ in range(T):
    N = int(input())
    wood = list(map(int, input().split()))

    wood.sort()
    li = [0] * N

    for i in range(N):
        li[i // 2 + (i % 2) * (N - 1 +(- 2) * (i // 2))] = wood[i] #홀수일때 N - 1 - i // 2
    
    cnt = abs(li[0] - li[-1])
    for w in range(N - 1):
        if cnt < abs(li[w] - li[w + 1]):
            cnt = abs(li[w] - li[w + 1])

    print(cnt)