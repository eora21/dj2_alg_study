import sys
input = sys.stdin.readline

for case in range(int(input())):
    N = int(input())
    
    score = []

    for _ in range(N):
        score.append(list(map(int, input().split())))
    
    score.sort(key=lambda x: x[0])

    min_score = N + 1
    cnt = 0

    for i in range(N):
        if score[i][1] < min_score:
            cnt += 1
            min_score = score[i][1]

    print(cnt)
