for case in range(int(input())):
    N, M = map(int, input().split())

    for _ in range(M):
        input()
    
    print(N - 1)

    # flights = [[] for _ in range(M)]
    # visited = [True] * M
    # stack = [0]
    # visited[0] = False

    # for _ in range(M):
    #     a, b = map(int, input().split())
    #     flights[a-1].append(b-1)
    #     flights[b-1].append(a-1)
    
    # while stack:
    #     now_country = stack.pop()
    #     while flights[now_country]:
    #         country = flights[now_country][0]
    #         if visited[country]:
    #             stack.append(country)
    #             visited[country] = False
    #         del(flights[now_country][0])