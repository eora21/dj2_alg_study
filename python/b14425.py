import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input() for _ in range(N)]
check = [input() for _ in range(M)]

cnt = 0
st = "/".join(S)
for i in range(M):
    if check[i] in st:
        cnt += 1
print(cnt)

#시간초과