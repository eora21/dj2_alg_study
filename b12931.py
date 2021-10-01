N = int(input())

nums = list(map(int, input().split()))


cnt = 0
while True:
    zero = 0
    flag = False

    for i in range(N):
        if nums[i] == 0:
            zero += 1
        elif nums[i] % 2:
            nums[i] -= 1
            cnt += 1
            flag = True
            break

    if flag:
        continue

    elif zero == N:
        print(cnt)
        break

    else:
        for i in range(N):
            nums[i] //= 2
        cnt += 1
