N = int(input())
balloon = list(map(int, input().split()))
idx = 0
cnt = 0

while cnt < N - 1:
    print(idx + 1, end=" ")
    paper = balloon[idx]
    goto = 1 if paper > 0 else -1
    paper *= goto
    balloon[idx] = 0
    
    step = 0

    while step < paper:
        idx += goto
        if idx >= N:
            idx -= N
        elif idx < 0:
            idx += N

        if balloon[idx] != 0:
            step += 1
    
    cnt += 1

print(idx + 1)
