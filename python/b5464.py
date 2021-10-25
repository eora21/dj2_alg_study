def enter_parking_lot(car):
    for i in range(N):
            if not parking_lot[i]:
                parking_lot[i] = car
                break
    else:
        queue.append(car)


N, M = map(int, input().split())
Rs = []
Wk = [0]
parking_lot = [0] * N
queue = []
for _ in range(N):
    Rs.append(int(input()))

for _ in range(M):
    Wk.append(int(input()))

costs = 0
for _ in range(2*M):
    c = int(input())
    
    if c > 0:
        enter_parking_lot(c)

    else:
        c *= -1
        for i in range(N):
            if parking_lot[i] == c:
                parking_lot[i] = 0
                costs += Rs[i] * Wk[c]
                if queue:
                    enter_parking_lot(queue.pop(0))
                break
        
print(costs)
