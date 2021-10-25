def BFS(li, flag=True):
    for i in range(N):
        if li[i] == "Y" and not check[i]:
            check[i] = True
            if flag:
                queue.append(i)
    if flag:
        for j in range(len(queue)):
            BFS(friends[queue[j]], False)
    return check.count(True)


N = int(input())

friends = [input() for _ in range(N)]

In_Ssa = 0

for i in range(N):
    queue = []
    check = [False] * N
    check[i] = True
    cnt = BFS(friends[i])
    if In_Ssa < cnt:
        In_Ssa = cnt

print(In_Ssa - 1)
