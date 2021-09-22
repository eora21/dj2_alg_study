for _ in range(int(input())):
    N = int(input())

    tree_up = [[] for _ in range(N)]
    tree_down = [[] for _ in range(N)]

    for _ in range(N - 1):
        A, B = map(int, input().split())
        tree_down[A-1].append(B-1)
        tree_up[B-1].append(A-1)
    
    A, B = map(int, input().split())

    parent = A - 1
    leaf = A - 1

    while True:
        if leaf == B - 1:
            print(parent + 1)
            break

        if tree_down[leaf]:
            down_leaf = tree_down[leaf][0]
            del(tree_down[leaf][0])
            leaf = down_leaf
        elif parent == leaf:
            parent = tree_up[leaf][0]
            tree_down[parent].remove(leaf)
            leaf = parent
        else:
            leaf = tree_up[leaf][0]