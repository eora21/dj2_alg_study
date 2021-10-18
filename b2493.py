from typing import Deque

N = int(input())
ans = [0] * N
nums = list(map(int, input().split()))
stack = Deque()
for idx in range(N):
    while stack:
        if nums[stack[-1]] < nums[idx]:
            stack.pop()
        else:
            ans[idx] = stack[-1] + 1
            break
    
    stack.append(idx)
    
print(*ans)
