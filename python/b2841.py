import sys
input = sys.stdin.readline

N, P = map(int, input().split())

pushing_fret = [[] for _ in range(6)]

cnt = 0
for _ in range(N):
    line, frat = map(int, input().split())
    line -= 1
    frat -= 1

    while pushing_fret[line]:
        if pushing_fret[line][-1] > frat:
            del(pushing_fret[line][-1])
            cnt += 1
        else:
            break

    if not pushing_fret[line] or pushing_fret[line][-1] != frat:
        pushing_fret[line].append(frat)
        cnt += 1

print(cnt)