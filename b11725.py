import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def make_tree(me=1, parent=1):
    for node in link[me]:
        if node != parent:
            tree[node] = me
            make_tree(node, me)


N = int(input())
link = [[] for _ in range(N + 1)]
tree = [0] * (N + 1)

for _ in range(N - 1):
    A, B = map(int, input().split())
    link[A].append(B)
    link[B].append(A)

make_tree()

for i in range(2, N+1):
    print(tree[i])
