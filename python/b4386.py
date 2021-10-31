n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
check = [True] * n
check[0] = False

total_score = 0
for _ in range(n - 1):
    min_score = 1000000
    want = 0
    for mine in range(n):
        if not check[mine]:
            for target in range(n):
                if check[target]:
                    score = ((stars[mine][0] - stars[target][0]) ** 2 + (stars[mine][1] - stars[target][1]) ** 2) ** 0.5
                    if min_score > score:
                        min_score = score
                        want = target
    
    total_score += min_score
    check[want] = False

print("{:.2f}".format(total_score))