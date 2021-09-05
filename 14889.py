def make_team(num=0):
    if num == N // 2:
        global min_minus_status
        
        for i in range(N):
            if i not in start:
                link.append(i)
        
        start_status = make_status(start)
        link_status = make_status(link)
        minus_status = abs(start_status - link_status)
        
        if min_minus_status > minus_status:
            min_minus_status = minus_status
        
        link.clear()

        return

    for i in range(N):
        if i not in start:
            start.append(i)
            make_team(num + 1)
            start.pop()
    return min_minus_status


def make_status(arr):
    status = 0
    for i in arr:
        for j in arr:
            status += li[i][j]
    return status


N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

start = []
link = []

min_minus_status = 100 * N

print (make_team())

# 시간초과
