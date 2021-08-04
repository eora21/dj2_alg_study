get = 1000 - int(input())

less = [500, 100, 50, 10, 5, 1]
cnt = 0

for m in less:
    cnt += get // m
    get %= m

print(cnt)