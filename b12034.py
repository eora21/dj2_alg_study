for case in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))
    result = []
    
    i = 1
    while li:
        if li[0] // 3 * 4 == li[i]:
            result.append(li[0])
            del[li[i]]
            del(li[0])
            i = 1
        else:
            i += 1

    print("Case #{}: ".format(case + 1), end="")
    print(*result)