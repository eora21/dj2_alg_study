N = int(input())
nums = list(map(int, input().split()))
ans = [-1] * N

for now in range(N - 1, -1, -1):
    for target in range(now - 1, -1, -1):
        if nums[now] > nums[target]:
            ans[target] = nums[now]
        else:
            break

print(*ans)
