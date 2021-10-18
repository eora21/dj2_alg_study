import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
stack = []

for i in range(N):
    building = int(input())
    while stack:
        if stack[-1] <= building:
            del(stack[-1])
        else:
            break
    stack.append(building)
    cnt += len(stack) - 1
    
print(cnt)