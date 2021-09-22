case = 1

while True:
    L, P, V = map(int, input().split())
    if not(L or P or V):
        break

    cnt = V // P * L
    V %= P

    if L < V < P:
        cnt += L

    else:
        cnt += V

    print("Case {}: {}".format(case, cnt))
    case += 1
