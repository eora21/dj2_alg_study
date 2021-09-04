adder = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def check(r, c):
    queue = [(r, c)]
    cnt = 1
    while queue:
        r, c = queue.pop(0)
        for arrow in range(4):
            y_adder, x_adder = adder[arrow]
            if 0 <= r + y_adder < N and 0 <= c + x_adder < N and arr[r + y_adder][c + x_adder]:
                arr[r + y_adder][c + x_adder] = 0
                queue.append((r + y_adder, c + x_adder))
                cnt += 1
    
    return cnt


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

li = []

for row in range(N):
    for col in range(N):
        if arr[row][col]:
            arr[row][col] = 0
            li.append(check(row, col))

li.sort()

print(len(li))
for num in li:
    print(num)