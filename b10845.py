from sys import stdin

def push(Q, N):
    Q.append(N)


def pop(Q):
    print(Q.pop(0) if len(Q) else -1)


def size(Q):
    print(len(Q))


def empty(Q):
    print(0 if len(Q) else 1)


def front(Q):
    print(Q[0] if len(Q) else -1)


def back(Q):
    print(Q[-1] if len(Q) else -1)


dic = {"pop": pop, "size": size, "empty": empty, "front": front, "back": back}

li = []

for _ in range(int(stdin.readline())):
    command = stdin.readline().split()
    if "push" in command:
        push(li, command[1])
    else:
        dic[command[0]](li)