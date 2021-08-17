from sys import stdin

T = int(stdin.readline())
sticks = [int(stdin.readline()) for _ in range(T)]
highest = 0
cnt = 0

for i in range(len(sticks) - 1, -1, -1):
    if highest < sticks[i]:
        cnt += 1
        highest = sticks[i]

print(cnt)