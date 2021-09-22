def make_team(num=0, human=0):
    global min_minus_status

    # if min_minus_status == 0:
    #     return 0

    if num == N // 2:
        print(team)

        status = [0] * 2
        for check in range(2):
            for i in range(N - 1):
                for j in range(i+1, N):
                    if team[i] == check and team[j] == check:
                        status[check] += li[i][j] + li[j][i]
        
        minus_status = abs(status[0] - status[1])

        if min_minus_status > minus_status:
            min_minus_status = minus_status

        return

    for i in range(human, N):
        if team[i]:
            team[i] = 0
            make_team(num+1, i+1)
            team[i] = 1
            
    return min_minus_status


N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

team = [1] * N
min_minus_status = 100 * N

print(make_team())

#시간초과