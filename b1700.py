N, K = map(int, input().split())
nums = list(map(int, input().split()))
multitap = set()
next = set()
cnt = 0

for i in range(len(nums)):
    if len(multitap) < N:
        multitap.add(nums[i])
        continue

    if len(next) == 0 and nums[i] in multitap:
        continue

    for j in range(i, K):
        if len(next) < N:
            next.add(nums[j])
            continue
    
        ready = multitap - next
        for k in range(j, K):
            if len(ready) == 1:
                break
            ready.discard(nums[k])

        multitap -= ready
        cnt += len(ready)
        multitap.add(nums[i])
        next.clear()
        break
    
cnt += len(next - multitap)
print(cnt)
