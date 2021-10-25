def palindrome(st, flag):
    i = 0
    while i < len(st) // 2:
        if st[i] != st[-(i + 1)]:
            if flag:
                    return (palindrome(st[i: len(st) - 1 - i], False) and palindrome(st[i + 1: len(st) - i], False)) + 1
            else:
                return 1
        i += 1
    return 0

T = int(input())

for _ in range(T):
    print(palindrome(input(), True))