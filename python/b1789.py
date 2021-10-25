S = int(input())

total = 0
cnt = 0
for i in range(1, S + 1):
    total += i
    cnt += 1
    if total == S:
        break
    elif total > S:
        cnt -= 1
        break

print(cnt)