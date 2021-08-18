from sys import stdin

li = []

dic = dict(
    push = lambda x: li.append(x),
    pop = lambda: li.pop(0) if li else -1,
    size = lambda: len(li),
    empty = lambda: 0 if li else 1,
    front = lambda: li[0] if li else -1,
    back= lambda: li[-1] if li else -1,
)


for _ in range(int(stdin.readline())):
    command = stdin.readline().split()
    if "push" in command:
        dic["push"](command[1])
    else:
        print(dic[command[0]]())