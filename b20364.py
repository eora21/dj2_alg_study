import sys
input = sys.stdin.readline

def field_check(num):
    if num >= N:
        return
    else:
        if fields[num] > field:
            fields[num] = field
            field_check((num+1) * 2 - 1)
            field_check((num+1) * 2)


N, Q = map(int, input().split())
fields = [N + 1] * N

for _ in range(Q):
    field = int(input())
    field -= 1
    if fields[field] == N + 1:
        print(0)
        field_check(field)
    else:
        print(fields[field] + 1)