def BFS(repeat=0, abs_sum=0):
    if repeat == N:
        global total
        if abs_sum > total:
            total = abs_sum
        return
    
    for i in range(N):
        if check[i]:
            continue
        abs_minus = 0
        queue.append(nums[i])
        check[i] = True

        if repeat > 0:
            abs_minus = abs(queue[repeat-1] - queue[repeat])
            abs_sum += abs_minus

        BFS(repeat+1, abs_sum)

        queue.pop()
        check[i] = False
        abs_sum -= abs_minus
    
    return total


N = int(input())
nums = list(map(int, input().split()))

check = [False] * N
queue = []
total = 0

print(BFS())