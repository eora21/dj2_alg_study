A, B = map(int, input().split())
L = R = 0

while A != B:
    if A == 1:
        R += B - 1
        B = 1
    elif B == 1:
        L += A - 1
        A = 1
    elif A > B:
        L += A // B
        A %= B
    elif A < B:
        R += B // A
        B %= A

print(L, R)
