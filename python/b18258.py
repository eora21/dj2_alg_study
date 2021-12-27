from typing import Deque
import sys
readline = sys.stdin.readline


def push(x):
    queue.append(x)


def pop():
    print(queue.popleft() if queue else "-1")


def size():
    print(len(queue))


def empty():
    print(0 if queue else 1)


def front():
    print(queue[0] if queue else "-1")


def back():
    print(queue[-1] if queue else "-1")


op = {"push": push, "pop": pop, "size": size, "empty": empty, "front": front, "back": back}

N = int(input())
queue = Deque()
for _ in range(N):
    user_op = readline().split()
    if len(user_op) > 1:
        op["push"](user_op[1])
    else:
        op[user_op[0]]()