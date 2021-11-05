N, D = map(int, input().split())
fast_road = sorted([list(map(int, input().split())) for _ in range(N)])
dp = list(range(D + 1))

for now, to, val in fast_road:
    if to <= D and dp[to] > dp[now] + val:
        another_dp = list(range(dp[now] + val, dp[now] + val + D - to + 1))
        for i in range(to, D + 1):
            dp[i] = another_dp[i - to] if another_dp[i - to] < dp[i] else dp[i]

print(dp[-1])