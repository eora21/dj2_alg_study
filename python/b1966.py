for _ in range(int(input())):
    N, M = map(int, input().split())
    check = [0] * N
    check[M] = True
    nums = list(map(int, input().split()))

    cnt = 1
    while nums:
        idx = nums.index(max(nums))
        if check[idx]:
            break

        nums = nums[idx + 1 :] + nums[: idx]
        check = check[idx + 1 :] + check[: idx]
        cnt += 1

    print(cnt)