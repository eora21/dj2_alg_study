for case in range(int(input())):
    N = int(input())
    li = list(map(int, input().split()))
    result = []
    
    i = 0
    while li:
        if not li[i] % 3 and li[i] // 3 * 4 in li:
            result.append(li[i])
            li.remove(li[i] // 3 * 4)
            del(li[i])
        else:
            i = (i + 1) % len(li)

    print("Case #{}: ".format(case + 1), end="")
    print(*result)