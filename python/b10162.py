T = int(input())

button = [300, 60, 10]
check = [0, 0, 0]

for i in range(3):
    check[i] = T // button[i]
    T %= button[i]

if T == 0:
    print(*check)
else:
    print(-1)