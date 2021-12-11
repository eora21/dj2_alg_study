n, w, L = map(int, input().split())
trucks = list(map(int , input().split()))
on_turn = [0] * n

on_weight = 0
turn = 1
rear = 0
head = 0
while rear < n:
    if on_turn[head] != 0 and on_turn[head] + w == turn:
        on_weight -= trucks[head]
        head += 1

    if on_weight + trucks[rear] <= L:
        on_turn[rear] = turn
        on_weight += trucks[rear]
        rear += 1
        turn += 1
    else:
        turn = on_turn[head] + w

print(turn + w - 1)
