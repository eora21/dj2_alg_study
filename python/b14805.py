K = int(input())
log = list(map(int, input().split()))
N = max(log) + 1
node = [-1] * N
stack = [log[0]]

for idx in log[1:]:
    if len(stack) > 1 and stack[-2] == idx:
        stack.pop()
    else:
        node[idx] = stack[-1]
        stack.append(idx)

print(N)
print(*node)