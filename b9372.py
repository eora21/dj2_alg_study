import sys
from sys import stdin

for case in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())

    [stdin.readline() for _ in range(M)]
    
    print(N - 1)