N = int(input())

num = ["X"] * 10
num[9] = -1
cnt = -1

while cnt < N:
    num[9] += 1
    flag = False
    for i in range(10):
        if num[i] == "X":
            continue

        if num[i] == 10:
            num[i-1] = 10 - i
            flag = True
            
        elif i > 0 and num[i-1] != "X" and num[i-1] <= num[i]:
            num[i-1] += 1
            flag = True
        
        if flag:
            for j in range(i, 10):
                num[j] = 9 - j
            num[9] -= 1
            break
    else:
        cnt += 1

    if num[0] == 10:
        break

if num[0] == 10:
    print(-1)
else:
    for i in range(0, 10):
        if num[i] != "X":
            print(num[i], end="")