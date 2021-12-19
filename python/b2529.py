bs = {
    "<": lambda before, now: True if before < now else False,
    ">": lambda before, now: True if before > now else False,
    }


def DFS(repeat=-1, val=0, bef=0):
    if repeat == k:
        global min_val, max_val
        if min_val > val:
            min_val = val
        if max_val < val:
            max_val = val
        return

    for n in range(10):
        if check[n]:
            if repeat == -1 or bs[op[repeat]](bef, n):
                check[n] = False
                new_val = val * 10 + n
                DFS(repeat + 1, new_val, n)
                check[n] = True


k = int(input())
op = input().split()
check = [True] * 10
min_val = 9876543210
max_val = 0
DFS()
print(max_val)
print(("{0:0>%d}"%(k+1)).format(min_val))