sugar = int(input())

k = 9999

for i in range((sugar // 3) + 1):
    for j in range((sugar - (3 * i) // 5) + 1):
        if sugar == 3 * i + 5 * j and k > i + j:
            k = i + j

if k != 9999:
    print(k)
else:
    print(-1)
