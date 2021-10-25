N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

left = 0
right = N - 1
total = 0

while True:
    if 0 <= left <= N - 1 and nums[left] < 0:
        total += abs(nums[left]) * 2
        left += M
    elif 0 <= right <= N - 1 and nums[right] > 0:
        total += nums[right] * 2
        right -= M
    else:
        total -= -nums[0] if abs(nums[0]) > nums[N - 1] else nums[N - 1]
        break

print(total)