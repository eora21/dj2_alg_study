N = int(input())
birds = []
for i in range(N):
    birds.append(input().split())

total = input().split()
fly = 0
ans = True
for word in total:
    for bird in birds:
        if bird and word == bird[0]:
            del(bird[0])
            if not bird:
                fly += 1
            break
    else:
        ans = False
        break

if fly != N:
    ans = False

print("Possible" if ans else "Impossible")