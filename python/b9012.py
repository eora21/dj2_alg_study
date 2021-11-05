import sys
input = sys.stdin.readline

par = {"(": True, ")": False}
stack = []
for _ in range(int(input())):
    stack.clear()
    PS = input()
    for ch in PS:
        try:
            if par[ch]:
                stack.append(1)
            else:
                stack.pop()
        except:
            print("NO")
            break
    else:
        if stack:
            print("NO")
        else:
            print("YES")