import sys
readline = sys.stdin.readline


def down(st):
    node = tree
    for ch in st:
        try:
            node = node[ch]
        except:
            return False
    
    return True
    


N, M = map(int, input().split())
tree = {}

for _ in range(N):
    st = readline().rstrip()
    node = tree
    for ch in st:
        try:
            node[ch]
        except:
            node[ch] = {}
        node = node[ch]

cnt = 0
for _ in range(M):
    if down(readline().rstrip()):
        cnt += 1

print(cnt)