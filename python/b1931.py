from sys import stdin

T = int(stdin.readline())

li = []
for _ in range(T):
    li.append(list(map(int, stdin.readline().split())))

li.sort(key=lambda x : (x[1], x[0]))

StartTime = 0
cnt = 0

for i in range(len(li)):
    if StartTime <= li[i][0]:
        cnt += 1
        StartTime = li[i][1]

print(cnt)