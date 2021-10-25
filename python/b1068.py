def erase(num):
    for c in tree[num]:
        erase(c)
    tree[num].append(-1)
    return


N = int(input())
st = list(map(int, input().split()))
tree = [[] for _ in range(N)]

for i in range(N):
    if st[i] != -1:
        tree[st[i]].append(i)

cut = int(input())
erase(cut)

try:
    tree[st[cut]].remove(cut)
except:
    pass

ans = 0

for leaf in tree:
    if not leaf:
        ans += 1

print(ans)
