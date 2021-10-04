from typing import Deque
from sys import stdin
input = stdin.readline

n = int(input())

stack = Deque()
i = 1
op = Deque()
for _ in range(n):
    num = int(input())
    if i > num and stack[-1] > num:
        print("NO")
        break
    while i <= num:
        stack.append(i)
        op.append("+")
        i += 1
    stack.pop()
    op.append("-")
else:
    for o in op:
        print(o)
