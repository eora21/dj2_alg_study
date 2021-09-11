def make_original_tree(start, end, row=0):
    if start == end:
        tree_original[row].append(tree[start-1])
        return

    middle = (start + end) // 2
    tree_original[row].append(tree[middle-1])
    make_original_tree(start, middle-1, row+1)
    make_original_tree(middle+1, end, row+1)

    return

K = int(input())

tree = list(map(int, input().split()))
tree_original = [[] for _ in range(K)]

make_original_tree(1, 2**K-1)

for row in range(K):
    print(*tree_original[row])
