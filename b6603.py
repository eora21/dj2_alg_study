def BFS(repeat=0, idx=-1):
    if repeat == 6:
        print(*queue)
        return

    for i in range(idx + 1, N):
        if check[i]:
            queue.append(nums[i+1])
            check[i] = False
            BFS(repeat+1, i)
            queue.pop()
            check[i] = True
    
    return


while True:
    st = input()
    if st == "0":
        break

    nums = list(map(int, st.split()))
    N = nums[0]
    check = [True] * N
    queue = []

    BFS()
    
    print()
