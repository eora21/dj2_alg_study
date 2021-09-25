def make_start(pick=0, num=0):
    if num == N // 2:
        make_link(pick, num)
        # print(start)
        return
    
    for i in range(num, N//2):
        team[i] = 0
        make_start(pick+1, i+1)
        team[i] = 1


def make_link(pick=0, num=0):
    if pick == N // 2:
        make_score()
        return

    if num == N:
        return
    
    for i in range(num, N):
            team[i] = 0
            make_link(pick+1, i+1)
            team[i] = 1

    make_link(pick, i + 1)


def make_score():
    status = [0] * 2
    for i in range(N):
        for j in range(N):
            if team[i] == team[j]:
                status[team[i]] += li[i][j]

    global min_minus_status
    minus_status = abs(status[0] - status[1])
    if min_minus_status > minus_status:
        min_minus_status = minus_status


N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

team = [1] * N
min_minus_status = 100 * N

make_start()

print(min_minus_status)