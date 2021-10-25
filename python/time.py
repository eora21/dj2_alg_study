import time

result = []
start = time.time()
for i in range(1000000):
    result.append([1, 2, 3])
    q = result.pop()
    a = q[0]
    b = q[1]
    c = [2]
end = time.time()
print(end - start)

start = time.time()
for i in range(1000000):
    result.append((1, 2, 3))
    q = result.pop()
    a = q[0]
    b = q[1]
    c = [2]
end = time.time()
print(end - start)

start = time.time()
for i in range(1000000):
    result.append((1, 2, 3))
    a, b, c = result.pop()
end = time.time()
print(end - start)