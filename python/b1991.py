def traversal(key='A'):
    first.append(key)
    left, right = tree[key][0], tree[key][1]
    
    if left != '.':
        traversal(left)
    middle.append(key)

    if right != '.':
        traversal(right)
    last.append(key)

    return


tree = {}

N= int(input())
for _ in range(N):
    center, left, right = input().split()
    tree[center] = [left, right]

first = []
middle = []
last = []

traversal()

print(''.join(first))
print(''.join(middle))
print(''.join(last))