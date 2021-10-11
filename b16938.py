def pick(bits=0, total=0, easy=10**6, hard=0):
    if L <= total <= R and X <= abs(easy - hard):
        global cnt
        cnt += 1
    
    elif R < total:
        return
    
    for i in range(N):
        if not bits & 1 << i and check[bits | 1 << i]:
            check[bits | 1 << i] = False
            new_easy = problems[i] if problems[i] < easy else easy
            new_hard = problems[i] if problems[i] > hard else hard
            pick(bits | 1 << i, total + problems[i], new_easy, new_hard)


N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
check = [True] * (1 << N)
cnt = 0
pick()
print(cnt)