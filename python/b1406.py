import sys
from typing import Deque
readline = sys.stdin.readline

left_list = list(input())
right_list = Deque()

M = int(readline())

for _ in range(M):
    op = readline()
    if op[0] == 'L':
        if left_list:
            right_list.appendleft(left_list.pop())
    elif op[0] == 'D':
        if right_list:
            left_list.append(right_list.popleft())
    elif op[0] == 'B':
        if left_list:
            del(left_list[-1])
    else:
        left_list.append(op[2])

print(''.join(left_list), end='')
print(''.join(right_list))
