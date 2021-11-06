N = int(input())
nums = list(map(int, input().split()))
ans = [-1] * N

stack = []
for i in range(N - 1, -1, -1):
    now = nums[i]
    while stack:
        if stack[-1] > now:
            ans[i] = stack[-1]
            break
        else:
            del(stack[-1])
    stack.append(now)

print(*ans)
