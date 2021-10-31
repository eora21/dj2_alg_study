import sys
input = sys.stdin.readline

n = int(input())
leaf_tree = [True] * (n + 1)
parent_tree = [0] * (n + 1)
score = [0] * (n + 1)
for _ in range(n - 1):
    parent, child, value = map(int, input().split())
    leaf_tree[parent] = False
    parent_tree[child] = parent
    score[child] = score[parent] + value

leafs = []
for i in range(1, n + 1):
    if leaf_tree[i]:
        leafs.append(i)

max_score = max(score)

first_leaf = score.index(max_score)
check = [False] * (n + 1)
TF = first_leaf
while TF:
    check[TF] = True
    TF = parent_tree[TF]

for second in range(len(leafs)):
    second_leaf = leafs[second]
    if first_leaf == second_leaf:
        continue
    TF = second_leaf
    while TF > 1:
        if check[TF]:
            break
        TF = parent_tree[TF]
    
    total = score[first_leaf] + score[second_leaf] - 2 * score[TF]
    if max_score < total:
        max_score = total

print(max_score)