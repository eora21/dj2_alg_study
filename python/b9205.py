import sys
input = sys.stdin.readline


def DFS():
    check = [True] * (n + 2)
    check[0] = False

    while stack:
        idx = stack.pop()
        if idx == n + 1:
            return True
        
        for i in range(1, n + 2):
            if check[i] and abs(node[idx][0] - node[i][0]) + abs(node[idx][1] - node[i][1]) <= 1000:
                check[i] = False
                stack.append(i)


t = int(input())
for case in range(t):
    n = int(input())
    node = [list(map(int, input().split())) for _ in range(n + 2)]

    stack = [0]
    print("happy" if DFS() else "sad")
