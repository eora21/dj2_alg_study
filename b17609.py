def palindrome(st, flag):
    while len(st) > 1:
        if st[0] != st[-1]:
            if flag:
                return (palindrome(st[0:-1], False) and palindrome(st[1:], False)) + 1
            else:
                return 1
        st = st[1: -1]
    return 0

T = int(input())

for _ in range(T):
    print(palindrome(input(), True))

