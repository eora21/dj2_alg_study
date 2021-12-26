import sys
input = sys.stdin.readline

N = int(input())
score = []
turn = []
total = 0

for _ in range(N):
    hw = list(map(int, input().split()))
    if hw[0]:
        score.append(hw[1])
        turn.append(hw[2])
    
    if turn:
        if turn[-1] == 1:
            turn.pop()
            total += score.pop()
        else:
            turn[-1] -= 1

print(total)