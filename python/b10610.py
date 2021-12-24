N = list(map(int, input()))

if 0 in N and sum(N) % 3 == 0:
    print(*sorted(N, reverse=True), sep="")
else:
    print(-1)
