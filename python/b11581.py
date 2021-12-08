import sys
input = sys.stdin.readline

def DFS(now):
    if now == N:
        return True
    
    for load in loads[now]:
        if check[load]:
            check[load] = False
            if not DFS(load):
                return False
            check[load] = True
        else:
            return False
    
    return True
    

N = int(input())
loads = [[] for _ in range(N + 1)]

flag = False
for p in range(1, N):
    _ = int(input())
    loads[p] = list(map(int, input().split()))
    
stack = []
check = [True] * (N + 1)
ans = True
for i in range(1, N + 1):
    if not DFS(i):
        ans = False
        break


print("NO CYCLE" if ans else "CYCLE")

