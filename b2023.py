queue = [2, 3, 5, 7]
adder = [1, 3, 7, 9]
N = int(input())
cnt = 1
while N > cnt:
    while queue[0] < 10 ** cnt:
        for i in range(4):
            num = queue[0] * 10 + adder[i]
            for check in range(2, int(num ** 0.5) + 1):
                if not num % check:
                    break
            else:
                queue.append(num)
        del(queue[0])
    cnt += 1
else:
    while queue:
        print(queue[0])
        del(queue[0])
   