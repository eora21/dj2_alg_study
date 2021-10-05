from typing import Deque
import sys
input = sys.stdin.readline

n = int(input())

stack = Deque()
op = Deque()
i = 1
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
    print("\n".join(op))
