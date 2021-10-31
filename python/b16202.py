import sys
input = sys.stdin.readline


def find_set(x):
    while x != node[x]:
        x = node[x]
    return x


def union(x, y):
    node[find_set(y)] = find_set(x)


N, M, K = map(int, input().split())
field = [[] for _ in range(N + 1)]
log = [list(map(int, input().split())) for _ in range(M)]

for game in range(K):
    node = list(range(N + 1))
    score = 0
    cnt = 0
    flag = False
    for line in range(game, M):
        A, B = log[line]
        if find_set(A) != find_set(B):
            score += line + 1
            cnt += 1
            union(A, B)
            if cnt == N - 1:
                flag = True
                break
    
    if flag:
        print(score, end=" ")
    else:
        print("0 " * (K - game))
        break
    
    