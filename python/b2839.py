sugar = int(input())

k = -1

for i in range((sugar // 5), -1, -1):
    for j in range((sugar - (5 * i) // 3) + 1):
        if sugar == 5 * i + 3 * j:
            k = i + j
            break
    if k != -1:
        break

print(k)