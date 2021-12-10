N, K = map(int, input().split())
people = list(range(1, N + 1))

rear = 0
print('<', end="")
while N > 1:
    rear = (rear + (K - 1)) % N
    print("{}, ".format(people.pop(rear)), end="")
    N -= 1
print("{}>".format(people[0]))
