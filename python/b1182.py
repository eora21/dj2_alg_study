def pick(step=0, total=0, p=False):
    if step == N:
        if total == S and p:
            global cnt
            cnt += 1
        return
    
    pick(step + 1, total + nums[step], True)
    pick(step + 1, total, p)



N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
pick()
print(cnt)