import time
start = time.time()

S = int(input())

N = 0

num = 2 ** (S // 2) + 1
for i in range(num):
    binary = bin(i)[2:]

    if binary.count("1") > N:
        total = 0
        for p in range(len(binary)):
            if binary[p] == '1':
                total += p + 1
        if total == S:
            N = binary.count("1")

print(N)
print("time :", time.time() - start)